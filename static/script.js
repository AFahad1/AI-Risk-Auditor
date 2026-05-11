const state = {
  framework:      "SOC 2",
  orgName:        "",
  assignee:       "",
  employeeCount:  null,
  phase:          "employee_count",   // "employee_count" | "assessment"
  questions:      [],
  currentIndex:   0,
  followUpCount:  0,
  controlHistory: [],   // [{role, content}] — resets per control
  results:        [],
  isProcessing:   false
};

// ── SETUP ──────────────────────────────────────────────

const defaultCard = document.querySelector(".framework-card[data-framework='SOC 2']");
if (defaultCard) {
  defaultCard.classList.add("selected");
  state.framework = "SOC 2";
}

document.querySelectorAll(".framework-card").forEach(card => {
  card.addEventListener("click", () => {
    document.querySelectorAll(".framework-card").forEach(c => c.classList.remove("selected"));
    card.classList.add("selected");
    state.framework = card.dataset.framework;
  });
});

document.getElementById("start-btn").addEventListener("click", startAssessment);

async function startAssessment() {
  const orgName  = document.getElementById("org-name").value.trim();
  const assignee = document.getElementById("assignee").value.trim();
  const errorEl  = document.getElementById("setup-error");

  if (!orgName) { showSetupError("Please enter your organisation name."); return; }
  errorEl.style.display = "none";

  state.orgName  = orgName;
  state.assignee = assignee;

  const btn = document.getElementById("start-btn");
  btn.textContent = "Loading…";
  btn.disabled    = true;

  try {
    const res = await fetch(`/api/questions/${encodeURIComponent(state.framework)}`);
    state.questions = await res.json();
  } catch {
    showSetupError("Failed to load questions. Is the server running?");
    btn.textContent = "Start Assessment →";
    btn.disabled    = false;
    return;
  }

  document.getElementById("setup-screen").style.display = "none";
  document.getElementById("chat-screen").style.display  = "flex";
  document.getElementById("sb-framework").textContent   = state.framework;
  document.getElementById("sb-org").textContent         = state.orgName;

  updateProgress();

  addBotMessage(
    `Welcome. I'll be your <strong>${state.framework}</strong> compliance auditor for ` +
    `<strong>${state.orgName}</strong> today. We have <strong>${state.questions.length} controls</strong> ` +
    `to work through. For each one I may ask a few follow-up questions before we move on. ` +
    `Answer as honestly and specifically as you can.`,
    true
  );

  setTimeout(() => {
    addBotMessage("Before we begin — approximately how many employees does your organisation have?");
    enableInput();
  }, 1000);
}

function showSetupError(msg) {
  const el = document.getElementById("setup-error");
  el.textContent    = msg;
  el.style.display  = "block";
}

// ── CONTROL LIFECYCLE ──────────────────────────────────

async function loadControl(index) {
  if (index >= state.questions.length) {
    completeAssessment();
    return;
  }

  state.currentIndex   = index;
  state.followUpCount  = 0;
  state.controlHistory = [];
  state.isProcessing   = false;

  updateProgress();
  addControlDivider(index);

  // Claude generates the opening question — history is empty
  await callAuditor();
}

async function submitAnswer() {
  const input  = document.getElementById("answer-input");
  const answer = input.value.trim();
  if (!answer || state.isProcessing) return;

  disableInput();
  input.value = "";
  addUserMessage(answer);

  if (state.phase === "employee_count") {
    state.employeeCount = answer;
    state.phase         = "assessment";
    addBotMessage(`Got it — ${answer}. Let's begin the assessment.`);
    setTimeout(() => loadControl(0), 1000);
    return;
  }

  state.isProcessing = true;

  // Append user answer to history before sending
  state.controlHistory = [...state.controlHistory, { role: "user", content: answer }];

  await callAuditor();
}

async function callAuditor() {
  const control    = state.questions[state.currentIndex];
  const isOpening  = state.controlHistory.length === 0;
  const thinkingId = addThinking();

  try {
    const res = await fetch("/api/chat", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        framework:       state.framework,
        control:         control,
        history:         state.controlHistory,
        follow_up_count: state.followUpCount,
        assignee:        state.assignee,
        employee_count:  state.employeeCount
      })
    });

    const data = await res.json();
    removeThinking(thinkingId);

    if (!data.success) {
      addBotMessage("I encountered an error. Please try again.");
      enableInput();
      state.isProcessing = false;
      return;
    }

    const { result, history } = data;
    state.controlHistory = history;

    if (result.action === "followup") {
      // Opening question does not count toward the 3 follow-up limit
      if (!isOpening) state.followUpCount++;
      addBotMessage(result.message);
      enableInput();
      state.isProcessing = false;

    } else if (result.action === "assess") {
      disableInput();
      addAssessmentCard(result.message, result.data, state.currentIndex);
      state.results.push(result.data);
      updateProgress();

      // Auto-advance to next control after a pause
      setTimeout(() => loadControl(state.currentIndex + 1), 3500);
    }

  } catch {
    removeThinking(thinkingId);
    addBotMessage("Connection error. Please try again.");
    enableInput();
    state.isProcessing = false;
  }
}

// ── COMPLETION ─────────────────────────────────────────

function completeAssessment() {
  const total   = state.results.length;
  const open    = state.results.filter(r => r.status === "OPEN").length;
  const treated = state.results.filter(r => r.status === "TREATED").length;
  const closed  = state.results.filter(r => r.status === "CLOSED").length;
  const avgL    = (state.results.reduce((s, r) => s + (r.residual_risk_likelihood || 0), 0) / total).toFixed(1);
  const avgI    = (state.results.reduce((s, r) => s + (r.residual_risk_impact     || 0), 0) / total).toFixed(1);

  const html = `
    <div class="completion-card">
      <h3>Assessment Complete</h3>
      <p>Here is a summary of your <strong>${state.framework}</strong> risk assessment for <strong>${state.orgName}</strong>.</p>
      <div class="stat-grid">
        <div class="stat-box"><div class="stat-num">${total}</div><div class="stat-label">Controls Assessed</div></div>
        <div class="stat-box"><div class="stat-num">${open}</div><div class="stat-label">Open Risks</div></div>
        <div class="stat-box"><div class="stat-num">${treated}</div><div class="stat-label">Treated</div></div>
        <div class="stat-box"><div class="stat-num">${closed}</div><div class="stat-label">Closed</div></div>
        <div class="stat-box"><div class="stat-num">${avgL}</div><div class="stat-label">Avg Residual Likelihood</div></div>
        <div class="stat-box"><div class="stat-num">${avgI}</div><div class="stat-label">Avg Residual Impact</div></div>
      </div>
      <p style="margin-top:14px;color:#475569;font-size:13px;">
        Click <strong>Download CSV Report</strong> in the sidebar to export your full risk register.
      </p>
    </div>`;

  addBotMessage(html, true);
  document.getElementById("download-btn").style.display  = "block";
  document.querySelector(".input-area").style.display    = "none";
  updateProgress();
}

async function downloadCSV() {
  const res  = await fetch("/api/export", {
    method:  "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ results: state.results, framework: state.framework })
  });
  const blob = await res.blob();
  const url  = URL.createObjectURL(blob);
  const a    = document.createElement("a");
  a.href     = url;
  a.download = `${state.framework.replace(/\s/g, "_")}_risk_assessment.csv`;
  a.click();
  URL.revokeObjectURL(url);
}

// ── UI HELPERS ─────────────────────────────────────────

function addControlDivider(index) {
  const msgs  = document.getElementById("messages");
  const total = state.questions.length;
  const div   = document.createElement("div");
  div.className   = "control-divider";
  div.innerHTML   = `<span>Control ${index + 1} of ${total}</span>`;
  msgs.appendChild(div);
  msgs.scrollTop  = msgs.scrollHeight;
}

function addBotMessage(content, isHtml = false) {
  const msgs = document.getElementById("messages");
  const div  = document.createElement("div");
  div.className = "message bot-message";
  div.innerHTML = `
    <div class="avatar"><span class="bot-dot"></span></div>
    <div class="bubble">${isHtml ? content : escapeHtml(content)}</div>`;
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
}

function addUserMessage(text) {
  const msgs = document.getElementById("messages");
  const div  = document.createElement("div");
  div.className = "message user-message";
  div.innerHTML = `<div class="bubble">${escapeHtml(text)}</div>`;
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
}

function addThinking() {
  const msgs = document.getElementById("messages");
  const div  = document.createElement("div");
  const id   = "thinking-" + Date.now();
  div.id        = id;
  div.className = "message bot-message thinking";
  div.innerHTML = `
    <div class="avatar"><span class="bot-dot"></span></div>
    <div class="bubble"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>`;
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
  return id;
}

function removeThinking(id) {
  const el = document.getElementById(id);
  if (el) el.remove();
}

function addAssessmentCard(message, data, index) {
  const statusClass = {
    OPEN:     "badge-open",
    ASSESSED: "badge-assessed",
    TREATED:  "badge-treated",
    CLOSED:   "badge-closed"
  }[data.status] || "badge-open";

  const html = `
    <div class="assess-intro">${escapeHtml(message)}</div>
    <div class="assess-card">
      <div class="assess-header">
        <span class="assess-title">${escapeHtml(data.name)}</span>
        <span class="badge ${statusClass}">${data.status}</span>
      </div>
      <div class="assess-body">
        <div class="assess-row">
          <span class="assess-label">Category</span>
          <span class="assess-value">${escapeHtml(data.category)}</span>
        </div>
        <div class="assess-row">
          <span class="assess-label">Residual Risk</span>
          <span class="assess-value">Likelihood ${data.residual_risk_likelihood}/5 · Impact ${data.residual_risk_impact}/5</span>
        </div>
        <div class="assess-row">
          <span class="assess-label">Tool</span>
          <span class="assess-value">${escapeHtml(data.application_name)}</span>
        </div>
        <div class="assess-row">
          <span class="assess-label">Treatment</span>
          <span class="assess-value">${escapeHtml(data.treatment)}</span>
        </div>
      </div>
    </div>
    <div class="assess-footer">Moving to the next control…</div>`;

  const msgs = document.getElementById("messages");
  const div  = document.createElement("div");
  div.className = "message bot-message";
  div.innerHTML = `<div class="avatar"><span class="bot-dot"></span></div><div class="bubble assess-bubble">${html}</div>`;
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
}

function updateProgress() {
  const total = state.questions.length;
  const done  = state.results.length;
  const pct   = total > 0 ? Math.round((done / total) * 100) : 0;
  document.getElementById("progress-bar").style.width    = pct + "%";
  document.getElementById("progress-text").textContent   = `${done} / ${total}`;
}

function enableInput() {
  const inp = document.getElementById("answer-input");
  const btn = document.getElementById("send-btn");
  inp.disabled = false;
  btn.disabled = false;
  inp.focus();
}

function disableInput() {
  document.getElementById("answer-input").disabled = true;
  document.getElementById("send-btn").disabled     = true;
}

function escapeHtml(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

document.getElementById("answer-input").addEventListener("keydown", e => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    submitAnswer();
  }
});

document.getElementById("send-btn").addEventListener("click", submitAnswer);
