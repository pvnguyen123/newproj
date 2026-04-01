from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI on Railway!"}


@app.get("/health")
async def health():
    return {"status": "ok"}
