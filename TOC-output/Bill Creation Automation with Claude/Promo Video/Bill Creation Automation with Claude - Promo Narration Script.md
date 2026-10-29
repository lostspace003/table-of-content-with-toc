# Bill Creation Automation with Claude - promo narration

Voice: the presenter's own cloned voice. Duration: 6.1 min.

**[hook]** A placed candidate's confirmation mail lands at ten in the morning. The staffing vendor needs the bill today, with G S T or without, and the amount had better be right. Someone opens a spreadsheet, retypes the figure, picks a tax rate from memory, and hopes.

**[hook]** What if Claude read the mail, extracted the amount, checked it against the vendor master, drafted both versions, and then waited for a person to say yes before the right one was numbered or sent? That is bill creation automation, done with agents, done safely.

**[intro]** Gennoor Tech presents Bill Creation Automation with Claude.

**[story]** One mail in. The right bill out. You build the pipeline in nine increments, and every increment is something you can run, test and demonstrate. Claude reads, extracts and explains. Deterministic Python computes the tax. A person approves. Every step is logged, from the first prompt to the issued document.

**[path0]** You begin with the workflow as it really happens. Who sends the mail, what a compliant tax invoice must carry, and when the company issues with G S T and when it issues a bill of supply without it. Then you set up the toolchain. Claude Code on your workstation. The Claude Agent S D K in Python. And an M C P server that exposes your mailbox and vendor master as read-only tools the agent can call but never bypass.

**[path0]** Then intake. The agent reads each mail through the Microsoft Graph A P I or I M A P, including the P D F attachments, and returns a strict J S O N record: candidate, vendor, amount, currency, G S T I N, service period, and a confidence score for every field. Pydantic validates the record. Anything missing or contradictory is flagged for a person, never guessed.

**[path1]** On day two the numbers meet the rules. You load the vendor master into S Q Lite and reconcile the claimed amount against the rate card, with a tolerance you control and a reason for every mismatch. Then you write the G S T engine as plain Python. C G S T and S G S T for intra-state supply. I G S T across states. H S N and S A C codes, rounding, and reverse charge where it applies. Claude explains the computation to the reviewer. It never performs it.

**[path2]** Then generation. Two versioned templates, a tax invoice and a bill of supply, rendered to P D F by the same deterministic code every time, from the same validated request. Both previews are drafted; only the one that applies is ever issued. Invoice numbers live in a sequence that only the approved path can advance. Claude drafts the covering mail and the one-paragraph summary a finance reviewer actually reads.

**[path3]** Day three is guardrails. Every bill enters an approval queue with the source mail, the extracted fields, the reconciliation result, the tax breakdown and both previews side by side. A person approves in ServiceNow or in the review C L I. Until then nothing is numbered, nothing is sent, and the audit log records who saw what, who decided, and when.

**[path3]** You then harden the pipeline. Pytest covers the G S T engine across every rate slab and every state pair, with golden P D F files guarding the templates. GitHub Actions runs the suite on every pull request and push. And approved bills export to your accounting system as C S V or Tally X M L, ready for posting, with the mail dispatched only after the approver's decision is recorded.

**[labs]** Every lab runs on a synthetic mailbox and a fictional vendor master. You will feed the agent a mail with a missing G S T I N and watch it refuse to proceed. You will trace an over-claim to its rate-card line, break a rate slab in a pull request and see the build fail, then approve a bill and read its complete audit trail.

**[mods]** Here is the full table of contents, 9 modules over three days. Day one: The vendor bill workflow and the agentic baseline; Setting up Claude Code, the Agent SDK and MCP for billing; and Mail intake and structured extraction. Day two: Vendor master, amount verification and reconciliation; The GST computation engine; and Bill generation, numbering and templates. Day three: Guardrails, approvals and audit for bill issuance; Testing, CI and accounting hand-off; and Capstone: end-to-end bill creation pipeline.

**[princ]** Every build in this course follows six engineering principles. Model output is a proposal, never a fact. Authorization lives outside the model. A human approves every consequential action. Decisions and evidence are logged. The stack stays provider-agnostic. And quality is measured, not assumed.

**[stats]** Nine build steps. Three days, hands-on. Two drafts from one source of truth, one bill issued. And zero bills issued without approval.

**[who]** This course is for enterprise I T and network operations teams, finance operations and shared-services engineers, and automation and platform teams in India and worldwide who want to automate billing without surrendering control. You need basic Python, comfort with J S O N, and a working knowledge of G S T invoicing.

**[cta]** Turn every candidate mail into a correct bill, with a person in the loop. Bill Creation Automation with Claude. Enrol now at gennoor dot com.