from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(examples=["ok"])
    service: str = Field(examples=["FlowForge"])
    version: str = Field(examples=["0.1.0"])
    environment: str = Field(examples=["development"])
