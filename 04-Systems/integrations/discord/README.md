# Integration: Discord
Added: 2026-05-07
Status: Active

## Why We Use This
Command and control layer for Project Z. Agents post status updates, seek CEO approvals,
log findings, and surface errors in real time. CEO receives push notifications on all devices.

## Server Structure
```
PROJECT Z
├── COMMAND CENTER
│   ├── #announcements              CEO-only posts, major decisions
│   └── #general                    Open discussion
├── AGENT OPS
│   ├── #agent-status               All agents: task start / complete / blocked
│   ├── #approvals-needed           Agent needs CEO input to continue
│   └── #errors-alerts              Failures, blockers, unexpected behavior
├── PHASE 0 | ONBOARDING
│   ├── #client-onboarding          Brand Analyst status during new client setup
│   └── #brand-voice                Brand profile outputs
├── PHASE 1 | RESEARCH
│   ├── #research-intel             Scraped URLs + bullet-point findings [NEW/UPDATE]
│   ├── #seo-research               Keyword maps, GEO/AEO output
│   └── #content-calendar           Strategy output, monthly content calendar
├── PHASE 3-4 | PRODUCTION + QA
│   ├── #content-output             Copy + visual prompts — CEO approval gate
│   └── #creative-review            Creative Director QA verdicts
├── PHASE 6-7 | PUBLISH + ANALYZE
│   ├── #published                  Publisher confirmation with timestamp + platform
│   └── #scraper-output             Performance data, competitor monitoring
└── FEEDBACK LOOP
    ├── #prompt-coach-log           Original prompt + optimized rewrite
    ├── #decisions-log              Key decisions from sessions
    └── #corrections-log            Corrections applied, rules updated
```

Phase 2 (Briefing): No dedicated channel — briefs are files; summary posts to #content-calendar.
Phase 5 (CEO Gate): Uses #content-output for review and #approvals-needed if escalated.

## Bot Hierarchy

```
Project Z Agent  [Administrator]
│  Infrastructure bot — top of bot hierarchy.
│  Creates/manages channels, webhooks, and onboards future bots.
│  Token: DISCORD_BOT_TOKEN in .env
│  ID: 1502063730266083538
│
└── Future bots  [Scoped permissions only]
       Each new bot gets only the permissions it needs for its role.
       Created and managed by Project Z Agent.
       Examples: Content Writer Bot (Send Messages only),
                 Scraper Bot (Send Messages + Attach Files)
```

**Rule:** Project Z Agent is the only bot with Administrator. All others are scoped down.
New bots are added here as they are activated and proven necessary.

## API / Connection Details
- Auth method: Bot token (for API calls) + Webhook URLs (for agent notifications)
- Key locations: see `.env` file — NEVER commit `.env`
- Guild ID: 1502062363539538061
- Official docs: https://discord.com/developers/docs

## Usage in This Project
- Agents load webhook URLs from `.env` via `notify.py`
- `notify.py` location: `04-Systems\agents\configs\notify.py`
- Each agent call maps to a channel (see STATUS_COLORS and WEBHOOKS in notify.py)

## Activation Decision
CEO approved: Yes — 2026-05-07
See: `08-Logs\decisions\2026-05-07-discord-selected-over-custom-platform.md`

## Security Note
Bot token was regenerated after initial setup. Current token in `.env` is fresh.
Never share bot tokens in conversation again — paste directly into `.env` instead.
