from e_mail import schemas

from fastapi import APIRouter

from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from fastapi_mail.email_utils import DefaultChecker

router_email = APIRouter(tags=['Email'])


html = """
<p>Hi this test mail, thanks for using Fastapi-mail</p> 
"""


conf = ConnectionConfig(
    MAIL_USERNAME="Brayan Mota",
    MAIL_PASSWORD="strong_password",
    MAIL_FROM="your@email.com",
    MAIL_PORT=587,
    MAIL_SERVER="your mail server",
    MAIL_FROM_NAME="Desired Name",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


@router_email.post('/v1/email')
async def send_email(email: schemas.EmailSchema):
    message = MessageSchema(
        subject="Fastapi-Mail module",
        # List of recipients, as many as you can pass
        recipients=email.dict().get("email"),
        body=html,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
