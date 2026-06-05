QUESTIONS = {
    "SOC 2": [
        {
            "id": "RSK001",
            "question": "Are there adequate controls in place to prevent unauthorized logical access to internal networks?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 3
        },
        {
            "id": "RSK002",
            "question": "Are adequate measures in place to control access to critical internal IT infrastructure and production servers?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 2
        },
        {
            "id": "RSK003",
            "question": "Are there policies restricting the usage of external storage devices, and are they effectively enforced?",
            "loss_of_cia": "C,I,A",
            "likelihood": 4,
            "impact": 5
        },
        {
            "id": "RSK004",
            "question": "Are there measures to prevent unauthorized access to colleagues' laptops or other devices? (what kind of authentication are the laptops having?)",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK005",
            "question": "Are identity and access management (IAM) policies (or any services you are using) in place to ensure strong authentication mechanisms for all users?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 4
        },
        {
            "id": "RSK006",
            "question": "Are all critical network components configured to use multi-factor authentication (MFA)?",
            "loss_of_cia": "I,A",
            "likelihood": 3,
            "impact": 5
        },
        {
            "id": "RSK007",
            "question": "Are there policies to ensure that all company assets, such as laptops, are returned upon employee exit?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 4
        },
        {
            "id": "RSK008",
            "question": "Are software applications and systems regularly updated to mitigate potential vulnerabilities?",
            "loss_of_cia": "C,I,A",
            "likelihood": 5,
            "impact": 4
        },
        {
            "id": "RSK009",
            "question": "Is there a process to prevent the installation of pirated or unauthorized software on company systems?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK010",
            "question": "Is there a patch management process in place to ensure Linux servers are regularly updated?",
            "loss_of_cia": "C,I,A",
            "likelihood": 4,
            "impact": 5
        },
        {
            "id": "RSK011",
            "question": "Are known system vulnerabilities being actively identified, managed, and patched?",
            "loss_of_cia": "C,I",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK012",
            "question": "Are APIs properly configured and secured to prevent unauthorized access or data breaches?",
            "loss_of_cia": "C,I,A",
            "likelihood": 3,
            "impact": 3
        },
        {
            "id": "RSK013",
            "question": "Are measures in place to protect the organization against malware attacks, and is monitoring in place?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK014",
            "question": "Are adequate logging and monitoring processes in place to ensure security incidents are identified and addressed promptly?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK015",
            "question": "Are databases encrypted to protect sensitive data from unauthorized access?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK016",
            "question": "Are company laptops equipped with full disk encryption to protect data in case of theft or loss?",
            "loss_of_cia": "I,A",
            "likelihood": 4,
            "impact": 5
        },
        {
            "id": "RSK017",
            "question": "Are encryption and access control measures in place to prevent data breaches involving sensitive business information?",
            "loss_of_cia": "I,A",
            "likelihood": 4,
            "impact": 5
        },
        {
            "id": "RSK018",
            "question": "Is there a secure process for disposing of hardware containing sensitive data?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK019",
            "question": "Are secure methods in place for the electronic transfer of sensitive information? - For example via Microsoft Sharepoint, Google Workspace.",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK020",
            "question": "Are controls in place to prevent data loss during migrations, deletions, or storage failures?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK021",
            "question": "Are physical access controls in place to prevent unauthorized access to the premises?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK022",
            "question": "Are FTP and HTTP services properly secured or disabled on the firewall to prevent unauthorized access?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK023",
            "question": "Are there redundancies in place to mitigate the risk of a primary cloud failure?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 4
        },
        {
            "id": "RSK024",
            "question": "Are network devices monitored, and are backups available to prevent operational downtime in case of failure?",
            "loss_of_cia": "I,A",
            "likelihood": 3,
            "impact": 5
        },
        {
            "id": "RSK025",
            "question": "Is there a contingency plan in place for internet service disruptions at the supplier's end?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK026",
            "question": "Are employees regularly trained on information security policies and requirements to ensure compliance?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK027",
            "question": "Are systems in place to ensure high resource utilization does not prevent customer access to production servers?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK028",
            "question": "Does the organization have a business continuity plan for events such as riots, pandemics, or natural disasters?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK029",
            "question": "Is there a risk of becoming dependent on a single cloud security provider or platform (vendor lock-in)?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "RSK030",
            "question": "Are systems protected from Denial of Service (DoS) attacks, and are robust mechanisms in place to prevent such incidents?",
            "loss_of_cia": "I,A",
            "likelihood": 1,
            "impact": 5
        },
    ]
}

# ISO 27001 uses the same questionnaire as SOC 2
QUESTIONS["ISO 27001"] = QUESTIONS["SOC 2"]


# ── GAP ASSESSMENT QUESTIONS ──────────────────────────────────────────────────

GAP_QUESTIONS = {
    "ISO 27001": [
        # ── Leadership ────────────────────────────────────────────────────────
        {"id": "GAP-ISO-001", "section": "Leadership", "control_area": "Top Management Commitment",
         "question": "Is there documented evidence of top management commitment (signed policy, meeting minutes, resource allocation)?"},
        {"id": "GAP-ISO-002", "section": "Leadership", "control_area": "Information Security Policy",
         "question": "Has an overarching Information Security Policy been formally approved by senior management and communicated to all staff?"},
        {"id": "GAP-ISO-003", "section": "Leadership", "control_area": "Roles & Responsibilities",
         "question": "Are ISMS roles and responsibilities formally defined, documented, and assigned to named individuals?"},
        {"id": "GAP-ISO-004", "section": "Leadership", "control_area": "CISO / ISO Role",
         "question": "Has an Information Security Officer been formally designated with defined authority and reporting lines?"},

        # ── Planning ──────────────────────────────────────────────────────────
        {"id": "GAP-ISO-005", "section": "Planning", "control_area": "Risk Assessment Process",
         "question": "Is there a documented, repeatable risk assessment methodology (asset identification, threat/vulnerability analysis, likelihood/impact scoring)?"},
        {"id": "GAP-ISO-006", "section": "Planning", "control_area": "Risk Treatment Plan",
         "question": "Has a formal Risk Treatment Plan (RTP) been produced and approved, mapping risks to controls?"},
        {"id": "GAP-ISO-007", "section": "Planning", "control_area": "Statement of Applicability",
         "question": "Has a Statement of Applicability been prepared listing all Annex A controls with inclusion/exclusion justification?"},
        {"id": "GAP-ISO-008", "section": "Planning", "control_area": "Risk Acceptance",
         "question": "Has senior management formally accepted residual risks documented in the risk treatment plan?"},
        {"id": "GAP-ISO-009", "section": "Planning", "control_area": "ISMS Objectives",
         "question": "Are measurable information security objectives established and monitored (e.g., incident response SLA, patch compliance rate, training completion)?"},
        {"id": "GAP-ISO-010", "section": "Planning", "control_area": "Planning for Changes",
         "question": "Is there a formal process to evaluate information security implications before implementing organizational or system changes?"},

        # ── Support ───────────────────────────────────────────────────────────
        {"id": "GAP-ISO-011", "section": "Support", "control_area": "Resources",
         "question": "Have sufficient resources (budget, personnel, tools) been formally allocated for ISMS operations?"},
        {"id": "GAP-ISO-012", "section": "Support", "control_area": "Competence",
         "question": "Are competency requirements documented for ISMS roles, with training records maintained as evidence?"},
        {"id": "GAP-ISO-013", "section": "Support", "control_area": "Awareness",
         "question": "Can the organization demonstrate that all staff are aware of the ISMS policy, their role in it, and the consequences of non-compliance?"},
        {"id": "GAP-ISO-014", "section": "Support", "control_area": "Communication",
         "question": "Is there a documented information security communication plan (who communicates what, when, and to whom)?"},
        {"id": "GAP-ISO-015", "section": "Support", "control_area": "Document Control",
         "question": "Is there a document control procedure governing creation, review, approval, versioning, and retention of ISMS documents?"},
        {"id": "GAP-ISO-016", "section": "Support", "control_area": "Document Retention",
         "question": "Are document retention periods defined and enforced for all ISMS-relevant records?"},

        # ── Operation ─────────────────────────────────────────────────────────
        {"id": "GAP-ISO-017", "section": "Operation", "control_area": "Operational Planning",
         "question": "Are operational security procedures documented and controlled for all processes within ISMS scope?"},
        {"id": "GAP-ISO-018", "section": "Operation", "control_area": "Risk Assessment (Periodic)",
         "question": "Are risk assessments performed at planned intervals and when significant changes occur, with results documented?"},
        {"id": "GAP-ISO-019", "section": "Operation", "control_area": "Risk Treatment",
         "question": "Are risk treatment actions tracked to completion, with evidence of control implementation?"},
        {"id": "GAP-ISO-020", "section": "Operation", "control_area": "Change Management Controls",
         "question": "Is there a formal change advisory process with a cybersecurity review gate before production changes are implemented?"},
        {"id": "GAP-ISO-021", "section": "Operation", "control_area": "Application Whitelisting",
         "question": "Have approved application lists been defined and enforced on endpoints?"},
        {"id": "GAP-ISO-022", "section": "Operation", "control_area": "Network Boundary - Guest Access",
         "question": "Are LAN cables and direct network access restricted from guests and third parties?"},
        {"id": "GAP-ISO-023", "section": "Operation", "control_area": "Audit Log Protection",
         "question": "Are event logs protected from unauthorized access, modification, and deletion?"},
        {"id": "GAP-ISO-024", "section": "Operation", "control_area": "Cloud Storage Blocking",
         "question": "Is unauthorized use of personal cloud storage (Google Drive, Dropbox) blocked at the firewall?"},
        {"id": "GAP-ISO-025", "section": "Operation", "control_area": "Patch Management Automation",
         "question": "Is automated patch management fully operational and enforced across all endpoints?"},
        {"id": "GAP-ISO-026", "section": "Operation", "control_area": "Proxy Routing",
         "question": "Is all outbound traffic routed through an approved proxy server?"},

        # ── Performance Evaluation ────────────────────────────────────────────
        {"id": "GAP-ISO-027", "section": "Performance Evaluation", "control_area": "Monitoring & Measurement",
         "question": "Are defined security KPIs monitored regularly and reported to management?"},
        {"id": "GAP-ISO-028", "section": "Performance Evaluation", "control_area": "SIEM / SOC Coverage",
         "question": "Does monitoring extend to all in-scope systems with documented alert thresholds and escalation paths?"},
        {"id": "GAP-ISO-029", "section": "Performance Evaluation", "control_area": "Internal Audit Program",
         "question": "Is there a formal annual ISMS internal audit program with documented plans, reports, and corrective actions?"},
        {"id": "GAP-ISO-030", "section": "Performance Evaluation", "control_area": "Audit Independence",
         "question": "Are internal ISMS audits conducted by personnel independent of the area being audited?"},
        {"id": "GAP-ISO-031", "section": "Performance Evaluation", "control_area": "Management Review",
         "question": "Are formal ISMS management reviews conducted at planned intervals with documented inputs and outputs?"},
        {"id": "GAP-ISO-032", "section": "Performance Evaluation", "control_area": "Review Inputs",
         "question": "Do management review records include audit results, risk treatment status, incidents, metrics, and stakeholder feedback?"},

        # ── Improvement ───────────────────────────────────────────────────────
        {"id": "GAP-ISO-033", "section": "Improvement", "control_area": "Continual Improvement",
         "question": "Is there a documented process to identify ISMS improvement opportunities beyond reactive incident response?"},
        {"id": "GAP-ISO-034", "section": "Improvement", "control_area": "Nonconformity & Corrective Action",
         "question": "When a nonconformity occurs, is there a process to identify root cause, implement corrective action, and verify effectiveness?"},
        {"id": "GAP-ISO-035", "section": "Improvement", "control_area": "Corrective Action Tracking",
         "question": "Are open corrective actions tracked in a register with target dates and owners, reviewed in management meetings?"},

        # ── People ────────────────────────────────────────────────────────────
        {"id": "GAP-ISO-036", "section": "People", "control_area": "Screening",
         "question": "Are background checks conducted for all employees and contractors prior to employment?"},
        {"id": "GAP-ISO-037", "section": "People", "control_area": "Terms & Conditions",
         "question": "Do employment contracts include information security responsibilities and confidentiality obligations?"},
        {"id": "GAP-ISO-038", "section": "People", "control_area": "Awareness & Training",
         "question": "Is security awareness training conducted at onboarding and annually, with attendance records maintained?"},
        {"id": "GAP-ISO-039", "section": "People", "control_area": "Disciplinary Process",
         "question": "Is there a formal disciplinary process for information security violations, documented and communicated to staff?"},
        {"id": "GAP-ISO-040", "section": "People", "control_area": "Post-Employment Obligations",
         "question": "Are post-employment information security obligations (data return, NDA continuation) documented and enforced?"},
        {"id": "GAP-ISO-041", "section": "People", "control_area": "Confidentiality Agreements",
         "question": "Are NDAs signed by all employees and third parties before access is granted?"},
        {"id": "GAP-ISO-042", "section": "People", "control_area": "Remote Working",
         "question": "Are information security controls for remote working formally defined and enforced (VPN, encrypted devices)?"},
        {"id": "GAP-ISO-043", "section": "People", "control_area": "Incident Reporting",
         "question": "Are all staff aware of how to report information security events, with a documented and tested reporting channel?"},

        # ── Physical Security ─────────────────────────────────────────────────
        {"id": "GAP-ISO-044", "section": "Physical Security", "control_area": "Physical Security Perimeters",
         "question": "Are all physical security perimeters (data rooms, server rooms) formally defined and protected?"},
        {"id": "GAP-ISO-045", "section": "Physical Security", "control_area": "Physical Entry Controls",
         "question": "Is there a current, maintained register of all personnel authorized to access controlled areas?"},
        {"id": "GAP-ISO-046", "section": "Physical Security", "control_area": "Securing Offices & Rooms",
         "question": "Are sensitive areas (server room, HR, Finance) protected with additional physical access restrictions?"},
        {"id": "GAP-ISO-047", "section": "Physical Security", "control_area": "Physical Security Monitoring",
         "question": "Is CCTV operational with recordings retained for a defined period and access to footage controlled?"},
        {"id": "GAP-ISO-048", "section": "Physical Security", "control_area": "Environmental Threats",
         "question": "Are environmental controls (UPS, fire suppression, temperature monitoring) in place for the IT server room?"},
        {"id": "GAP-ISO-049", "section": "Physical Security", "control_area": "Working in Secure Areas",
         "question": "Are controls in place to prevent unauthorized photography or removal of equipment from secure areas?"},
        {"id": "GAP-ISO-050", "section": "Physical Security", "control_area": "Clear Desk & Screen Policy",
         "question": "Is a clear desk and clear screen policy defined, communicated, and enforced (auto-lock configured)?"},
        {"id": "GAP-ISO-051", "section": "Physical Security", "control_area": "Equipment Siting",
         "question": "Is critical IT equipment positioned to minimize risk from environmental hazards and unauthorized access?"},
        {"id": "GAP-ISO-052", "section": "Physical Security", "control_area": "Assets Off-Premises",
         "question": "Are controls defined for devices taken off-premises (encryption, remote wipe, tracking)?"},
        {"id": "GAP-ISO-053", "section": "Physical Security", "control_area": "Storage Media",
         "question": "Is there a documented process for secure handling, storage, and disposal of removable media?"},
        {"id": "GAP-ISO-054", "section": "Physical Security", "control_area": "Supporting Utilities",
         "question": "Are power and communications utilities (UPS, generators, redundant ISPs) documented and tested?"},
        {"id": "GAP-ISO-055", "section": "Physical Security", "control_area": "Cabling Security",
         "question": "Is network cabling secured against unauthorized interception, damage, or tampering?"},

        # ── Technology ────────────────────────────────────────────────────────
        {"id": "GAP-ISO-056", "section": "Technology", "control_area": "User Endpoint Devices",
         "question": "Is there an acceptable use policy for endpoints with MDM enforcing security baselines?"},
        {"id": "GAP-ISO-057", "section": "Technology", "control_area": "Privileged Access Rights",
         "question": "Are privileged accounts inventoried, periodically reviewed, and usage logged and monitored?"},
        {"id": "GAP-ISO-058", "section": "Technology", "control_area": "Information Access Restriction",
         "question": "Is access restricted by role with least privilege enforced and a formal access control matrix in place?"},
        {"id": "GAP-ISO-059", "section": "Technology", "control_area": "Secure Authentication (MFA)",
         "question": "Is MFA enforced for all remote access and critical system access?"},
        {"id": "GAP-ISO-060", "section": "Technology", "control_area": "Capacity Management",
         "question": "Are capacity and performance of critical systems monitored with defined thresholds and alerts?"},
        {"id": "GAP-ISO-061", "section": "Technology", "control_area": "Protection Against Malware",
         "question": "Is endpoint protection deployed on all in-scope devices with policies enforced and definitions kept up to date?"},
        {"id": "GAP-ISO-062", "section": "Technology", "control_area": "Technical Vulnerability Management",
         "question": "Is vulnerability scanning conducted regularly, with findings risk-ranked and remediated within defined SLAs?"},
        {"id": "GAP-ISO-063", "section": "Technology", "control_area": "Configuration Management",
         "question": "Are secure configuration baselines (CIS or equivalent) defined, documented, and enforced for all system types?"},
        {"id": "GAP-ISO-064", "section": "Technology", "control_area": "Information Deletion",
         "question": "Are processes in place to securely delete data when no longer required, including from cloud storage and backups?"},
        {"id": "GAP-ISO-065", "section": "Technology", "control_area": "Data Leakage Prevention",
         "question": "Are DLP controls implemented to detect and prevent unauthorized exfiltration of sensitive data?"},
        {"id": "GAP-ISO-066", "section": "Technology", "control_area": "Information Backup",
         "question": "Are backups taken regularly, stored securely off-site or in the cloud, and tested at least annually?"},
        {"id": "GAP-ISO-067", "section": "Technology", "control_area": "Logging",
         "question": "Are security event logs enabled on all in-scope systems with defined retention periods and centralized collection?"},
        {"id": "GAP-ISO-068", "section": "Technology", "control_area": "Monitoring Activities",
         "question": "Are logs actively monitored for anomalies with automated alerting and defined escalation paths?"},
        {"id": "GAP-ISO-069", "section": "Technology", "control_area": "Clock Synchronization",
         "question": "Are all system clocks synchronized to a single authoritative NTP source?"},
        {"id": "GAP-ISO-070", "section": "Technology", "control_area": "Software Installation Controls",
         "question": "Is software installation restricted to approved applications only via technical enforcement?"},
        {"id": "GAP-ISO-071", "section": "Technology", "control_area": "Network Security Controls",
         "question": "Are network security controls (firewalls, IDS/IPS, segmentation) formally documented and reviewed annually?"},
        {"id": "GAP-ISO-072", "section": "Technology", "control_area": "Segregation of Networks",
         "question": "Is network segmentation implemented to isolate sensitive systems, guest networks, and operational networks?"},
        {"id": "GAP-ISO-073", "section": "Technology", "control_area": "Web Filtering",
         "question": "Is web content filtering implemented to block malicious or unauthorized websites?"},
        {"id": "GAP-ISO-074", "section": "Technology", "control_area": "Cryptography",
         "question": "Is a cryptography policy in place governing approved algorithms, key lengths, and key management?"},
        {"id": "GAP-ISO-075", "section": "Technology", "control_area": "Secure Development Lifecycle",
         "question": "Does the organisation conduct in-house software development? If yes, is a formal Secure Development Lifecycle process in place? If not applicable, has this been formally excluded in the Statement of Applicability with justification?"},
        {"id": "GAP-ISO-076", "section": "Technology", "control_area": "Secure System Architecture",
         "question": "Is there a documented secure architecture or network diagram reflecting the current topology?"},
        {"id": "GAP-ISO-077", "section": "Technology", "control_area": "Change Management",
         "question": "Is there a formal change management process with cybersecurity review gates and rollback procedures?"},

        # ── Supplier Management ───────────────────────────────────────────────
        {"id": "GAP-ISO-078", "section": "Supplier Management", "control_area": "Supplier IS Policy",
         "question": "Is there a documented policy for managing information security risks in supplier relationships?"},
        {"id": "GAP-ISO-079", "section": "Supplier Management", "control_area": "Supplier Agreements",
         "question": "Do all supplier contracts include mandatory information security, data protection, and incident notification clauses?"},
        {"id": "GAP-ISO-080", "section": "Supplier Management", "control_area": "ICT Supply Chain",
         "question": "Are ICT supply chain risks (hardware/software provenance) assessed during procurement?"},
        {"id": "GAP-ISO-081", "section": "Supplier Management", "control_area": "Monitoring Supplier Services",
         "question": "Are supplier security commitments reviewed annually, including third-party security reports or certifications?"},
        {"id": "GAP-ISO-082", "section": "Supplier Management", "control_area": "Cloud Services Security",
         "question": "Are cloud providers assessed for security controls before and during engagement?"},

        # ── Incident Management ───────────────────────────────────────────────
        {"id": "GAP-ISO-083", "section": "Incident Management", "control_area": "Incident Response Planning",
         "question": "Is there a documented incident response plan covering all phases: detect, triage, contain, eradicate, recover, and lessons learned?"},
        {"id": "GAP-ISO-084", "section": "Incident Management", "control_area": "Assessment of Events",
         "question": "Is there a defined process to classify security events into incidents with severity criteria documented?"},
        {"id": "GAP-ISO-085", "section": "Incident Management", "control_area": "Response to Incidents",
         "question": "Are incident response activities tracked in a ticketing or SIEM system with evidence retained?"},
        {"id": "GAP-ISO-086", "section": "Incident Management", "control_area": "Learning from Incidents",
         "question": "Are post-incident reviews formally conducted for high and critical incidents with findings fed back into controls?"},
        {"id": "GAP-ISO-087", "section": "Incident Management", "control_area": "Evidence Collection",
         "question": "Is there a documented digital forensics and evidence preservation procedure for legal investigations?"},

        # ── Business Continuity ───────────────────────────────────────────────
        {"id": "GAP-ISO-088", "section": "Business Continuity", "control_area": "IS During Disruption",
         "question": "Does the BCP/DRP explicitly address how information security controls are maintained during a disruption or disaster?"},
        {"id": "GAP-ISO-089", "section": "Business Continuity", "control_area": "ICT Readiness for BC",
         "question": "Have ICT continuity plans been tested within the last 12 months with documented results and improvement actions?"},
    ],

    "SOC 2": [],  # Coming Soon
}
