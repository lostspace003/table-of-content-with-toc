# Traffic and Flow Diagram Automation with Claude - promo narration

Voice: neural TTS (en-US-AndrewNeural). Duration: 5.8 min.

**[hook]** A ticket asks for the traffic flow from the branch office to the payments V I P. Someone opens a terminal, runs traceroute, runs ping, and starts drawing boxes by hand. By the time the diagram is finished, the path has already changed.

**[hook]** What if Claude ran the probes through code you trust, read every hop as evidence, and drew the diagram for you, with a person approving before anything is published? That is traffic and flow diagram automation, done with Claude, done safely.

**[intro]** Gennoor Tech presents Traffic and Flow Diagram Automation with Claude.

**[story]** One request in. One proven diagram out. Over three days you build a pipeline in eleven modules where Claude plans and explains, deterministic Python runs ping and traceroute, and every hop in the picture traces back to a probe you can replay. Claude never guesses a path. If a hop did not answer, the diagram says so.

**[path0]** You begin with what traceroute and ping can actually prove, and what they cannot. Asymmetric return paths. Load balancers that hide pool members. Firewalls that drop I C M P. Then you set up the workbench. Claude Code on your machine, the Claude Agent S D K in Python, and an M C P server that exposes only read only probe tools, with every call logged and credentials kept out of the prompt.

**[path0]** Next you build the probe runners. Deterministic Python wrappers around ping and traceroute, with timeouts, retries and parsers that turn raw output into a typed path record. Claude requests the probes through tool use and receives structured J S O N. It cannot run a shell command on its own. And when a hop returns stars, the record marks it unknown instead of filling the gap.

**[path1]** Day two adds context. Hops are enriched from F5 through iControl REST and t m s h, from Citrix NetScaler through the NITRO A P I, from Radware Alteon and Cyber Controller, and from other load balancers, Anaya L B included, through a common adapter. The Cisco A P I C tells you where a path enters the A C I fabric. Then Claude writes Mermaid. A deterministic renderer validates the syntax, every node carries the probe I D that placed it, and unknown segments are drawn as unknown.

**[path2]** Then the module most teams skip. Guardrails. Probe targets are restricted to an approved scope list, enforced in code and not in the prompt. Rate limits and probe budgets keep automated tracing from becoming a ping storm on production links. Any diagram going to the C M D B or into a shared repository needs a named approver, and every tool call, device query and decision lands in an audit log you can hand to a reviewer.

**[path3]** Day three is publishing. The result is written to the ServiceNow incident, change or request record through the Table A P I, with the diagram and its evidence bundle attached through the Attachment A P I, and Flow Designer starting the pipeline. A GitHub pull request carries the Mermaid file, the evidence and a summary Claude wrote, and a person reviews and merges it.

**[path3]** Then drift. A GitHub Actions schedule re-runs the probes within scope, compares the new path with the published one, and opens a pull request with a diff only when something changed. Claude explains the difference in plain language. You decide what to do with it. The capstone ties it all together, from request to approved diagram, with nothing published that a person did not sign off.

**[labs]** Every lab runs in a contained environment with lab load balancers, a lab A P I C and fictional hostnames. You will watch a traceroute go dark behind a firewall, see Claude mark it unknown instead of inventing a hop, and reject a publish that has no approver.

**[mods]** Here is the full table of contents, 11 modules over three days. Day one: What a flow diagram must prove, and what probes can tell you; Setting up Claude Code, the Agent SDK and MCP for this workflow; Deterministic probe runners in Python; and Path evidence model and structured outputs. Day two: Enriching hops with load balancer context; Data centre fabric and cloud path context; Generating the traffic and flow diagram with Mermaid; and Guardrails, approvals and audit for probing and publishing. Day three: Publishing to ServiceNow and GitHub; Drift detection and scheduled re-mapping; and Capstone: request to approved flow diagram, end to end.

**[princ]** Every build in this course follows six engineering principles. Model output is a proposal, never a fact. Authorization lives outside the model. A human approves every consequential action. Decisions and evidence are logged. The stack stays provider-agnostic. And quality is measured, not assumed.

**[stats]** Eleven build modules. Three days, hands on. Four device families enriched. And zero hops drawn without evidence behind them.

**[who]** This course is for network operations, N O C, load balancer, data centre and cloud network teams, and automation leads in India and worldwide. You need T C P I P basics, hands on familiarity with ping and traceroute, and introductory Python and Git.

**[cta]** Stop drawing paths by hand. Traffic and Flow Diagram Automation with Claude. Enrol now at gennoor dot com.