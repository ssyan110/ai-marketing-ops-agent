from pydantic import BaseModel, Field


class CampaignInput(BaseModel):
    business_name: str
    industry: str = ""
    location: str = ""
    product_service: str
    target_audience: str
    campaign_goal: str
    platform: str
    customer_pain_points: str = ""
    requested_content_types: str = ""
    content_calendar_length: str = ""
    tone: str
    language: str
    constraints: str = ""
    source_notes: str = ""


class MarketingBrief(BaseModel):
    business_name: str
    industry: str = ""
    location: str = ""
    product_service: str
    target_audience: str
    campaign_goal: str
    platform: str
    requested_content_types: str = ""
    content_calendar_length: str = ""
    tone: str
    language: str
    constraints: str = ""


class AudienceInsight(BaseModel):
    pain_points: list[str] = Field(default_factory=list)
    objections: list[str] = Field(default_factory=list)
    motivations: list[str] = Field(default_factory=list)
    desired_outcomes: list[str] = Field(default_factory=list)


class CampaignStrategy(BaseModel):
    hook: str
    positioning: str
    message_hierarchy: list[str] = Field(default_factory=list)
    cta_direction: str


class ContentCalendarItem(BaseModel):
    day: str
    channel: str
    content_type: str
    hook: str
    asset_needed: str
    cta: str


class ContentPack(BaseModel):
    linkedin_post: str
    content_types: list[str] = Field(default_factory=list)
    carousel_outline: list[str] = Field(default_factory=list)
    shot_list: list[str] = Field(default_factory=list)
    content_calendar: list[ContentCalendarItem] = Field(default_factory=list)
    short_video_script: str
    cta: str
    publishing_checklist: list[str] = Field(default_factory=list)


class EvaluationResult(BaseModel):
    total_score: int
    passed: bool
    scores: dict[str, int] = Field(default_factory=dict)
    suggestions: list[str] = Field(default_factory=list)


class CampaignPack(BaseModel):
    brief: MarketingBrief
    audience: AudienceInsight
    strategy: CampaignStrategy
    content: ContentPack
    evaluation: EvaluationResult
    warnings: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
