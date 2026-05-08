# Platform Registry — Project Z
_Loaded every session. Documents all external integrations, their purpose,
and their current activation status._

---

## Activation Rule
A platform is added to Active only after:
1. It has been tested with a real use case
2. It delivered a measurable, beneficial outcome
3. CEO has approved activation (log entry in `08-Logs\decisions\`)

Do NOT integrate a platform speculatively. Prove it first.

---

## Active Integrations

| Platform | Purpose | Integration Folder | Activated |
|----------|---------|-------------------|-----------|
| Discord | Agent notifications, CEO approvals, feedback loop | `04-Systems\integrations\discord\` | 2026-05-07 |

---

## Pending (Under Evaluation)

| Platform | Purpose | Integration Folder | Status |
|----------|---------|-------------------|--------|
| Notion | Technical documentation, user manuals | `04-Systems\integrations\notion\` | Pending testing |
| Figma | Design boards, visual assets | `04-Systems\integrations\figma\` | Pending testing |

---

## Retired Integrations
_Platforms that were tested and did not deliver value, or were replaced._

---

## Integration File Structure
Each platform folder in `04-Systems\integrations\[platform-name]\` contains:
- `README.md` — purpose, setup steps, API key location, usage in this project
- `config-template.env` — environment variable names (no actual keys — never committed)
- `test-notes.md` — test results and verdict for CEO activation decision

See `04-Systems\integrations\_integration-template\` for the blank template.
