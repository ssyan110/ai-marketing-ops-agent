from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.agent import campaign_from_brief, render_campaign_markdown, run_campaign
from app.models import CampaignInput

app = FastAPI(title="AI Marketing Ops Agent")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "index.html", {"pack": None})


@app.post("/generate", response_class=HTMLResponse)
def generate(
    request: Request,
    business_name: str = Form("Your business"),
    business_brief: str = Form(""),
    product_service: str = Form(""),
    target_audience: str = Form(""),
    campaign_goal: str = Form(""),
    platform: str = Form("LinkedIn"),
    tone: str = Form("Practical, specific, no hype"),
    language: str = Form("Vietnamese"),
    constraints: str = Form(""),
    source_notes: str = Form(""),
) -> HTMLResponse:
    if business_brief.strip():
        campaign = campaign_from_brief(business_name, business_brief, platform, language, tone)
    else:
        campaign = CampaignInput(
            business_name=business_name,
            product_service=product_service,
            target_audience=target_audience,
            campaign_goal=campaign_goal,
            platform=platform,
            tone=tone,
            language=language,
            constraints=constraints,
            source_notes=source_notes,
        )
    pack = run_campaign(campaign)
    return templates.TemplateResponse(
        request,
        "index.html",
        {"pack": pack, "campaign": campaign, "pack_markdown": render_campaign_markdown(pack)},
    )
