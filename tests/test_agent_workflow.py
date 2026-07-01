from app.agent import campaign_from_brief, render_campaign_markdown, run_campaign
from app.models import CampaignInput


def test_run_campaign_returns_complete_pack_without_api_key():
    campaign = CampaignInput(
        business_name="Adam Yan AI",
        product_service="AI workflow education for Vietnamese office workers",
        target_audience="Vietnamese office workers and marketers",
        campaign_goal="Teach practical AI agent workflows for content production",
        platform="LinkedIn",
        tone="Practical, professional, direct",
        language="Vietnamese",
        constraints="No hype. Include actionable steps.",
        source_notes="Focus on busy operators who need repeatable workflows.",
    )

    pack = run_campaign(campaign)

    assert pack.brief.business_name == "Adam Yan AI"
    assert pack.audience.pain_points
    assert pack.strategy.hook
    assert pack.content.linkedin_post
    assert len(pack.content.carousel_outline) >= 5
    assert pack.content.content_types
    assert len(pack.content.shot_list) >= 4
    assert len(pack.content.content_calendar) >= 4
    assert pack.content.short_video_script
    assert pack.content.cta
    assert pack.content.publishing_checklist
    assert pack.evaluation.total_score > 0
    assert pack.evaluation.scores["restaurant_specificity"] >= 3
    assert pack.evaluation.scores["calendar_usefulness"] == 5
    assert pack.evaluation.scores["visual_guidance"] == 5
    assert isinstance(pack.warnings, list)
    assert isinstance(pack.assumptions, list)

    markdown = render_campaign_markdown(pack)
    assert "## Content Types" in markdown
    assert "## Photo and Shot Guidance" in markdown
    assert "## Short Content Calendar" in markdown
    assert "## LinkedIn Post" in markdown
    assert "## Evaluation" in markdown
    assert "## Warnings and Assumptions" in markdown


def test_business_brief_generates_specific_real_world_pack():
    campaign = campaign_from_brief(
        "Loyal Beans",
        (
            "Audience: Vietnamese coffee shop owners. "
            "Offer: Zalo loyalty program setup. "
            "Goal: get 20 repeat orders in 30 days. "
            "Channels: Facebook, Instagram, Zalo, Google Business Profile. "
            "Constraint: no discount race."
        ),
    )

    pack = run_campaign(campaign)
    markdown = render_campaign_markdown(pack).lower()

    assert campaign.target_audience == "Vietnamese coffee shop owners"
    assert campaign.product_service == "Zalo loyalty program setup"
    assert campaign.campaign_goal == "get 20 repeat orders in 30 days"
    assert campaign.platform == "Facebook, Instagram, Zalo, Google Business Profile"
    assert "coffee shop owners" in markdown
    assert "zalo loyalty program" in markdown
    assert "repeat orders" in markdown
    assert "discount framing" not in " ".join(pack.warnings).lower()
    assert "hero dish" in markdown
    assert "google business profile" in markdown
    assert "comment 'workflow'" not in pack.content.linkedin_post.lower()


def test_brief_without_audience_keeps_guardrail_warning():
    campaign = campaign_from_brief(
        "Invoice Helper",
        "Offer: monthly invoice cleanup. Goal: reduce missed invoice deadlines.",
    )

    pack = run_campaign(campaign)

    assert campaign.target_audience == ""
    assert "target audience" in " ".join(pack.warnings).lower()


def test_vietnamese_labeled_brief_is_extracted():
    campaign = campaign_from_brief(
        "Loyal Beans",
        (
            "Khách hàng: chủ quán cà phê Việt Nam. "
            "Dịch vụ: thiết lập chương trình khách hàng thân thiết trên Zalo. "
            "Mục tiêu: có 20 đơn quay lại trong 30 ngày."
        ),
    )

    assert campaign.target_audience == "chủ quán cà phê Việt Nam"
    assert campaign.product_service == "thiết lập chương trình khách hàng thân thiết trên Zalo"
    assert campaign.campaign_goal == "có 20 đơn quay lại trong 30 ngày"
