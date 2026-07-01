from app.guardrails import check_content
from app.models import CampaignInput, ContentPack, EvaluationResult, MarketingBrief


RESTAURANT_TERMS = (
    "restaurant",
    "cafe",
    "coffee",
    "dish",
    "menu",
    "dining",
    "dine-in",
    "takeaway",
    "ordering",
    "plating",
    "prep",
    "local",
)


def _content_text(content: ContentPack) -> str:
    calendar_text = " ".join(
        f"{item.day} {item.channel} {item.content_type} {item.hook} {item.asset_needed} {item.cta}"
        for item in content.content_calendar
    )
    return " ".join(
        [
            content.linkedin_post,
            content.short_video_script,
            content.cta,
            *content.content_types,
            *content.carousel_outline,
            *content.shot_list,
            *content.publishing_checklist,
            calendar_text,
        ]
    ).lower()


def _context_score(content: ContentPack, context: CampaignInput | MarketingBrief | None) -> int:
    if context is None:
        return 4 if len(content.linkedin_post.split()) >= 20 else 1
    if not context.target_audience.strip():
        return 1
    text = _content_text(content)
    terms = [
        term.strip().lower()
        for term in [context.target_audience, context.product_service, context.campaign_goal]
        if term.strip()
    ]
    matches = sum(term in text for term in terms)
    return 5 if matches == len(terms) else 3 if matches >= 2 else 1


def _restaurant_score(content: ContentPack, context: CampaignInput | MarketingBrief | None) -> int:
    text = _content_text(content)
    context_text = ""
    if context is not None:
        context_text = " ".join(
            [context.target_audience, context.product_service, context.campaign_goal, context.constraints]
        ).lower()
    matches = sum(term in f"{text} {context_text}" for term in RESTAURANT_TERMS)
    return 5 if matches >= 4 else 3 if matches >= 2 else 1


def evaluate_campaign(content: ContentPack, context: CampaignInput | MarketingBrief | None = None) -> EvaluationResult:
    warnings = check_content(content)
    scores = {
        "audience_specificity": _context_score(content, context),
        "content_usefulness": 5 if len(content.carousel_outline) >= 5 else 1,
        "restaurant_specificity": _restaurant_score(content, context),
        "calendar_usefulness": 5 if len(content.content_calendar) >= 4 else 3 if len(content.content_calendar) >= 3 else 1,
        "visual_guidance": 5 if len(content.shot_list) >= 4 else 3 if len(content.shot_list) >= 2 else 1,
        "actionability": 4 if content.publishing_checklist else 1,
        "cta_quality": 4 if content.cta.strip() else 1,
        "risk_control": 5 if not warnings else 3,
    }
    total = sum(scores.values())
    return EvaluationResult(
        total_score=total,
        passed=total >= 28 and not any("Missing CTA" in item for item in warnings),
        scores=scores,
        suggestions=warnings,
    )
