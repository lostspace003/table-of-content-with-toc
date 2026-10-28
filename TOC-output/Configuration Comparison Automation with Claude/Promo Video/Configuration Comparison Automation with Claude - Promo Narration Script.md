# Configuration Comparison Automation with Claude - promo narration

Voice: neural TTS (en-US-AndrewNeural). Duration: 6.0 min.

**[hook]** A data centre load balancer is moving to the cloud. The cut-over is on Saturday. The configuration on the new platform was rebuilt by hand from a spreadsheet, and nobody can say with certainty that the two sides match.

**[hook]** What if Claude read both sides, object by object, told you exactly what differs, why it matters, and what to fix before the change window opens? That is configuration comparison, automated with Claude, and governed by people.

**[intro]** Gennoor Tech presents Configuration Comparison Automation with Claude.

**[story]** Two platforms. One verified difference report. Cloud to cloud, physical to cloud, or cloud back to physical, the problem is always the same: two configurations written in different dialects that must mean the same thing. You build the pipeline in ten modules. Claude plans, drafts and explains. Deterministic Python collects and diffs. A person approves every consequential action. And everything is logged.

**[path0]** You start with the planning discipline: what a migration comparison must prove, which objects matter, and why a raw text diff between an F five and a NetScaler is worthless. Then you set up the workbench. Claude Code for interactive work, the Claude Agent S D K for the pipeline, and M C P servers that expose read-only collectors as tools Claude can call but never bypass.

**[path0]** Day one ends with collection and normalisation. You pull running configuration from F five through iControl R E S T and t m s h, from Citrix NetScaler through the N I T R O A P I, from Radware Alteon, from other load balancers such as Anaya L B, and from Cisco A P I C and Terraform state. Every virtual server, pool, monitor, certificate and policy lands in one canonical Pydantic model, with provenance on every field and unknowns marked explicitly instead of guessed.

**[path1]** On day two Claude plans. Given the source inventory and the target platform, it drafts the migration plan as structured J S O N: object mappings, feature gaps, dependency order and risks. It must cite the inventory it was given, and it must say plainly what cannot be mapped. Each plan step carries a confidence and an owner, so the review meeting argues about facts, not formatting. You test it with incomplete and contradictory input and watch it refuse to invent a mapping.

**[path2]** Then the diff engine. Deterministic code compares canonical models field by field, classifies each difference by severity, and produces a machine-readable report. Claude never computes the diff. It reads the diff through tool use and writes the explanation, the drift summary and the remediation steps an engineer can act on, with every claim tied to a report line. You will seed a hidden persistence mismatch and watch the engine find it.

**[path3]** Day three is governance. Collectors run with read-only credentials. Every report becomes a GitHub pull request with the evidence attached, and a ServiceNow change record created through the Table A P I and routed for approval in Flow Designer. Nothing is applied to any platform without a named approver, and the approval itself is part of the audit record.

**[path3]** You then wire it into GitHub Actions: Terraform plan output compared against live state before apply, scheduled drift checks between platforms, and an audit trail that records every prompt, every tool call and every decision, so a reviewer can replay the run months later.

**[labs]** Every lab runs against lab devices and recorded A P I responses, so you can break things safely. You will compare a physical F five with a cloud NetScaler, seed a hidden persistence timeout mismatch into the target, and prove the diff engine catches it, Claude explains it, and the tests never let it slip through. Then you attempt an unapproved remediation and prove the pipeline blocks it and logs the attempt.

**[mods]** Here is the full table of contents, 10 modules over three days. Day one: Configuration comparison as a migration discipline; Setting up Claude Code, the Agent SDK and MCP for the workflow; Collecting configuration from every platform; and Normalising into a canonical configuration model. Day two: Migration planning with Claude; The deterministic diff engine; and Claude explains the differences. Day three: Guardrails, approvals and audit for configuration comparison; Scheduling, Terraform plan checks and GitHub Actions; and Capstone: end-to-end physical-to-cloud comparison.

**[princ]** Every build in this course follows six engineering principles. Model output is a proposal, never a fact. Authorization lives outside the model. A human approves every consequential action. Decisions and evidence are logged. The stack stays provider-agnostic. And quality is measured, not assumed.

**[stats]** Three migration directions. Five platform A P I families. One canonical schema for every object. And zero changes applied without approval.

**[who]** This course is for enterprise I T and network operations teams, load balancer and cloud migration engineers, and automation leads, in India and worldwide. You need basic networking, Python and command line skills. Prior use of Claude is helpful, not required.

**[cta]** Know every difference before the change window opens. Configuration Comparison Automation with Claude. Enrol now at gennoor dot com.