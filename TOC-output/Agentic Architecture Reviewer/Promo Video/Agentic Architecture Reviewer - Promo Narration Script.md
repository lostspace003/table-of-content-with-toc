# Agentic Architecture Reviewer - promo narration

Voice: neural TTS (en-US-AndrewNeural). Duration: 5.1 min.

**[hook]** The diagram said encrypted. The implementation said otherwise. And the architecture review happened six months earlier.

**[hook]** What if every architecture got a threat model that shows its evidence, asks the questions it cannot answer, and never labels a guess as a finding? That is what you build here.

**[intro]** Gennoor Tech presents the Agentic Architecture Reviewer.

**[story]** From diagram to threat register. Six STRIDE categories applied to every flow, but only to components that really exist in the model. Every edge carries its source. Every threat carries its assumptions and a validation question. Every finding separates what was observed from what was assumed.

**[path0]** Day one is the model. You start with constrained inputs, Mermaid flowcharts, a simple JSON architecture schema and Markdown decision records, and you report what could not be parsed instead of pretending. You build a typed system graph with components, data stores, identities, external systems, protocols, data classifications and trust boundaries, and you extract security requirements as explicit statements with I Ds and verification status.

**[path1]** Day two is the threat model. The agent proposes STRIDE candidates. Your code accepts only those that link to a modeled component or flow, and you watch it reject a plausible-sounding threat about a service that is not in the design. Review rules then check authentication, authorization boundaries, secrets handling, logging, encryption, data minimization and failure handling.

**[path2]** Findings are evidence-graded. Observed design facts, assumptions, missing information and recommended questions stay separate, and an unverified concern is never called a confirmed vulnerability. On day three architects accept, reject, defer or ask for more evidence, with rationale and an owner, and the tool tracks changes across design revisions.

**[path3]** Then the cross-check. You compare modeled requirements with Terraform, Kubernetes and repository evidence, and report coverage and gaps, never full proof of conformance. Finally you evaluate against secure and intentionally flawed reference architectures: threat coverage, unsupported claims, evidence linkage and usefulness.

**[labs]** Labs use two reference architectures, one secure and one deliberately flawed, so you can measure what the reviewer finds, what it misses and what it should have asked.

**[mods]** Here is the full table of contents, 9 modules over three days. Day one: Architecture inputs and a constrained format; The system graph with provenance; and Requirements extraction. Day two: Method-driven threat generation; Architecture review rules; and Evidence-graded findings. Day three: Architect review and decision records; Design-to-implementation comparison; and Evaluation and capstone.

**[princ]** Every build in this course follows six engineering principles. Model output is a proposal, never a fact. Authorization lives outside the model. A human approves every consequential action. Decisions and evidence are logged. The stack stays provider-agnostic. And quality is measured, not assumed.

**[stats]** Three days, hands-on. Six STRIDE categories. Two reference designs. One hundred percent of findings linked to evidence.

**[who]** This course is for security architects, solution architects, application security, platform architects and engineering leads. You need system design fundamentals, basic networking and identity, threat modeling and Python or A P I familiarity.

**[cta]** Review the architecture, not the slide. The Agentic Architecture Reviewer. Enrol now at gennoor dot com.