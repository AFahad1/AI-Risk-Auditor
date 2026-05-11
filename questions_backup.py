QUESTIONS = {
    "ISO 27001": [
        {
            "id": "ISO-A5.1",
            "control": "A.5.1 — Policies for Information Security",
            "question": "Do you have a documented, management-approved information security policy that is communicated to all staff?"
        },
        {
            "id": "ISO-A5.2",
            "control": "A.5.2 — Information Security Roles and Responsibilities",
            "question": "Are information security roles and responsibilities formally defined and assigned across the organisation?"
        },
        {
            "id": "ISO-A6.1",
            "control": "A.6.1 — Screening",
            "question": "Do you conduct background verification checks on all candidates before employment, proportional to their role and data access?"
        },
        {
            "id": "ISO-A6.3",
            "control": "A.6.3 — Information Security Awareness, Education and Training",
            "question": "Do employees receive regular information security awareness training, and is completion tracked?"
        },
        {
            "id": "ISO-A7.1",
            "control": "A.7.1 — Physical Security Perimeters",
            "question": "Are physical access controls (e.g. key cards, CCTV, secure zones) in place to protect offices and data centres?"
        },
        {
            "id": "ISO-A8.1",
            "control": "A.8.1 — User Endpoint Devices",
            "question": "Are endpoint devices (laptops, mobiles) managed, encrypted, and subject to a formal acceptable use policy?"
        },
        {
            "id": "ISO-A8.2",
            "control": "A.8.2 — Privileged Access Rights",
            "question": "Is privileged access (admin accounts, root access) controlled, regularly reviewed, and granted on a need-to-know basis?"
        },
        {
            "id": "ISO-A8.5",
            "control": "A.8.5 — Secure Authentication",
            "question": "Is multi-factor authentication (MFA) enforced for access to critical systems, cloud services, and remote access?"
        },
        {
            "id": "ISO-A8.7",
            "control": "A.8.7 — Protection Against Malware",
            "question": "Is anti-malware software deployed and actively maintained across all endpoints and servers?"
        },
        {
            "id": "ISO-A8.8",
            "control": "A.8.8 — Management of Technical Vulnerabilities",
            "question": "Do you have a formal patch management process to identify and remediate vulnerabilities in a timely manner?"
        },
        {
            "id": "ISO-A8.15",
            "control": "A.8.15 — Logging",
            "question": "Are security-relevant events logged across systems, and are logs protected from tampering and reviewed regularly?"
        },
        {
            "id": "ISO-A8.24",
            "control": "A.8.24 — Use of Cryptography",
            "question": "Is sensitive data encrypted both in transit (TLS) and at rest, with encryption keys managed securely?"
        },
        {
            "id": "ISO-A5.24",
            "control": "A.5.24 — Information Security Incident Management",
            "question": "Do you have a documented incident response plan with defined roles, escalation paths, and post-incident review processes?"
        },
        {
            "id": "ISO-A5.29",
            "control": "A.5.29 — Information Security During Disruption",
            "question": "Is there a tested business continuity and disaster recovery plan that covers critical information systems?"
        },
        {
            "id": "ISO-A5.19",
            "control": "A.5.19 — Information Security in Supplier Relationships",
            "question": "Do you assess the security posture of third-party vendors and include security requirements in supplier contracts?"
        }
    ],

    "SOC 2": [
        {
            "id": "SOC2-CC1.1",
            "control": "CC1.1 — Control Environment: Security Policies",
            "question": "Do you have documented security policies that cover the Trust Service Criteria and are they communicated to staff?"
        },
        {
            "id": "SOC2-CC2.1",
            "control": "CC2.1 — Communication and Information: Risk Assessment",
            "question": "Is there a formal annual risk assessment process in place to identify and evaluate risks to your systems and data?"
        },
        {
            "id": "SOC2-CC6.1",
            "control": "CC6.1 — Logical Access Controls",
            "question": "Are logical access controls implemented so that only authorised users can access systems, with access reviews conducted regularly?"
        },
        {
            "id": "SOC2-CC6.2",
            "control": "CC6.2 — Authentication",
            "question": "Is multi-factor authentication (MFA) required for all users accessing production systems or customer data?"
        },
        {
            "id": "SOC2-CC6.6",
            "control": "CC6.6 — Network Security",
            "question": "Are network security controls (firewalls, IDS/IPS, network segmentation) in place to prevent unauthorised access?"
        },
        {
            "id": "SOC2-CC7.1",
            "control": "CC7.1 — System Monitoring",
            "question": "Do you continuously monitor systems for security events, anomalies, and threats, with alerts going to an accountable team?"
        },
        {
            "id": "SOC2-CC7.3",
            "control": "CC7.3 — Incident Response",
            "question": "Do you have a documented and tested incident response process, including notification procedures for affected customers?"
        },
        {
            "id": "SOC2-CC8.1",
            "control": "CC8.1 — Change Management",
            "question": "Is there a formal change management process requiring review, testing, and approval before changes go to production?"
        },
        {
            "id": "SOC2-A1.1",
            "control": "A1.1 — Availability: Capacity Management",
            "question": "Do you monitor system capacity and performance to ensure availability commitments and SLAs are met?"
        },
        {
            "id": "SOC2-A1.2",
            "control": "A1.2 — Availability: Recovery",
            "question": "Is there a tested disaster recovery plan ensuring systems can be restored within defined recovery time objectives (RTOs)?"
        },
        {
            "id": "SOC2-PI1.1",
            "control": "PI1.1 — Processing Integrity",
            "question": "Are controls in place to ensure data is processed completely, accurately, and in a timely manner, with errors detected and corrected?"
        },
        {
            "id": "SOC2-C1.1",
            "control": "C1.1 — Confidentiality",
            "question": "Is confidential customer and business data identified, classified, and protected with appropriate technical controls such as encryption?"
        },
        {
            "id": "SOC2-P1.1",
            "control": "P1.1 — Privacy: Notice and Consent",
            "question": "Do you have a privacy policy, and do you obtain and manage user consent for the collection and use of personal data?"
        },
        {
            "id": "SOC2-CC9.2",
            "control": "CC9.2 — Vendor Management",
            "question": "Do you maintain a vendor management programme that assesses and monitors the security of third-party service providers?"
        }
    ],

    "HIPAA": [
        {
            "id": "HIPAA-164.308(a)(1)",
            "control": "§164.308(a)(1) — Risk Analysis",
            "question": "Have you conducted a formal, documented risk analysis to identify all threats and vulnerabilities to electronic Protected Health Information (ePHI)?"
        },
        {
            "id": "HIPAA-164.308(a)(2)",
            "control": "§164.308(a)(2) — Assigned Security Responsibility",
            "question": "Have you formally appointed a HIPAA Security Officer responsible for developing and implementing security policies?"
        },
        {
            "id": "HIPAA-164.308(a)(3)",
            "control": "§164.308(a)(3) — Workforce Security",
            "question": "Are procedures in place to ensure that workforce members have access to ePHI only as needed for their job functions?"
        },
        {
            "id": "HIPAA-164.308(a)(5)",
            "control": "§164.308(a)(5) — Security Awareness Training",
            "question": "Does your organisation provide HIPAA security awareness training to all workforce members, with records of completion maintained?"
        },
        {
            "id": "HIPAA-164.308(a)(6)",
            "control": "§164.308(a)(6) — Security Incident Procedures",
            "question": "Do you have documented procedures for identifying, responding to, and reporting security incidents involving ePHI?"
        },
        {
            "id": "HIPAA-164.308(a)(7)",
            "control": "§164.308(a)(7) — Contingency Plan",
            "question": "Is there a contingency plan (backup, disaster recovery) to ensure continued access to ePHI during emergencies?"
        },
        {
            "id": "HIPAA-164.310(a)(1)",
            "control": "§164.310(a)(1) — Facility Access Controls",
            "question": "Are physical access controls in place to limit access to facilities where ePHI systems are housed to authorised personnel only?"
        },
        {
            "id": "HIPAA-164.310(d)(1)",
            "control": "§164.310(d)(1) — Device and Media Controls",
            "question": "Do you have procedures for the disposal and re-use of hardware and media that contain ePHI, including secure wiping and tracking?"
        },
        {
            "id": "HIPAA-164.312(a)(1)",
            "control": "§164.312(a)(1) — Access Control",
            "question": "Are technical access controls implemented so that only authorised users can access ePHI, using unique user IDs and automatic logoff?"
        },
        {
            "id": "HIPAA-164.312(b)",
            "control": "§164.312(b) — Audit Controls",
            "question": "Do you have audit controls that record and examine activity on systems containing ePHI, with logs reviewed regularly?"
        },
        {
            "id": "HIPAA-164.312(c)(1)",
            "control": "§164.312(c)(1) — Integrity Controls",
            "question": "Are controls in place to ensure ePHI is not improperly altered or destroyed, including error-checking and integrity verification mechanisms?"
        },
        {
            "id": "HIPAA-164.312(e)(1)",
            "control": "§164.312(e)(1) — Transmission Security",
            "question": "Is ePHI encrypted when transmitted over electronic networks, using strong encryption standards (e.g. TLS 1.2+)?"
        },
        {
            "id": "HIPAA-164.308(b)(1)",
            "control": "§164.308(b)(1) — Business Associate Agreements",
            "question": "Do you have signed Business Associate Agreements (BAAs) in place with all vendors and partners who access or process ePHI?"
        },
        {
            "id": "HIPAA-164.404",
            "control": "§164.404 — Breach Notification",
            "question": "Do you have a documented breach notification procedure covering assessment, reporting timelines (60 days), and notification to HHS and affected individuals?"
        }
    ]
}
