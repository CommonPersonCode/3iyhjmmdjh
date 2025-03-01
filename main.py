from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def send_mesage(api_key: str, text: str, chat_id: int):
    async with httpx.AsyncClient() as client:
        telegram_api = f"https://api.telegram.org/bot{api_key}/sendMessage"
        await client.get(telegram_api, params={"chat_id": chat_id, "text": text})
    return {"status": "ok"}
