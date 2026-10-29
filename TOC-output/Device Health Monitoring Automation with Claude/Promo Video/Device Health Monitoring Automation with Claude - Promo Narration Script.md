# Device Health Monitoring Automation with Claude - promo narration

Voice: the presenter's own cloned voice. Duration: 6.3 min.

**[hook]** Forty devices. One morning check. And someone still logs in to every box to ask if it is healthy.

**[hook]** What if an agent checked every V I P, every H A pair, every sync state and every version, worked out what changed, and raised the right ServiceNow ticket before your first coffee? That is device health monitoring, done with Claude, done safely.

**[intro]** Gennoor Tech presents Device Health Monitoring Automation with Claude.

**[story]** Six signals in. One verdict out. You build the platform in eleven increments, and every increment is something you can test, review and demonstrate. Claude plans the code and explains the evidence. Deterministic Python does the collecting. A person approves anything that matters. And everything is logged.

**[path0]** You start by defining what healthy actually means. V I P status, uptime, H A status, sync status when a pair is in H A, software version, and the last change performed on the device. You map each signal to F5, NetScaler, Radware, other load balancers, and Cisco A C I. Then you set up Claude Code, the Agent S D K and an M C P server that exposes read-only device tools, with credentials kept well outside the model.

**[path0]** Then the collectors. F5 iControl REST and t m s h for virtual server stats, failover state and sync status. The NetScaler NITRO A P I for load balancing virtual servers, H A nodes and version. Radware Alteon through Cyber Controller, a generic adapter for other load balancers, and the Cisco A P I C REST A P I for fabric nodes, firmware and health. Every reading lands in one shared schema, and a missing signal is marked unknown, never assumed healthy.

**[path1]** On day two you answer the question every N O C asks first. What changed? You pull audit logs from the devices, configuration snapshots from Git, and change requests from ServiceNow, and build a timeline for every device. Then Claude becomes the triage analyst. It receives the evidence bundle and returns a structured verdict: severity, affected signals, cited readings, likely cause and recommended action. No citation, no conclusion. And the severity rules live in code, so a sync failure in an H A pair is never quietly downgraded.

**[path2]** Next, the ticket. Through the ServiceNow Table A P I the pipeline looks up the open incident by correlation I D, decides whether to update it, reopen it or create a new one, and never creates a duplicate. Flow Designer handles assignment and notification. Then the guardrails. The M C P server has no write tools for devices. Priority one and priority two tickets wait for a person. Every run writes its readings, prompt, verdict, ticket action and approver to an audit log, and a flapping device cannot flood your queue.

**[path3]** Day three is operations. The pipeline ships through a GitHub pull request, runs from GitHub Actions on a schedule using a runner that can reach the devices, and respects declared maintenance windows so a planned upgrade never becomes a false incident.

**[path3]** You add pytest suites for the collectors, the severity rules and the ticket logic, export readings to Prometheus, and put a Grafana fleet dashboard beside the ticket flow. Then you write the runbook for the days when a collector fails, a verdict is wrong, or ServiceNow itself is down. And you measure the outcome: time to ticket, duplicate rate and false positives, so the platform proves its own value.

**[labs]** Every lab runs against a lab fleet of F5, NetScaler, Radware and A C I devices with synthetic faults. Nothing touches production. You will break sync on purpose, upgrade one side of a pair, pull a collector out from under the agent, and watch the pipeline explain exactly what happened.

**[mods]** Here is the full table of contents, 11 modules over three days. Day one: What device health means across the fleet; Setting up Claude Code, the Agent SDK and MCP for this workflow; Collecting health from F5 and NetScaler; and Collecting health from Radware, other load balancers (Anaya LB) and Cisco ACI. Day two: Last change performed: correlating config history and change records; Claude as the triage analyst: structured health verdicts; Creating or updating ServiceNow tickets; and Guardrails, approvals and audit for health monitoring. Day three: Scheduling and running the workflow with GitHub Actions; Testing, dashboards and operations; and Capstone: end-to-end device health monitoring for a mixed fleet.

**[princ]** Every build in this course follows six engineering principles. Model output is a proposal, never a fact. Authorization lives outside the model. A human approves every consequential action. Decisions and evidence are logged. The stack stays provider-agnostic. And quality is measured, not assumed.

**[stats]** Eleven build steps. Three days, hands-on. Five device platforms covered. And zero duplicate tickets.

**[who]** This course is for network operations and load balancer engineers, N O C leads, data centre teams, and I T S M and automation teams in India and worldwide. You need working knowledge of load balancers, basic REST and JSON, and basic Python and Git.

**[cta]** Let the fleet report its own health, and let the ticket write itself. Device Health Monitoring Automation with Claude. Enrol now at gennoor dot com.