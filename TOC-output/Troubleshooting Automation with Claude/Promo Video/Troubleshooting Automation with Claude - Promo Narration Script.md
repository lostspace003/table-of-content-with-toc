# Troubleshooting Automation with Claude - promo narration

Voice: neural TTS (en-US-AndrewNeural). Duration: 6.1 min.

**[hook]** An incident lands in ServiceNow at nine at night. The acknowledgement mail goes out, and then the questions begin. Which V I P? Since when? What changed? Who is looking at it? And the engineer on call is typing the same first five commands they typed last week.

**[hook]** What if an agent read the ticket, asked for the missing details, pulled the evidence from the load balancer, and suggested the exact C L I commands to run next? Troubleshooting, automated, with a person still in charge of every change.

**[intro]** Gennoor Tech presents Troubleshooting Automation with Claude.

**[story]** One incident in. One resolution note out. You build the troubleshooting workflow in ten modules, and every module ends with something that actually runs. Claude reads, plans and explains. Deterministic Python collects the evidence and updates the ticket. A person approves anything that touches a device. And every step is logged, in your audit trail and in the ServiceNow work notes.

**[path0]** You start with the incident lifecycle in ServiceNow, from the moment the ticket is created to the acknowledgement mail and the first troubleshooting reply. You map where an agent may act and where it may not. Then you set up Claude Code, the Claude Agent S D K and M C P servers for this exact workflow, with a read only ServiceNow tool, a read only device tool, and nothing else. Credentials stay in the vault, never in a prompt.

**[path0]** Then intake. You pull the incident through the ServiceNow Table A P I, validate it, and let Claude compare it against a primary troubleshooting checklist. Affected V I P, symptom, start time, scope, last change. The agent lists what is missing and drafts the clarification mail. An engineer reviews it and sends it.

**[path1]** Day two is evidence and diagnosis. Deterministic collectors run F5 t m s h and iControl REST, the NetScaler NITRO A P I, Radware Alteon and other load balancers, and the Cisco A P I C REST interface, and return typed facts with a device, a timestamp and the raw output. Claude turns those facts into a ranked list of likely causes, and for each cause the exact C L I command that confirms or rules it out. Structured J S O N, with a citation for every claim, never free text.

**[path2]** Then the guardrails. Every suggested command is classified read only or state changing. Read only commands can run in the lab automatically. Anything else waits for an engineer to approve, and the approval, the command and the output are written to the audit log and to the ServiceNow work notes. You will try to push a change through without approval, and you will watch it refuse. Then you run the full loop. Suggest, approve, execute, interpret, until the cause is confirmed or a senior engineer is paged.

**[path3]** Day three is the template. Reason, action, next action. Claude drafts it from the evidence it was given, cites the command output behind every line, and marks what it could not verify. You post it to the incident through the Table A P I, with the close code, and you create the knowledge article the next incident will reuse.

**[path3]** You finish by wiring it all into a troubleshooting page. A FastAPI service with the incident queue, the evidence, the suggested steps, the approve and reject buttons and the audit tab. Tested with pytest against recorded device output, and shipped through a reviewed GitHub pull request with Actions green.

**[labs]** Every lab runs against a ServiceNow developer instance, lab load balancers and a Cisco A C I sandbox, with synthetic incidents that have real symptoms. You will watch the agent ask the right question, run the right command, and refuse the wrong one. And in the capstone a fresh incident lands and your team takes it from acknowledgement to posted resolution note.

**[mods]** Here is the full table of contents, 10 modules over three days. Day one: The troubleshooting workflow and the ServiceNow incident lifecycle; Setting up Claude Code, the Agent SDK and MCP for incident triage; and Incident intake through the Table API and the acknowledgement mail. Day two: Evidence collection from load balancers and ACI; Claude suggests troubleshooting steps as structured JSON; Guardrails, approvals and audit for incident automation; and Running approved steps and reading the result. Day three: The reason, action and next action template; The troubleshooting page: service, tests and delivery; and Capstone: incident to resolution note, end to end.

**[princ]** Every build in this course follows six engineering principles. Model output is a proposal, never a fact. Authorization lives outside the model. A human approves every consequential action. Decisions and evidence are logged. The stack stays provider-agnostic. And quality is measured, not assumed.

**[stats]** Ten modules that run. Three days, hands on. Four device platforms. And zero device changes without a person saying yes.

**[who]** This course is for network operations, load balancer and data centre engineers, N O C and service desk teams, and I T automation leads in India and worldwide. You need basic networking, comfort with a C L I, and some Python. Familiarity with ServiceNow incidents helps, but it is not required.

**[cta]** Turn every incident into a documented, repeatable fix. Troubleshooting Automation with Claude. Enrol now at gennoor dot com.