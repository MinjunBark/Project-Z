# Project Z — CLAUDE.md
_Loaded at the start of every session. All agents read this first._

---

## Project Identity
Autonomous, client-facing marketing agency directed by a CEO.
Core product: end-to-end social media presence pipeline — brand voice extraction,
content funnels, SEO/GEO/AEO strategy, competitive analysis, and campaign delivery.
Build methodology: Agile. One proven step at a time.
Agents support execution. The CEO sets direction and makes final calls.

## Who I Am Working With
See `AboutMe.md` for the full CEO profile.
- CEO makes all strategic decisions
- Agents propose, analyze, build — CEO approves
- When in doubt: surface to CEO, do not decide independently

---

## Non-Negotiable Operating Rules

### No Guessing. Ever.
If any agent does not know the answer with 99% confidence:
1. STOP — do not generate a response based on assumption
2. Perform a web search and locate factual, citable sources
3. Present findings with source links before proceeding
4. If no reliable source is found — surface the gap to the CEO explicitly
5. Do not fill knowledge gaps with inference or estimation

Guesswork is not scalable. Every unverified claim is technical debt.
This applies to: facts, statistics, tool behavior, market conditions,
technical implementation details, and anything domain-specific.

### Ask Observant Questions
Before executing, identify and surface assumptions.
If a decision has unexamined risks, flag them with evidence — not opinions.
Challenge strategy. It is expected and required.

### No Over-Engineering
Solve what is directly in front of us.
Do not add features, abstractions, or complexity beyond the task.
Simple, working, and documented beats clever and fragile.

---

## Documentation Rules (Mandatory)

Every session must produce at least one log entry when applicable:

| Event Type | Log Location |
|------------|-------------|
| New implementation (code, files, structure) | `08-Logs\implementations\YYYY-MM-DD-[slug].md` |
| Correction to a previous output or approach | `08-Logs\corrections\YYYY-MM-DD-[slug].md` |
| Strategic or architectural decision | `08-Logs\decisions\YYYY-MM-DD-[slug].md` |
| Research finding or insight | `08-Logs\findings\YYYY-MM-DD-[slug].md` |
| Lesson learned or knowledge gap closed | `08-Logs\knowledge-checks\YYYY-MM-DD-[slug].md` |
| CEO prompt + optimized rewrite | `08-Logs\prompts\YYYY-MM-DD-[slug].md` |

Log files are named with today's date and a short descriptive slug.
Example: `2026-05-07-workspace-setup.md`

---

## Folder Reference

```
00-Inbox\         Raw ideas, unprocessed inputs
01-Projects\      Active initiatives (one subfolder each)
02-Research\      Knowledge base: competitive, references, findings
03-Content\       Creative output: scripts, copy, articles
04-Systems\       Technical: agents, integrations, automation, tools
05-Strategy\      Direction: roadmaps, decisions, plans
06-Templates\     Reusable patterns — copy before modifying
07-Outputs\       Finalized deliverables, dated bundles
08-Logs\          Feedback loop — all event types logged here
.claude\          AI context: CLAUDE.md, AboutMe.md, AGENTS.md, PLATFORMS.md
```

---

## Coding Style

- Default language: Python for scripts/automation, Markdown for docs
- No unnecessary comments — code should self-explain via naming
- All code lives in `04-Systems\`
- All agent prompts live in `04-Systems\agents\prompts\`
- No file modification without a log entry in `08-Logs\implementations\`

---

## Session Start Protocol

At the beginning of every session, the Primary Agent must fire a Discord notification
to confirm it is online. Run this command immediately after loading this file:

```
python -c "import sys; sys.path.insert(0, r'C:\Users\alex8\Documents\Project Z\04-Systems\agents\configs'); from notify import notify_status; notify_status('Primary Agent (Tier 1)', 'Session Started', 'Primary Agent online. Ready for directives.')"
```

This posts to `#agent-status`. If it fails, surface the error to CEO before proceeding.

---

## Pre-Implementation Checklist

Before any implementation, verify existing state:

| Action | Check first |
|--------|-------------|
| Create Discord channel | Fetch guild channels — does it already exist? |
| Create Discord webhook | Fetch channel webhooks — is one already attached? |
| Create file or folder | Glob/Read — does it already exist? |
| Add .env variable | Read .env — is the key already there? |
| Write agent role file | Glob roles/ — does this role file already exist? |

Never create without reading current state first.
Session context resets do not reset the real world.

---

## Agent Rules

- All agents operate under the Non-Negotiable Rules above
- No agent is activated without a defined role file in `04-Systems\agents\roles\`
- See `AGENTS.md` for the active roster, hierarchy, and communication rules
- Roles are defined before work begins — never assigned mid-task
