# Terraform and GitHub Automation with Claude - promo narration

Voice: the presenter's own cloned voice. Duration: 6.2 min.

**[hook]** Your Terraform apply just removed a production virtual server. The plan said minus one. Nobody read it. The change went through at two in the morning, and the incident bridge opened at six.

**[hook]** What if Claude read every plan, explained every change in plain English, flagged the common mistakes before they reached a device, and the apply ran only after a person clicked approve? That is Terraform and GitHub automation, done with Claude, done safely.

**[intro]** Gennoor Tech presents Terraform and GitHub Automation with Claude.

**[story]** One repository. One pull request per change. You learn Terraform step by step, you learn the mistakes that burn real teams, and you put Claude to work as planner, explainer and reviewer. Claude drafts the code and reads the plan. Deterministic pipelines run the apply. A human approves anything that touches a device, and every step is logged. By the end you own a repository your whole team can work in.

**[path0]** You start with infrastructure as code for network and load balancer teams. Providers, resources, variables, outputs and state, written in H C L. Then you set up Claude Code, the Claude Agent S D K and an M C P server that exposes the Terraform C L I as tools, so the agent can run init, validate and plan, but never apply on its own. You will see exactly which tools the agent holds and which it does not.

**[path0]** Then Terraform, step by step. Init, plan, apply, and the state file that makes it all work. You read a plan line by line, you import a virtual server that already exists, and you move to remote state with locking, workspaces for dev and prod, and modules you can reuse for every site.

**[path1]** Day two opens with the common mistakes. Unpinned provider versions. Secrets hard coded in variables. Count where for each belonged. A state file committed to Git. A targeted apply that left drift behind. Each mistake gets a name, a symptom and a fix. You reproduce each one in the lab, then wire in the checks that catch it: terraform format, validate, tflint and a Claude review that names the mistake and cites the line.

**[path2]** Then GitHub. Branches, commits, a git ignore that keeps state and secrets out of the repository, pull requests with required reviewers, code owners and branch protection. GitHub Actions runs plan on every pull request and apply only on merge, with the plan output posted as a comment for the team to read before anyone clicks approve. Guardrails follow: an allow list of resource types, a block on destroy without a change ticket, approval gates in GitHub environments, and an audit record for every plan and apply.

**[path3]** Day three brings the agent into the review loop. An Agent S D K application reads the plan as J S O N, returns a structured verdict with risk level, affected resources and a plain English summary, and posts it to the pull request. It never merges and it never applies. When it cannot classify a resource, it says so and asks for a human.

**[path3]** Finally, the devices themselves. The F5 BIG-IP provider for virtual servers, pools and certificates. The Citrix A D C provider for NetScaler. The Cisco A C I provider for tenants and bridge domains. And Python wrappers for Radware Alteon and other load balancers (Anaya LB) where no provider exists, so one workflow covers the whole estate.

**[labs]** Every lab runs against a shared GitHub organization and lab devices in a sandbox. Nothing you do in the lab can reach a production device. You will commit a state file on purpose, watch Claude catch it, break a plan with an unintended destroy, and see the approval gate hold until a person says yes.

**[mods]** Here is the full table of contents, 10 modules over three days. Day one: Infrastructure as code for network and load balancer teams; Setting up Claude Code, the Agent SDK and MCP for Terraform work; and Terraform scripting step by step: init, plan, apply, state. Day two: Common Terraform mistakes and how to catch them early; GitHub repository fundamentals for infrastructure code; GitHub Actions pipelines: plan on pull request, apply on merge; and Guardrails, approvals and audit for Terraform and GitHub automation. Day three: Claude as plan reviewer: Agent SDK, MCP and structured verdicts; Terraform for F5, NetScaler, Cisco ACI and other load balancers; and Capstone: end-to-end change through the Claude-reviewed pipeline.

**[princ]** Every build in this course follows six engineering principles. Model output is a proposal, never a fact. Authorization lives outside the model. A human approves every consequential action. Decisions and evidence are logged. The stack stays provider-agnostic. And quality is measured, not assumed.

**[stats]** Ten modules. Three days, hands-on. Five common mistakes reproduced and fixed. And zero applies without a human approval.

**[who]** This course is for enterprise I T and network operations teams, load balancer and data center engineers, and platform teams moving to infrastructure as code, in India and worldwide. You need basic Linux and networking knowledge. Git helps, and no prior Terraform is required.

**[cta]** Ship every change through a pull request, not a prayer. Terraform and GitHub Automation with Claude. Enrol now at gennoor dot com.