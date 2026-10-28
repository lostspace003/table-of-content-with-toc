# HR Hiring Flow Automation with Claude - promo narration

Voice: neural TTS (en-US-AndrewNeural). Duration: 6.2 min.

**[hook]** Three hundred applications land in the job portal overnight. Your recruiters have two days, one phone each, and a hiring manager who wants a shortlist by Friday. Every profile has to be filtered, downloaded, called, judged and pitched, and every one of those steps is done by hand.

**[hook]** What if an agent filtered the portal, downloaded the profiles, prepared every screening call, scored English proficiency, experience, location, salary ask and working hours against the role, and drafted the pitch, while a person made every decision that matters? That is hiring flow automation, done with Claude, done safely.

**[intro]** Gennoor Tech presents HR Hiring Flow Automation with Claude.

**[story]** One job requisition in. One approved, documented shortlist out. You build the hiring pipeline in ten modules across three days, and every module is something you can test, review and demonstrate. Claude plans, drafts and explains. Deterministic Python code executes. A recruiter approves every outreach and every pitch. And everything is logged.

**[path0]** You begin by mapping the real hiring flow, from the job portal of your choice to the onboarding ticket, and by deciding which steps a model may propose and which only a person may approve. Then you set up Claude Code with a project file that encodes hiring policy, the Claude Agent S D K in Python, and a Model Context Protocol server that exposes your portal exports and candidate store as tools with strict J S O N outputs.

**[path0]** Next comes sourcing. You filter and download candidate data from portal exports and sanctioned portal A P I endpoints, validate every row with Pydantic, deduplicate across portals, and record where every record came from. A typed candidate profile captures experience, location, salary ask and preferred working hours, extracted from resumes with a confidence per field. Unknowns are marked, never guessed.

**[path1]** On day two you reach the candidate. Claude drafts a call script from the role and the profile, and a deterministic scheduler books a slot in the candidate's preferred hours and places the call through Twilio Programmable Voice, with recorded consent and a transcript stored against the record. The script is a proposal. The recruiter runs the call, and nothing dials until they say yes.

**[path2]** Then assessment. A rubric-driven agent scores English proficiency from the transcript on C E F R aligned bands, checks experience, location, working hours and salary ask against the requisition, and cites the exact lines that justify each score. Low confidence routes to a human. A pitch generator then drafts a personalised pitch within approved talking points and the approved salary band. Ask it to promise a number outside the band and it refuses. And nothing is sent until the recruiter approves it.

**[path3]** Day three is control. You build the guardrails specific to hiring: P I I minimisation, consent and retention tracking, prompt injection defences for untrusted resume and transcript text, fairness checks on score distributions, and an append-only audit log in PostgreSQL. Every shortlist, every outreach and every pitch passes through an approval gate with a named approver, and every override is recorded.

**[path3]** Finally orchestration. The pipeline runs as a FastAPI service with pytest coverage. Every prompt, rubric and schema change goes through a GitHub pull request, and GitHub Actions runs the evaluation set before it merges. When a candidate accepts, a ServiceNow record is opened through the Table A P I so onboarding and access requests start the same day.

**[labs]** Every lab uses synthetic candidates, synthetic portal exports and a sandbox telephony number. You will watch a resume try to inject instructions into the scorer and fail. You will see the gate block a pitch that quotes the wrong salary. And you will trace one candidate from portal row to onboarding ticket, event by event, in the audit log.

**[mods]** Here is the full table of contents, 10 modules over three days. Day one: The hiring flow and the automation baseline; Setting up Claude Code, the Agent SDK and MCP for hiring; Sourcing: filtering and downloading from the portal of choice; and Candidate profile schema and resume extraction. Day two: Calling candidates: scripts, scheduling and consented recording; Assessing English proficiency, experience, location, salary ask and hours; and Pitching the role: drafts within approved talking points. Day three: Guardrails, approvals and audit for hiring automation; Orchestration, ServiceNow handoff and CI; and Capstone: requisition to approved shortlist.

**[princ]** Every build in this course follows six engineering principles. Model output is a proposal, never a fact. Authorization lives outside the model. A human approves every consequential action. Decisions and evidence are logged. The stack stays provider-agnostic. And quality is measured, not assumed.

**[stats]** Ten course modules. Three days, hands-on. Five fit criteria scored with cited evidence. And zero candidates contacted without a recruiter's approval.

**[who]** This course is for H R operations and talent acquisition teams, H R technology and enterprise I T automation engineers, and the network and platform teams asked to build and host these workflows, in India and worldwide. You need basic Python, a working knowledge of your hiring process, and nothing more. No prior agent experience is required.

**[cta]** Hire faster without handing the decision to a machine. HR Hiring Flow Automation with Claude. Enrol now at gennoor dot com.