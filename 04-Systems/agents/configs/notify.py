import os
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent.parent / "integrations" / "discord" / ".env")

WEBHOOKS = {
    # Phase 0
    "brand-voice":       os.getenv("DISCORD_WEBHOOK_BRAND_VOICE"),
    # Original channels (webhooks backfilled 2026-05-07)
    "seo-research":      os.getenv("DISCORD_WEBHOOK_SEO_RESEARCH"),
    "scraper-output":    os.getenv("DISCORD_WEBHOOK_SCRAPER_OUTPUT"),
    "content-output":    os.getenv("DISCORD_WEBHOOK_CONTENT_OUTPUT"),
    "corrections":       os.getenv("DISCORD_WEBHOOK_CORRECTIONS"),
    # Core operations
    "agent-status":      os.getenv("DISCORD_WEBHOOK_AGENT_STATUS"),
    "approvals":         os.getenv("DISCORD_WEBHOOK_APPROVALS"),
    "errors":            os.getenv("DISCORD_WEBHOOK_ERRORS"),
    "prompt-coach":      os.getenv("DISCORD_WEBHOOK_PROMPT_COACH"),
    "decisions":         os.getenv("DISCORD_WEBHOOK_DECISIONS"),
    # Pipeline channels
    "content-calendar":  os.getenv("DISCORD_WEBHOOK_CONTENT_CALENDAR"),
    "creative-review":   os.getenv("DISCORD_WEBHOOK_CREATIVE_REVIEW"),
    "published":         os.getenv("DISCORD_WEBHOOK_PUBLISHED"),
    "research-intel":    os.getenv("DISCORD_WEBHOOK_RESEARCH_INTEL"),
    "client-onboarding": os.getenv("DISCORD_WEBHOOK_CLIENT_ONBOARDING"),
}

STATUS_COLORS = {
    "complete": 3066993,   # green
    "waiting":  16776960,  # yellow
    "error":    15158332,  # red
    "progress": 3447003,   # blue
}


def post_to_discord(
    channel: str,
    agent_name: str,
    status: str,
    title: str,
    message: str,
    fields: list[dict] | None = None,
) -> None:
    url = WEBHOOKS.get(channel)
    if not url:
        raise ValueError(f"No webhook configured for channel: '{channel}'. "
                         f"Valid channels: {list(WEBHOOKS.keys())}")

    embed = {
        "title": title,
        "description": message,
        "color": STATUS_COLORS.get(status, STATUS_COLORS["progress"]),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "footer": {"text": "Project Z Agent System"},
    }

    if fields:
        embed["fields"] = fields

    payload = {
        "username": agent_name,
        "embeds": [embed],
    }

    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()


# Convenience wrappers
def notify_status(agent: str, title: str, message: str, fields=None):
    post_to_discord("agent-status", agent, "progress", title, message, fields)

def notify_complete(agent: str, title: str, message: str, fields=None):
    post_to_discord("agent-status", agent, "complete", title, message, fields)

def notify_approval_needed(agent: str, title: str, message: str, fields=None):
    post_to_discord("approvals", agent, "waiting", title, message, fields)

def notify_error(agent: str, title: str, message: str, fields=None):
    post_to_discord("errors", agent, "error", title, message, fields)

def notify_decision(agent: str, title: str, message: str, fields=None):
    post_to_discord("decisions", agent, "complete", title, message, fields)

def notify_research_intel(agent: str, source_url: str, tag: str, bullets: list[str]):
    """Post a research finding to #research-intel. Max 5 bullets. No paragraphs."""
    if len(bullets) > 5:
        raise ValueError("research-intel posts are capped at 5 bullets")
    bullet_text = "\n".join(f"- {b}" for b in bullets)
    post_to_discord(
        channel="research-intel",
        agent_name=agent,
        status="progress",
        title=f"{tag} {source_url}",
        message=bullet_text,
    )

def notify_published(agent: str, client: str, platform: str, url: str):
    post_to_discord("published", agent, "complete", f"Published: {client}",
        f"Platform: {platform}\n{url}")

def notify_onboarding(agent: str, client: str, message: str, fields=None):
    post_to_discord("client-onboarding", agent, "progress", f"Onboarding: {client}", message, fields)

def notify_creative_review(agent: str, content_id: str, verdict: str, notes: str):
    status = "complete" if verdict == "APPROVE" else "waiting" if verdict == "REVISE" else "error"
    post_to_discord("creative-review", agent, status, f"QA [{verdict}]: {content_id}", notes)

def notify_prompt_coach(original: str, rewrite: str, coaching_note: str):
    post_to_discord(
        channel="prompt-coach",
        agent_name="Prompt Coach (Tier 2)",
        status="progress",
        title="Prompt Optimization",
        message="New prompt log entry — review and apply when ready.",
        fields=[
            {"name": "Original", "value": original[:1024], "inline": False},
            {"name": "Optimized Rewrite", "value": rewrite[:1024], "inline": False},
            {"name": "Coaching Note", "value": coaching_note[:512], "inline": False},
        ],
    )
