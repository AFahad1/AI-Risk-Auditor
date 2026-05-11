QUESTIONS = {
    "SOC 2": [
        {
            "id": "DVL001",
            "question": "Are there adequate controls in place to prevent unauthorized logical access to internal networks?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 3
        },
        {
            "id": "DVL002",
            "question": "Are adequate measures in place to control access to critical internal IT infrastructure and production servers?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 2
        },
        {
            "id": "DVL003",
            "question": "Are there policies restricting the usage of external storage devices, and are they effectively enforced?",
            "loss_of_cia": "C,I,A",
            "likelihood": 4,
            "impact": 5
        },
        {
            "id": "DVL004",
            "question": "Are there measures to prevent unauthorized access to colleagues' laptops or other devices? (what kind of authentication are the laptops having?)",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL006",
            "question": "Are identity and access management (IAM) policies (or any services you are using) in place to ensure strong authentication mechanisms for all users?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 4
        },
        {
            "id": "DVL007",
            "question": "Are controls in place to prevent unauthorized logical access to emails and internal networks?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 4
        },
        {
            "id": "DVL008",
            "question": "Are all critical network components configured to use multi-factor authentication (MFA)?",
            "loss_of_cia": "I,A",
            "likelihood": 3,
            "impact": 5
        },
        {
            "id": "DVL009",
            "question": "Are there policies to ensure that all company assets, such as laptops, are returned upon employee exit?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 4
        },
        {
            "id": "DVL010",
            "question": "Are software applications and systems regularly updated to mitigate potential vulnerabilities?",
            "loss_of_cia": "C,I,A",
            "likelihood": 5,
            "impact": 4
        },
        {
            "id": "DVL011",
            "question": "Is there a process to prevent the installation of pirated or unauthorized software on company systems?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL012",
            "question": "Is there a patch management process in place to ensure Linux servers are regularly updated?",
            "loss_of_cia": "C,I,A",
            "likelihood": 4,
            "impact": 5
        },
        {
            "id": "DVL013",
            "question": "Are known system vulnerabilities being actively identified, managed, and patched?",
            "loss_of_cia": "C,I",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL014",
            "question": "Are APIs properly configured and secured to prevent unauthorized access or data breaches?",
            "loss_of_cia": "C,I,A",
            "likelihood": 3,
            "impact": 3
        },
        {
            "id": "DVL015",
            "question": "Are measures in place to protect the organization against malware attacks, and is monitoring in place?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL016",
            "question": "Are there controls to prevent users from removing antivirus software from their systems?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL017",
            "question": "Are adequate logging and monitoring processes in place to ensure security incidents are identified and addressed promptly?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL018",
            "question": "Are databases encrypted to protect sensitive data from unauthorized access?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL019",
            "question": "Are company laptops equipped with full disk encryption to protect data in case of theft or loss?",
            "loss_of_cia": "I,A",
            "likelihood": 4,
            "impact": 5
        },
        {
            "id": "DVL020",
            "question": "Are encryption and access control measures in place to prevent data breaches involving sensitive business information?",
            "loss_of_cia": "I,A",
            "likelihood": 4,
            "impact": 5
        },
        {
            "id": "DVL021",
            "question": "Is there a secure process for disposing of hardware containing sensitive data?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL022",
            "question": "Are secure methods in place for the electronic transfer of sensitive information?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL023",
            "question": "Are controls in place to prevent data loss during migrations, deletions, or storage failures?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL024",
            "question": "Are physical access controls in place to prevent unauthorized access to the premises?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL026",
            "question": "Are FTP and HTTP services properly secured or disabled on the firewall to prevent unauthorized access?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL027",
            "question": "Are there redundancies in place to mitigate the risk of a primary cloud failure?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 4
        },
        {
            "id": "DVL028",
            "question": "Are network devices monitored, and are backups available to prevent operational downtime in case of failure?",
            "loss_of_cia": "I,A",
            "likelihood": 3,
            "impact": 5
        },
        {
            "id": "DVL029",
            "question": "Is there a contingency plan in place for internet service disruptions at the supplier's end?",
            "loss_of_cia": "I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL031",
            "question": "Are employees regularly trained on information security policies and requirements to ensure compliance?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL032",
            "question": "Are systems in place to ensure high resource utilization does not prevent customer access to production servers?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL034",
            "question": "Does the organization have a business continuity plan for events such as riots, pandemics, or natural disasters?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL036",
            "question": "Is there a risk of becoming dependent on a single cloud security provider or platform (vendor lock-in)?",
            "loss_of_cia": "C,I,A",
            "likelihood": 2,
            "impact": 5
        },
        {
            "id": "DVL038",
            "question": "Are systems protected from Denial of Service (DoS) attacks, and are robust mechanisms in place to prevent such incidents?",
            "loss_of_cia": "I,A",
            "likelihood": 1,
            "impact": 5
        },
    ]
}

# ISO 27001 uses the same questionnaire as SOC 2
QUESTIONS["ISO 27001"] = QUESTIONS["SOC 2"]
