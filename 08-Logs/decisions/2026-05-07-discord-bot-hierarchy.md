# Decision: Discord Bot Hierarchy — Project Z Agent as Admin
Date: 2026-05-07
Decided by: CEO

## Context
Discord server has been set up with one bot (Project Z Agent). As the agency scales,
additional specialized bots will be added (content, scraper, reporting, etc.).
A hierarchy decision was needed: what permission level does each bot hold?

## Decision
Project Z Agent holds Administrator permission permanently — it is the infrastructure
bot responsible for creating channels, managing webhooks, and onboarding all future bots.

All future bots receive only the minimum permissions required for their specific function.
No other bot gets Administrator.

## Bot Permission Protocol
When a new bot is added:
1. Define its exact required permissions (minimum viable)
2. Create its Discord application via Project Z Agent or developer portal
3. Invite with scoped permissions only
4. Document in this README under Bot Hierarchy section
5. Log activation in `08-Logs\decisions\`

## Assumptions
Project Z Agent token is stored securely in `.env` and never shared publicly.

## Revisit Trigger
If Discord changes how bot permissions work, or if a future bot legitimately
requires elevated permissions beyond its role scope.
