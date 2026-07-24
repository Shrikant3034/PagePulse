from pydantic import BaseModel, HttpUrl


class AuditRequest(BaseModel):
    url: HttpUrl


class AuditResponse(BaseModel):
    url: str
    status_code: int
    response_time_ms: float
    https: bool
    title: str
    server: str
    content_length: int