from fastapi.testclient import TestClient

from app.main import app


def test_generate_route_renders_campaign_pack():
    client = TestClient(app)

    response = client.post(
        "/generate",
        data={
            "business_name": "Adam Yan AI",
            "product_service": "AI workflow education",
            "target_audience": "Vietnamese marketers",
            "campaign_goal": "Teach AI agents",
            "platform": "LinkedIn",
            "tone": "Practical",
            "language": "Vietnamese",
        },
    )

    assert response.status_code == 200
    assert "LinkedIn post" in response.text
    assert "Evaluation" in response.text


def test_generate_route_accepts_structured_wizard_fields():
    client = TestClient(app)

    response = client.post(
        "/generate",
        data={
            "business_name": "Corner Kitchen",
            "industry": "Restaurant",
            "location": "District 1 office and apartment area",
            "product_service": "mac and cheese with spicy crispy chicken",
            "target_audience": "office workers and nearby apartment residents",
            "campaign_goal": "increase lunch and dinner visits this week",
            "platform": "Website, Facebook, Instagram/Reels, Zalo, Google Business Profile",
            "customer_pain_points": "Lunch feels repetitive; dinner decisions are last-minute.",
            "requested_content_types": "Landing page section, Facebook post, Instagram Reel, Zalo broadcast",
            "content_calendar_length": "7 days",
            "tone": "Practical, local, appetizing",
            "language": "Vietnamese",
            "constraints": "Low budget, no discount race.",
        },
    )

    assert response.status_code == 200
    assert "Marketing campaign pack" in response.text
    assert "District 1 office and apartment area" in response.text
    assert "Landing page section" in response.text
    assert "Day 7" in response.text


def test_generate_route_accepts_short_business_brief():
    client = TestClient(app)

    response = client.post(
        "/generate",
        data={
            "business_name": "Loyal Beans",
            "business_brief": (
                "Audience: Vietnamese coffee shop owners. "
                "Offer: Zalo loyalty program setup. "
                "Goal: get 20 repeat orders in 30 days."
            ),
        },
    )

    assert response.status_code == 200
    assert "Vietnamese coffee shop owners" in response.text
    assert "Zalo loyalty program setup" in response.text
    assert "repeat orders" in response.text
    assert "Audience insight" in response.text
    assert "Content types" in response.text
    assert "Short video script" in response.text
    assert "Photo and shot guidance" in response.text
    assert "Short content calendar" in response.text
    assert "Publishing checklist" in response.text


def test_index_keeps_primary_input_small():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 200
    assert "Business name" in response.text
    assert "Industry" in response.text
    assert "Target audience" in response.text
    assert "Campaign goal" in response.text
    assert "data-step-index" in response.text
