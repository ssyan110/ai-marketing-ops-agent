import re

from app.evaluator import evaluate_campaign
from app.guardrails import check_content, check_input
from app.models import (
    AudienceInsight,
    ContentCalendarItem,
    CampaignInput,
    CampaignPack,
    CampaignStrategy,
    ContentPack,
    MarketingBrief,
)


def _clean(value: str, fallback: str = "") -> str:
    return " ".join((value or "").split()).strip(" .") or fallback


def _extract_labeled(text: str, labels: tuple[str, ...]) -> str:
    for label in labels:
        match = re.search(rf"(?:^|[.;\n])\s*{re.escape(label)}\s*:\s*([^.;\n]+)", text, re.IGNORECASE)
        if match:
            return _clean(match.group(1))
    return ""


def _restaurant_channels(platform: str) -> list[str]:
    channels = [_clean(channel) for channel in re.split(r"[,/]+|\band\b", platform) if _clean(channel)]
    return channels or ["Facebook", "Instagram/Reels", "Zalo", "Google Business Profile"]


def campaign_from_brief(
    business_name: str,
    business_brief: str,
    platform: str = "LinkedIn",
    language: str = "Vietnamese",
    tone: str = "Practical, specific, no hype",
) -> CampaignInput:
    notes = _clean(business_brief)
    first_sentence = _clean(re.split(r"[.;\n]", notes, maxsplit=1)[0] if notes else "")
    return CampaignInput(
        business_name=_clean(business_name, "Your business"),
        product_service=_extract_labeled(
            notes, ("offer", "product", "service", "ưu đãi", "sản phẩm", "dịch vụ", "giải pháp")
        )
        or first_sentence
        or "a practical offer",
        target_audience=_extract_labeled(
            notes, ("audience", "customer", "customers", "khách hàng", "đối tượng", "người mua", "người dùng")
        ),
        campaign_goal=_extract_labeled(notes, ("goal", "objective", "outcome", "mục tiêu", "kết quả")),
        platform=_extract_labeled(notes, ("channel", "channels", "platform", "kênh")) or _clean(platform, "LinkedIn"),
        tone=_clean(tone, "Practical, specific, no hype"),
        language=_clean(language, "Vietnamese"),
        constraints=_extract_labeled(notes, ("constraint", "constraints", "ràng buộc", "lưu ý"))
        or "Avoid unsupported claims.",
        source_notes=notes,
    )


def run_campaign(campaign: CampaignInput) -> CampaignPack:
    business = _clean(campaign.business_name, "Your business")
    offer = _clean(campaign.product_service, "a practical offer")
    audience_name = _clean(campaign.target_audience, "Vietnamese small business operators")
    goal = _clean(campaign.campaign_goal, "turn interest into a qualified next step")
    constraint = _clean(campaign.constraints, "Avoid unsupported claims.")
    language = _clean(campaign.language, "Vietnamese")
    platform = _clean(campaign.platform, "LinkedIn")
    cta = f"Message {business} for a first-step checklist on using {offer} to {goal}."
    channels = _restaurant_channels(platform)
    brief = MarketingBrief(
        business_name=business,
        product_service=offer,
        target_audience=audience_name,
        campaign_goal=goal,
        platform=platform,
        tone=_clean(campaign.tone, "Practical, specific, no hype"),
        language=language,
        constraints=constraint,
    )
    audience = AudienceInsight(
        pain_points=[
            f"{audience_name} are trying to {goal}, but daily work leaves little time for campaign planning.",
            f"They need to understand why {offer} helps now, not just what it is.",
            "They distrust broad marketing promises that do not connect to their day-to-day work.",
        ],
        objections=[
            "Will this fit my situation, or is it another generic template?",
            "What do I need to do first, and how much effort will it take?",
        ],
        motivations=[
            f"Move toward a visible business outcome: {goal}.",
            "Use a low-risk first step before committing more budget or time.",
        ],
        desired_outcomes=[
            f"A clear reason to consider {offer}.",
            "A next action they can take today.",
        ],
    )
    strategy = CampaignStrategy(
        hook=f"{audience_name}: make the path to {goal} feel concrete before asking for attention.",
        positioning=f"{business} packages {offer} as a practical next step for {audience_name} who need to {goal}.",
        message_hierarchy=[
            f"Name the costly problem blocking this goal: {goal}.",
            f"Show how {offer} removes one piece of that friction.",
            "Use one daily-work example instead of a broad claim.",
            "Ask for one small next action, not a vague expression of interest.",
        ],
        cta_direction=cta,
    )
    content = ContentPack(
        linkedin_post=(
            f"{strategy.hook}\n\n"
            f"If you run a restaurant for {audience_name}, the real problem is rarely 'we need more posts.' "
            f"It is that buyers do not see a simple path from today's friction to the goal: {goal}.\n\n"
            f"That is where {offer} needs a sharper campaign:\n"
            "1. Name the painful moment the audience already recognizes.\n"
            f"2. Connect that moment to the goal: {goal}.\n"
            f"3. Show how {offer} makes the first step easier.\n"
            "4. Add one true restaurant proof point or concrete service example before publishing.\n"
            "5. Make the CTA small enough for a busy person to act on today.\n\n"
            f"For {business}, the campaign promise should stay practical: help {audience_name} move toward the goal: {goal} while respecting this constraint: {constraint}\n\n"
            f"CTA: {cta}"
        ),
        content_types=[
            f"Hero dish/menu item post for {offer}",
            "Behind-the-counter prep or service moment",
            "Customer-situation post tied to a local lunch, dinner, or repeat-visit occasion",
            "Short Reel/TikTok showing one texture, plating, or ordering moment",
            "Google Business Profile update with a clear availability note",
        ],
        carousel_outline=[
            f"{audience_name}: the real blocker behind the goal",
            f"Why {offer} matters now",
            "The hidden cost of keeping the current workaround",
            "A before-and-after example the audience can recognize",
            "The smallest next step to reduce risk",
            f"How to talk to {business} without a big commitment",
        ],
        shot_list=[
            f"Close-up of {offer} with natural light and a clean table background",
            "One prep or plating shot that proves freshness without making unsupported claims",
            f"One owner/manager or staff handoff shot to make {business} feel local and real",
            "One menu/ordering shot that shows how customers can ask for the offer",
            "One 5-second vertical clip with hook text over the first frame",
        ],
        content_calendar=[
            ContentCalendarItem(
                day="Day 1",
                channel=channels[0],
                content_type="Hero dish post",
                hook=f"Show {offer} as the simple first step toward {goal}.",
                asset_needed="Best product photo",
                cta=cta,
            ),
            ContentCalendarItem(
                day="Day 2",
                channel=channels[min(1, len(channels) - 1)],
                content_type="Behind-the-scenes short video",
                hook="Show the prep, plating, or service moment customers cannot see from the menu.",
                asset_needed="Vertical prep clip",
                cta=cta,
            ),
            ContentCalendarItem(
                day="Day 4",
                channel=channels[min(2, len(channels) - 1)],
                content_type="Local occasion post",
                hook=f"Connect {offer} to when {audience_name} are most likely to act.",
                asset_needed="Dining room, takeaway, or neighborhood context photo",
                cta=cta,
            ),
            ContentCalendarItem(
                day="Day 6",
                channel=channels[min(3, len(channels) - 1)],
                content_type="Reminder and objection answer",
                hook=f"Answer the practical question: why try {offer} now?",
                asset_needed="Menu or ordering screenshot/photo",
                cta=cta,
            ),
        ],
        short_video_script=(
            f"Hook: If you are {audience_name} trying to {goal}, do not start with a generic post. "
            f"Scene 1: show the restaurant moment that makes the goal hard. "
            f"Scene 2: introduce {offer} with a close-up or prep shot. "
            f"Scene 3: show one concrete ordering, pickup, or dine-in moment. "
            f"Close: {cta}"
        ),
        cta=cta,
        publishing_checklist=[
            f"{audience_name} are named in the first two lines",
            f"The offer connects directly to the goal: {goal}",
            "Any proof point is true, specific, and source-checkable",
            f"The copy avoids claims blocked by: {constraint}",
            "The calendar is realistic for an owner or manager to execute without a marketing team",
            "The CTA asks for one realistic next action",
        ],
    )
    warnings = check_input(campaign) + check_content(content)
    evaluation = evaluate_campaign(content, campaign)
    assumptions = [
        "The campaign is for educational and marketing content, not regulated advice.",
        "No external research was used; verify factual claims before publishing.",
        f"The first deterministic MVP drafts in {language} context but does not translate full copy automatically.",
    ]
    return CampaignPack(
        brief=brief,
        audience=audience,
        strategy=strategy,
        content=content,
        evaluation=evaluation,
        warnings=warnings,
        assumptions=assumptions,
    )


def render_campaign_markdown(pack: CampaignPack) -> str:
    return "\n\n".join(
        [
            f"# Campaign Pack: {pack.brief.business_name}",
            "## Brief\n"
            f"- Product/service: {pack.brief.product_service}\n"
            f"- Audience: {pack.brief.target_audience or 'Not specified'}\n"
            f"- Goal: {pack.brief.campaign_goal}\n"
            f"- Platform: {pack.brief.platform}\n"
            f"- Tone: {pack.brief.tone}\n"
            f"- Language: {pack.brief.language}",
            "## Audience Insight\n"
            + "\n".join(
                f"- {item}"
                for item in (
                    pack.audience.pain_points
                    + pack.audience.objections
                    + pack.audience.motivations
                    + pack.audience.desired_outcomes
                )
            ),
            "## Strategy\n"
            f"**Hook:** {pack.strategy.hook}\n\n"
            f"**Positioning:** {pack.strategy.positioning}\n\n"
            + "\n".join(f"- {item}" for item in pack.strategy.message_hierarchy),
            "## Content Types\n" + "\n".join(f"- {item}" for item in pack.content.content_types),
            f"## LinkedIn Post\n{pack.content.linkedin_post}",
            "## Carousel Outline\n"
            + "\n".join(f"{index}. {slide}" for index, slide in enumerate(pack.content.carousel_outline, 1)),
            "## Photo and Shot Guidance\n" + "\n".join(f"- {item}" for item in pack.content.shot_list),
            "## Short Content Calendar\n"
            + "\n".join(
                f"- {item.day} | {item.channel} | {item.content_type}: {item.hook} "
                f"(Asset: {item.asset_needed}; CTA: {item.cta})"
                for item in pack.content.content_calendar
            ),
            f"## Short Video Script\n{pack.content.short_video_script}",
            f"## CTA\n{pack.content.cta}",
            "## Publishing Checklist\n"
            + "\n".join(f"- {item}" for item in pack.content.publishing_checklist),
            "## Evaluation\n"
            f"- Total score: {pack.evaluation.total_score}\n"
            f"- Passed: {'yes' if pack.evaluation.passed else 'no'}",
            "## Warnings and Assumptions\n"
            + "\n".join(f"- {item}" for item in pack.warnings + pack.assumptions),
        ]
    )
