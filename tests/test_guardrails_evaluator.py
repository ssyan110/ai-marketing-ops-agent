from app.evaluator import evaluate_campaign
from app.guardrails import check_content, check_input
from app.models import CampaignInput, ContentCalendarItem, ContentPack


def test_guardrails_warn_when_target_audience_is_missing():
    campaign = CampaignInput(
        business_name="Adam Yan AI",
        product_service="AI workflow education",
        target_audience="",
        campaign_goal="Create a LinkedIn campaign",
        platform="LinkedIn",
        tone="Practical",
        language="Vietnamese",
    )

    warnings = check_input(campaign)

    assert "target audience" in " ".join(warnings).lower()


def test_evaluator_scores_strong_content_higher_than_weak_content():
    strong = ContentPack(
        linkedin_post="Busy marketers do not need more AI tips. They need a repeatable workflow for turning one idea into a campaign.",
        carousel_outline=[
            "Start with the business goal",
            "Name the target audience",
            "Map pain points and objections",
            "Draft the post and carousel",
            "Check claims, CTA, and next action",
        ],
        short_video_script="Hook: Your AI content workflow is too random. Step 1: capture the goal. Step 2: define the audience. Step 3: evaluate before posting.",
        cta="Comment 'workflow' if you want the checklist.",
        publishing_checklist=["Confirm audience", "Check unsupported claims", "Add CTA"],
    )
    weak = ContentPack(
        linkedin_post="Use AI to grow faster.",
        carousel_outline=["AI is good"],
        short_video_script="Try AI.",
        cta="",
        publishing_checklist=[],
    )

    assert evaluate_campaign(strong).total_score > evaluate_campaign(weak).total_score


def test_evaluator_rewards_campaign_context_specificity():
    campaign = CampaignInput(
        business_name="Loyal Beans",
        product_service="Zalo loyalty program setup",
        target_audience="Vietnamese coffee shop owners",
        campaign_goal="get 20 repeat orders in 30 days",
        platform="LinkedIn",
        tone="Practical",
        language="Vietnamese",
    )
    specific = ContentPack(
        linkedin_post="Vietnamese coffee shop owners can use Zalo loyalty program setup to get 20 repeat orders in 30 days with one clear next step.",
        carousel_outline=["Audience", "Offer", "Goal", "Proof", "CTA"],
        short_video_script="Show the coffee shop owner problem, then show the Zalo loyalty program setup.",
        cta="Message Loyal Beans for a Zalo loyalty checklist.",
        publishing_checklist=["Check audience", "Check offer", "Check goal"],
    )
    generic = ContentPack(
        linkedin_post="Busy business owners need better marketing. Create content, post consistently, check results, and invite people to talk.",
        carousel_outline=["Problem", "Offer", "Value", "Proof", "CTA"],
        short_video_script="Show a business problem and invite people to talk.",
        cta="Message us for help.",
        publishing_checklist=["Check audience", "Check offer", "Check goal"],
    )

    assert evaluate_campaign(specific, campaign).scores["audience_specificity"] > evaluate_campaign(
        generic, campaign
    ).scores["audience_specificity"]


def test_guardrails_warn_on_discount_trap_and_overclaim():
    campaign = CampaignInput(
        business_name="Loyal Beans",
        product_service="50% off lunch combo",
        target_audience="office workers near the cafe",
        campaign_goal="guaranteed repeat visits",
        platform="Facebook",
        tone="Practical",
        language="Vietnamese",
        source_notes="Promise instant results with a discount.",
    )

    warnings = " ".join(check_input(campaign)).lower()

    assert "discount" in warnings
    assert "overclaim" in warnings


def test_restaurant_evaluator_rewards_calendar_and_shot_guidance():
    campaign = CampaignInput(
        business_name="Loyal Beans",
        product_service="mac and cheese with spicy crispy chicken",
        target_audience="office workers near the restaurant",
        campaign_goal="increase weekday lunch visits",
        platform="Facebook, Instagram, Zalo, Google Business Profile",
        tone="Practical",
        language="Vietnamese",
    )
    content = ContentPack(
        linkedin_post="Office workers near the restaurant can try mac and cheese with spicy crispy chicken for a practical weekday lunch visit.",
        content_types=["Hero dish post", "Behind-the-scenes prep", "Google Business Profile update"],
        carousel_outline=["Audience", "Dish", "Local lunch moment", "Ordering", "CTA"],
        shot_list=[
            "Close-up dish photo",
            "Prep shot",
            "Menu ordering shot",
            "Local dining room shot",
        ],
        content_calendar=[
            ContentCalendarItem(
                day="Day 1",
                channel="Facebook",
                content_type="Hero dish",
                hook="Show the dish for lunch.",
                asset_needed="Food photo",
                cta="Message Loyal Beans to ask about lunch.",
            ),
            ContentCalendarItem(
                day="Day 2",
                channel="Instagram",
                content_type="Prep video",
                hook="Show plating and texture.",
                asset_needed="Vertical prep clip",
                cta="Message Loyal Beans to ask about lunch.",
            ),
            ContentCalendarItem(
                day="Day 4",
                channel="Zalo",
                content_type="Local reminder",
                hook="Invite nearby workers.",
                asset_needed="Dining room photo",
                cta="Message Loyal Beans to ask about lunch.",
            ),
            ContentCalendarItem(
                day="Day 6",
                channel="Google Business Profile",
                content_type="Availability update",
                hook="Tell searchers what is available.",
                asset_needed="Menu photo",
                cta="Message Loyal Beans to ask about lunch.",
            ),
        ],
        short_video_script="Show the restaurant prep, plating, ordering, and dine-in moment.",
        cta="Message Loyal Beans to ask about lunch.",
        publishing_checklist=["Confirm dish", "Check claim", "Post calendar"],
    )

    result = evaluate_campaign(content, campaign)

    assert result.scores["restaurant_specificity"] == 5
    assert result.scores["calendar_usefulness"] == 5
    assert result.scores["visual_guidance"] == 5
    assert not check_content(content)
