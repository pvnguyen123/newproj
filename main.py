from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set")

supabase: Client = create_client(supabase_url, supabase_key)


class MessageCreate(BaseModel):
    content: str


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI on Railway! take two"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/messages")
async def get_messages():
    result = supabase.table("messages").select("*").order("created_at", desc=True).execute()
    return result.data


@app.post("/messages", status_code=201)
async def create_message(body: MessageCreate):
    result = supabase.table("messages").insert({"content": body.content}).execute()
    return result.data[0]
