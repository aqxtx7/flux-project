from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()
    except:
        data = {"message": "no json payload"}

    print("🔥 Webhook received:")
    print(data)

    return {"status": "ok"}