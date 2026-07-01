from app.models import CampaignInput, ContentPack


OVERCLAIMS = ("guaranteed", "100%", "instant results", "best in town", "best ever", "risk-free")
DISCOUNT_TERMS = ("discount", "% off", "sale", "voucher", "coupon", "free drink", "buy one get one", "bogo")
DISCOUNT_NEGATIONS = ("no discount", "avoid discount", "without discount", "discount race", "không giảm giá")


def _has_any(text: str, terms: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in terms)


def _uses_discount_trap(text: str) -> bool:
    lowered = text.lower()
    return _has_any(lowered, DISCOUNT_TERMS) and not _has_any(lowered, DISCOUNT_NEGATIONS)


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
    )


def check_input(campaign: CampaignInput) -> list[str]:
    warnings: list[str] = []
    source_text = " ".join(
        [
            campaign.product_service,
            campaign.campaign_goal,
            campaign.constraints,
            campaign.source_notes,
        ]
    )
    if not campaign.target_audience.strip():
        warnings.append("Missing target audience. Add who the campaign is for before publishing.")
    if not campaign.campaign_goal.strip():
        warnings.append("Missing campaign goal. The agent needs a clear outcome to optimize the pack.")
    if _has_any(source_text, OVERCLAIMS):
        warnings.append("Potential overclaim in source notes. Verify the claim before using it.")
    if _uses_discount_trap(source_text):
        warnings.append("Margin-risky discount framing. Add a non-discount value angle before publishing.")
    return warnings


def check_content(content: ContentPack) -> list[str]:
    warnings: list[str] = []
    content_text = _content_text(content)
    if not content.cta.strip():
        warnings.append("Missing CTA. Add one clear next action.")
    if len(content.linkedin_post.split()) < 20:
        warnings.append("LinkedIn post is too thin. Add concrete context and useful steps.")
    if len(content.carousel_outline) < 5:
        warnings.append("Carousel outline needs at least 5 slides for a complete story.")
    if content.content_calendar and len(content.content_calendar) < 3:
        warnings.append("Content calendar is too thin. Give the owner at least 3 practical posting steps.")
    if _has_any(content_text, OVERCLAIMS):
        warnings.append("Potential overclaim in generated content. Verify the claim before publishing.")
    if _uses_discount_trap(content_text):
        warnings.append("Margin-risky discount framing. Add a non-discount value angle before publishing.")
    return warnings
