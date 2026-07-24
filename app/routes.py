from fastapi import APIRouter
from fastapi import Request

from app.audit import audit_url
from app.models import AuditRequest

from app.responses import success, failure

from app.exceptions import AuditException

from app.limiter import limiter

router = APIRouter()


@router.get("/")
def home():

    return {

        "project": "Page Pulse",

        "message": "API is running successfully!"

    }


@router.post("/audit")
@limiter.limit("5/minute")
def audit(request: Request, body: AuditRequest):

    try:

        result = audit_url(str(body.url))

        return success(result)

    except AuditException as e:

        return failure(str(e))