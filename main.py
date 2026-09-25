from main_real_scanner import app
# Railway entry point
if __name__ == "__main__":
    import uvicorn, os
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
