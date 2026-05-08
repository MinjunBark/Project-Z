# Integration: Figma
Added: 2026-05-07
Status: Pending

## Why We Use This
Design boards and visual assets — Figma API enables agents to read design context,
extract assets, and coordinate between design and implementation phases.

## Setup
1. Go to Figma → Account Settings → Personal Access Tokens
2. Generate a new token with required scopes
3. Set FIGMA_ACCESS_TOKEN in your .env file (see config-template.env)
4. Note your File Key from any Figma file URL (figma.com/design/[FILE_KEY]/...)

## API / Connection Details
- Auth method: Personal Access Token (header: X-Figma-Token)
- Key location: FIGMA_ACCESS_TOKEN (env variable)
- Official docs: https://www.figma.com/developers/api

## Usage in This Project
- Agents: TBD — assigned when activated
- Triggers: TBD
- Outputs land in: TBD

## Test Results
See `test-notes.md` — not yet tested.

## Activation Decision
CEO approved: Pending
