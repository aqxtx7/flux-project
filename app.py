from fastapi import FastAPI, Request

app = FastAPI()

@app.api_route("/", methods=["GET", "POST"])
@app.api_route("/webhook", methods=["GET", "POST"])
async def webhook(request: Request):
    body = await request.body()
    headers = dict(request.headers)

    print("🔥 Webhook received")
    print("Headers:", headers)
    print("Raw Body:", body.decode("utf-8"))

    return {"status": "ok"}