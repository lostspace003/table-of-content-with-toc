# Cisco ACI Upgrade Automation with Claude - promo narration

Voice: neural TTS (en-US-AndrewNeural). Duration: 6.0 min.

**[hook]** An A C I fabric upgrade is a weekend you do not get back. Two hundred switches, a cluster that must be fully fit before anything moves, and one bad group away from rebooting both v P C peers.

**[hook]** What if Claude read the validator output, drafted the upgrade plan and explained every step, while deterministic code did the work and a person approved every window? That is A C I upgrade automation, done the Cisco way.

**[intro]** Gennoor Tech presents Cisco ACI Upgrade Automation with Claude.

**[story]** One fabric in. One upgraded fabric out, with every Cisco recommended check completed and recorded. You build the workflow in ten hands-on modules, and each one is something you can run against the lab fabric, review and demonstrate. Claude plans, drafts and explains. Python and Ansible execute. A human approves the consequential actions. Everything is logged.

**[path0]** You start with the process itself, as Cisco documents it. Target release selection, the release notes and compatibility matrix, A P I C cluster first, then switch groups, and why a v P C pair must never sit in the same group. Then you set up Claude Code, the Claude Agent S D K and an M C P server that exposes read-only A P I C queries as tools.

**[path0]** Then discovery. A Python client for the A P I C R E S T A P I that logs in, pulls every node, controller, firmware version, cluster state and health score, and returns typed J S O N. You run the Cisco pre-upgrade validator and the open-source validation script, parse the results, and let Claude explain each failure in plain language, citing the exact query that produced it.

**[path1]** On day two the plan takes shape. Claude proposes upgrade groups from the inventory, keeps v P C peers apart, orders the A P I C cluster before the leaves and spines, and maps every group to a maintenance window. The output is structured J S O N, validated against a schema, so a bad plan is rejected before anyone reads it. You then stage firmware in the repository, take a configuration export and snapshot, and raise the change request in ServiceNow through the Table A P I.

**[path2]** Guardrails come next, and they are specific to this workflow. The agent can read the fabric, but it cannot trigger an upgrade. Every maintenance policy and firmware group is created by deterministic code, after a person approves the plan in a GitHub pull request. Scheduled start times are checked against the approved window, an incomplete validator run blocks the next step, and every decision, prompt and A P I call is written to an audit log you can hand to the change board.

**[path3]** Day three is execution. The runner upgrades the A P I C cluster, waits for the cluster to be fully fit, then moves through the switch groups one at a time, polling firmware status and never starting the next group until the last one is healthy. If a node does not come back, the run pauses and Claude writes the status update for the on-call engineer.

**[path3]** Then verification. Pre and post snapshots of versions, faults, endpoint counts, routes and v P C state are compared by code, and Claude turns the diff into a readable report with a clear go, hold or roll back recommendation that a person signs off.

**[labs]** Execution labs run on a small physical lab fabric with fictional hostnames, three A P I Cs, four leaves and two spines, so the cluster and switch groups really upgrade and reboot. The runner's failure paths are exercised against a mocked A P I C with recorded responses. You will fail a validator check on purpose, watch the pipeline block, fix the fault, and finish an end to end upgrade with the full evidence bundle.

**[mods]** Here is the full table of contents, 10 modules over three days. Day one: The Cisco ACI upgrade process and where upgrades go wrong; Claude Code, Agent SDK and MCP setup for the ACI workflow; Fabric discovery through the APIC REST API; and Pre-upgrade validation and explained failures. Day two: Upgrade planning with structured outputs; Firmware staging, backups and the change request; and Guardrails, approvals and audit for fabric upgrades. Day three: Executing the APIC cluster and switch group upgrades; Post-upgrade verification, reporting and rollback decisions; and Capstone: end-to-end ACI fabric upgrade with evidence bundle.

**[princ]** Every build in this course follows six engineering principles. Model output is a proposal, never a fact. Authorization lives outside the model. A human approves every consequential action. Decisions and evidence are logged. The stack stays provider-agnostic. And quality is measured, not assumed.

**[stats]** Ten hands-on modules. Three days. Six physical switches upgraded for real in the lab. And zero upgrades triggered without human approval.

**[who]** This course is for enterprise network operations, data centre and automation engineers in India and worldwide who run Cisco A C I fabrics. You need working A C I knowledge, basic Python, and familiarity with R E S T A P I calls. Experience with an A I coding assistant helps but is not required.

**[cta]** Upgrade the fabric the Cisco way, every time, with proof. Cisco ACI Upgrade Automation with Claude. Enrol now at gennoor dot com.