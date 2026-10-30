# Per-course research and content plan: data format

One JSON file per course, `tools/research/<exact course title>.json`. `tools/build_research.py` turns each into
`TOC-output/<course>/Research/<course> - Research and Content Plan` (.md, .html, .docx, watermarked .pdf).

Cite inline with `[c1]`, `[c2]` ... in any text field; the ids refer to `citations`. Every cited URL must have been
opened and checked to contain the stated fact. No content is split by hour (every day is 8 hours).

```json
{
  "course": "exact title from content.py",
  "domain": "Cybersecurity | Network and Infrastructure Automation | Business Process Automation",
  "source_input": "the client input this course came from, quoted or closely paraphrased",
  "why_this_course": ["paragraph", "paragraph"],
  "design_decisions": [{"decision": "...", "rationale": "..."}],
  "audience_profile": [{"role": "...", "needs": "...", "starting_point": "..."}],
  "prerequisite_check": ["a skill or question to check before enrolling"],
  "lab_environment": {
    "overview": "...",
    "components": [{"name": "...", "version": "...", "purpose": "...", "how_to_obtain": "...", "notes": "..."}],
    "fixtures": [{"name": "...", "contents": "...", "used_in": "module title(s)"}],
    "safety": ["..."]
  },
  "modules": [{
    "day": 1,
    "title": "exact module title from content.py",
    "goal": "one sentence",
    "learning_objectives": ["Learners can ..."],
    "lessons": [{"title": "...", "points": ["concrete teaching point [c3]"]}],
    "instructor_demo": ["step", "step"],
    "lab": {"brief": "...", "steps": ["..."], "success_criteria": ["..."]},
    "common_pitfalls": ["..."],
    "knowledge_check": [{"q": "...", "a": "..."}],
    "slides_and_assets": ["..."],
    "sources": ["c1", "c4"]
  }],
  "capstone_plan": {"brief": "...", "milestones": ["..."], "evaluation_notes": ["..."]},
  "promo_video_research": {
    "hook_basis": "why the opening scenario of the promo is realistic [c2]",
    "claims_check": [{"claim": "statement or on-screen text from the promo", "basis": "where it comes from [c5]"}]
  },
  "citations": [{"id": "c1", "title": "...", "url": "...", "publisher": "...", "supports": "module or section",
                 "key_fact": "...", "verified": "2026-10-30"}]
}
```
