# Agent Roster — Project Z
_All agents operating in this workspace must appear here.
No agent activates without a defined role file._

---

## Universal Rules
All agents operate under the Non-Negotiable Rules defined in `CLAUDE.md`.
No exceptions.

---

## Role Hierarchy

Defines authority, task assignment, and escalation direction.
Higher tiers assign work to lower tiers. Lower tiers escalate up.

```
Tier 0 │ CEO (you)
       │ Ultimate authority. Vision, strategy, final approval.
       │
Tier 1 │ Primary Agent (Claude)
       │ Generalist orchestrator. Advises CEO, coordinates all agents,
       │ executes across all domains when no specialist is assigned.
       │
Tier 2 │ Strategist  ·  Creative Director  ·  Prompt Coach
       │ Meta-level functions: direction-setting, QA gatekeeping, comms quality.
       │ Advise CEO directly. Work reviewed by CEO, not Tier 1.
       │
Tier 3 │ Brand Analyst  ·  Researcher  ·  SEO Specialist
       │ Content Writer  ·  Creative Prompter  ·  Engineer
       │ Publisher  ·  Analyst
       │ Domain executors. Receive tasks from Tier 1 or Tier 2.
       │ Output reviewed by Tier 1 before CEO sees it (unless urgent).
       │
Tier 4 │ [Future specialist agents]
       │ Narrow-task roles added as work proves they are needed.
       │ Assigned and reviewed by Tier 3 leads.
```

Escalation path: Tier 4 → Tier 3 → Tier 1 → CEO
Creative Director (Tier 2) → CEO directly for content escalations
Prompt Coach (Tier 2) → CEO directly

---

## Active Agents

| Tier | Role | Expertise Domain | Decision Authority | Role File |
|------|------|-----------------|-------------------|-----------|
| 0 | CEO | All domains | Final authority on all decisions | N/A |
| 1 | Primary (Claude) | Generalist | Propose and execute; CEO approves strategy | Built-in |
| 2 | Prompt Coach | CEO communication calibration | Rewrite prompts; flag patterns; report direct to CEO | `04-Systems\agents\roles\prompt-coach.md` |

---

## Defined Roles (role file created — pending first activation)

Role file exists. Activation = CEO directs the role to take on a live task.

| Tier | Role | Domain | Role File |
|------|------|--------|-----------|
| 2 | Creative Director | QA gatekeeper, second visionary | `04-Systems\agents\roles\creative-director.md` |
| 2 | Strategist | Content calendar, campaign briefs, phase planning | `04-Systems\agents\roles\strategist.md` |
| 3 | Brand Analyst | Client onboarding, brand extraction | `04-Systems\agents\roles\brand-analyst.md` |
| 3 | Content Writer | Long-form articles, social copy, carousel scripts | `04-Systems\agents\roles\content-writer.md` |
| 3 | SEO Specialist | Keyword research, GEO/AEO strategy | `04-Systems\agents\roles\seo-specialist.md` |
| 3 | Creative Prompter | Midjourney/Gemini prompts, Figma guidance | `04-Systems\agents\roles\creative-prompter.md` |
| 3 | Publisher | Scheduling, distribution, formatting | `04-Systems\agents\roles\publisher.md` |
| 3 | Analyst | Performance tracking, reporting | `04-Systems\agents\roles\analyst.md` |

---

## Pending Roles (not yet defined)

| Tier | Role | Domain |
|------|------|--------|
| 3 | Researcher | Competitive analysis, trends, fact-checking |
| 3 | Engineer | Code, automation, scrapers, technical assets |

---

## Role Activation Protocol

Before any new agent role is activated:
1. Create `04-Systems\agents\roles\[role-name].md` with full spec
2. Define: tier, expertise scope, tools, decision authority, escalation path
3. Add to Active Agents table above
4. CEO approves activation (log entry in `08-Logs\decisions\`)

---

## Communication Architecture

```
╔══════════════════════════════════════════════════════════════════════════╗
║                           CEO  (Tier 0)                                 ║
║  Issues:   Directives · Approvals · Strategic Decisions                 ║
║  Receives: All final outputs · Prompt rewrites · Status reports ·       ║
║            Escalations from any tier                                    ║
╚══════════╤═══════════════════════╤═══════════════════════╤══════════════╝
           │                       │                       │
           │ Directives            │ Direct Reports        │ Auto-capture
           │ Approvals             │ Recommendations       │ (every prompt)
           ▼                       ▼                       ▼
  ╔═════════════════╗    ╔══════════════════╗    ╔══════════════════╗
  ║  Primary Agent  ║    ║   Strategist     ║    ║  Prompt Coach    ║
  ║   (Tier 1)      ║◄──►║   (Tier 2)       ║    ║  (Tier 2)        ║
  ║  Orchestrator   ║    ║  Direction &     ║    ║  CEO comms       ║
  ║  Hub for all    ║    ║  Planning        ║    ║  calibration     ║
  ║  Tier 3 work    ║    ╚══════════════════╝    ╚══════════════════╝
  ╚════════╤════════╝
           │
           │  Task assignments (with full context)
           │  Output reviews (before reaching CEO)
           │
     ┌─────┴────────────────────────────────────┐
     │                                          │
     ▼                                          ▼
╔════════════════╗  ╔════════════════╗  ╔════════════════╗
║ Content Writer ║  ║   Researcher   ║  ║   Engineer     ║
║   (Tier 3)     ║  ║   (Tier 3)     ║  ║   (Tier 3)     ║
╚════════╤═══════╝  ╚════════╤═══════╝  ╚════════╤═══════╝
         │                   │                   │
         └───────────────────┴───────────────────┘
                   All outputs → Primary → CEO
```

## Communication Rules

| Flow | Direction | Notes |
|------|-----------|-------|
| CEO → Primary | Directives, approvals | All work originates here |
| CEO → Strategist | Strategy-first tasks | Direct when direction-setting |
| Primary → CEO | Status reports, synthesized outputs | All Tier 3 work passes through Primary |
| Strategist → CEO | Recommendations | Direct — not filtered by Primary |
| Prompt Coach → CEO | Prompt rewrites + coaching notes | Direct — logged to 08-Logs\prompts\ |
| Primary → Tier 3 | Task assignments with full context | Primary breaks down CEO directives |
| Tier 3 → Primary | Completed outputs for review | Primary reviews before surfacing to CEO |
| Tier 3 ↔ Tier 3 | NOT ALLOWED | All cross-agent coordination via Primary |
| Any Tier → CEO | Urgent escalation | Bypass chain only when blocked or decision required |

## CEO Visibility Guarantee
No output ships, no decision is logged, no platform activates without CEO awareness.
Primary aggregates and surfaces — never filters or hides.

## Escalation Rules
- Any agent blocked → escalate to next tier up
- Any strategic decision → escalate to CEO
- Any scope change → CEO approval required before work continues
- Prompt Coach feedback → reviewed by CEO directly, no escalation needed
