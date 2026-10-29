# Device Upgrade Automation with Claude - promo narration

Voice: the presenter's own cloned voice. Duration: 6.6 min.

**[hook]** It is two in the morning. The change window is open, the firmware is uploaded, the H A pair is waiting, and the box says disk full. Again. The window closes, the ticket slips a week, and nobody slept.

**[hook]** What if an agent had already cleared the space, staged the image with a verified checksum, run every pre-check, and asked you for one approval before the reboot? That is device upgrade automation, done with Claude, done safely.

**[intro]** Gennoor Tech presents Device Upgrade Automation with Claude.

**[story]** One device list in. One verified upgrade out, with evidence. You build the workflow in eleven modules, across F five, NetScaler, Radware and Cisco A C I. Claude plans, drafts and explains. Deterministic Python code executes. A person approves every space clear, install and reboot. And every call is logged.

**[path0]** You start with how vendors actually upgrade: F five boot volumes and U C S archives, NetScaler build files, Alteon image banks, A C I firmware groups, and the ways upgrades fail in production. Then you set up Claude Code, the Claude Agent S D K and M C P servers that wrap the F five iControl REST A P I, the NetScaler NITRO A P I and the Radware Alteon A P I, read only to begin with, with strict J S O N outputs for every tool.

**[path0]** Then discovery and pre-checks. You pull the inventory from the ServiceNow C M D B with the Table A P I, collect version, licence, H A role, sync state and disk usage from every device, and freeze a golden snapshot of virtual servers, pools, certificates and configuration backups. Claude reads the snapshot and explains anything that looks wrong before you touch a thing. No backup, no upgrade.

**[path1]** Day two is the work itself. Deterministic adapters clear old images, core files and stale backups from allowlisted paths, dry-run first, to make room. They upload the firmware with S H A two five six verification and install it to the inactive boot volume. Upgrades run H A aware: standby first, verify, fail over, then the former active. The agent proposes the order and the exact A P I calls as structured J S O N. The code runs the approved plan and records state after every step. Nothing is improvised.

**[path2]** Then verification. The post-check snapshot is diffed against the golden snapshot: version, virtual server status, pool members, H A sync, certificate expiry. Claude turns the diff into a structured verdict with a rollback recommendation, and the guardrail module enforces it. Allowlisted tools and devices, read only by default, a ServiceNow change request for every window, a human gate before every space clear, install and reboot, and an append-only audit log of every prompt, plan and call. You will try to talk the agent into skipping a check, and watch the runner refuse.

**[path3]** Day three adds the scheduler. Approved change windows come from ServiceNow, runs are triggered through GitHub Actions, and the runner refuses to start outside the window. Reminders go out before, progress during, and a summary after. When a window is about to overrun, the run pauses at the next safe step and asks for an extension instead of leaving a device half upgraded.

**[path3]** Then you scale to the fleet. Cisco A C I upgrades follow the process Cisco prescribes, with the pre-upgrade validator and A P I C firmware groups, controllers first, then switches in groups. Batches get canary devices, blast radius limits and stop on first failure, and the same adapter contract extends to other load balancers, Anaya L B included. The capstone runs a scheduled, approved, H A aware upgrade across a mixed fleet, end to end, and ships the evidence pack as a GitHub pull request.

**[labs]** Every lab runs against simulated and lab devices with fictional hostnames. You will fill a disk on purpose, watch the pre-check gate stop an upgrade, fail a post-check deliberately, and roll back to the previous boot volume under time pressure.

**[mods]** Here is the full table of contents, 11 modules over three days. Day one: The device upgrade lifecycle and why upgrades fail; Claude Code, Agent SDK and MCP for upgrade workflows; Inventory and pre-flight discovery; and Pre-checks and the golden snapshot. Day two: Disk space clearing and firmware staging; Upgrade execution adapters, HA-aware; Post-checks, verification and rollback; and Guardrails, approvals and audit for upgrades. Day three: Scheduler and change windows; Cisco ACI and fleet-scale, multi-vendor runs; and Capstone: scheduled, approved, HA-aware upgrade end to end.

**[princ]** Every build in this course follows six engineering principles. Model output is a proposal, never a fact. Authorization lives outside the model. A human approves every consequential action. Decisions and evidence are logged. The stack stays provider-agnostic. And quality is measured, not assumed.

**[stats]** Eleven build modules. Three days, hands-on. Four vendor families. And zero reboots without approval.

**[who]** This course is for enterprise I T and network operations teams, load balancer and data centre engineers, N O C automation leads and change managers in India and worldwide. You need basic networking, load balancer administration, a Linux shell and some Python. Experience with an A I coding assistant helps but is not required.

**[cta]** Upgrade every device the same safe way. Device Upgrade Automation with Claude. Enrol now at gennoor dot com.