from fastapi import FastAPI, Request

app = FastAPI()

@app.api_route("/", methods=["GET", "POST"])
@app.api_route("/webhook", methods=["GET", "POST"])
async def webhook(request: Request):
    try:
        data = await request.json()
    except:
        data = {"message": "no json payload"}

    print("🔥 Webhook received:")
    print(data)

    return {"status": "ok"}

    print("final test")