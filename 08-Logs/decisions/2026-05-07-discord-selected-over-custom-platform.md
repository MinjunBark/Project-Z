# Decision: Discord Selected as Communication Layer
Date: 2026-05-07
Decided by: CEO (Primary Agent recommendation)

## Context
CEO proposed building a custom communication platform with channels, bots, agent tracking,
feedback loop, and scraper notifications. Evaluated against using an existing platform.

## Options Considered
- Option A: Build a custom web application — full control, fits exact needs
- Option B: Use Slack — MCP tools available, but 90-day message history on free tier
- Option C: Use Discord — free forever, no message limits, full API, webhook support

## Decision
Discord (Option C). Covers every stated requirement at zero cost with zero build time.
Custom platform deferred — revisit trigger: 5+ clients, revenue positive, specific gaps
Discord cannot fill.

## Assumptions
Discord's free tier remains unlimited for message history and webhooks.
Agent notification volume stays within Discord's rate limits.

## Revisit Trigger
If Discord's free tier changes significantly, or if a client-facing communication
requirement emerges that Discord cannot satisfy.
