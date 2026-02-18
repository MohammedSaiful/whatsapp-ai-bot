from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from App.ai_agent import get_ai_reply

app = FastAPI()


@app.get("/")
def home():
    return {"message": "WhatsApp AI Bot Running"}


@app.post("/whatsapp", response_class=PlainTextResponse)
async def whatsapp_webhook(
    Body: str = Form(...),
    From: str = Form(None),
):
    """
    Receive WhatsApp message and return AI auto-reply.
    """

    print("Message from:", From)
    print("Text:", Body)

    ai_reply = get_ai_reply(Body)

    return ai_reply
