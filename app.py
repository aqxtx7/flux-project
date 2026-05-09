from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()

    print("🔥 Webhook received:")
    print(payload)

    return {"status": "received"}