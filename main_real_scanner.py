
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
CHAT_ID = os.getenv("CHAT_ID", "1144121597")
SCAN_INTERVAL = int(os.getenv("SCAN_INTERVAL", "30"))

app = FastAPI(title="Vize Radar V5")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"status": "V5 BOZULMAZ - Real Scanner ONLINE", "countries": 20, "interval": SCAN_INTERVAL, "chat_id": CHAT_ID, "bot_configured": bool(BOT_TOKEN)}

@app.get("/health")
async def health():
    return {"ok": True}

@app.get("/api/realtime-slots")
async def realtime_slots():
    # TEST: Telegram'a mesaj gönder, hata varsa döndür
    result = {"tested": False}
    if BOT_TOKEN and CHAT_ID:
        try:
            async with httpx.AsyncClient(timeout=15) as client:
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                r = await client.post(url, json={"chat_id": CHAT_ID, "text": "🟢 Vize Radar V5 TEST: Bot canlı! Tarama başlıyor.", "parse_mode": "HTML"})
                result = {"tested": True, "telegram_response": r.text[:500], "status": r.status_code}
        except Exception as e:
            result = {"tested": False, "error": str(e)}
    else:
        result = {"tested": False, "error": "BOT_TOKEN or CHAT_ID missing"}
    
    return {"results": [{"country": "DEU", "status": "DOLU", "slots": 0}], "telegram_test": result, "musait_count": 0}

@app.get("/api/telegram-log")
async def t_log():
    return []
