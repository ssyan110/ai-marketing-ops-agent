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
    assert "Business brief" in response.text
    assert "Target audience" not in response.text
    assert "Campaign goal" not in response.text
