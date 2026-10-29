# Agentic Configuration Reviewer - promo narration

Voice: the presenter's own cloned voice. Duration: 5.1 min.

**[hook]** The S three bucket was public for eleven days. The pull request had two approvals. Nobody read line two fourteen.

**[hook]** What if every configuration change got a reviewer that never gets tired, never guesses, and always shows its evidence? In two days you build one.

**[intro]** Gennoor Tech presents the Agentic Configuration Reviewer.

**[story]** Deterministic rules decide. The model explains and drafts the fix. Native tooling validates. And the pull request gets a comment, never a merge. That division of labour is the whole design, and it is why the reviewer can be trusted in C I.

**[path0]** Day one starts with parsers for Terraform plan output and Kubernetes YAML, using native libraries, so every finding keeps its file, line and resource provenance. Then a small, honest ruleset: public exposure, privileged workloads, overly broad permissions. Each rule has a stable I D, severity, rationale, references, exceptions and test fixtures, including secure configurations to measure false positives.

**[path1]** Then the agent. It receives the parsed resource and the rule evidence and returns a concise explanation, its uncertainty and a remediation rationale, in a strict schema. You verify that nothing it says can change a policy outcome.

**[path2]** Day two is remediation. Minimal candidate diffs, only for supported cases, never touching unrelated files. Every patch runs through formatting, syntax validation, native tooling, policy checks and tests before it is allowed to call itself validated. You will watch an invalid patch get rejected.

**[path3]** Then integration. A local review report first, then pull request comments in a sandbox repository through a C I workflow. The integration is read-only by default, handles untrusted repository content safely, and never merges. You finish with an evaluation: precision and recall on the fixture set, unsupported statements, patch validity and review noise.

**[labs]** Labs run on a sandbox repository with seeded misconfigurations, so you can see real pull request comments appear, with evidence and a validated patch attached.

**[mods]** Here is the full table of contents, 6 modules over two days. Day one: Supported formats, parsers and provenance; Deterministic policy rules; and AI explanations in a strict schema. Day two: Candidate diffs and native validation; Pull-request integration, read-only by default; and Evaluation, developer experience and capstone.

**[princ]** Every build in this course follows six engineering principles. Model output is a proposal, never a fact. Authorization lives outside the model. A human approves every consequential action. Decisions and evidence are logged. The stack stays provider-agnostic. And quality is measured, not assumed.

**[stats]** Two days, hands-on. Two formats, Terraform and Kubernetes. Zero auto-merges, ever. One C I integrated reviewer you can take home.

**[who]** This course is for DevSecOps, platform and cloud engineers, infrastructure as code authors and security champions inside engineering teams. You need Terraform or Kubernetes basics, Git and pull requests, and Python fundamentals.

**[cta]** Catch line two fourteen before it ships. The Agentic Configuration Reviewer. Enrol now at gennoor dot com.