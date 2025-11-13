from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Any, Dict, Optional

app = FastAPI(title="AI Agent", version="1.0.0")

class ExecuteRequest(BaseModel):
    query: str = Field(..., description="User request")
    params: Optional[Dict[str, Any]] = None

class ExecuteResponse(BaseModel):
    answer: str
    sources: list = []
    tools: list = []
    latency_ms: int = 0

@app.get("/health/alive")
async def alive():
    return {"status": "alive"}

@app.get("/health/ready")
async def ready():
    return {"status": "ready"}

@app.post("/execute", response_model=ExecuteResponse)
async def execute(req: ExecuteRequest):
    try:
        # demo echo
        return ExecuteResponse(
            answer=f"OK: received query='{req.query}'",
            sources=[], tools=[], latency_ms=1
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
