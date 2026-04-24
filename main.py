# =============================================================================
# main.py
# Pravaha Test — FastAPI Hello World
# Used to test the Pravaha Python deployment pipeline
# =============================================================================

from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Pravaha FastAPI Test",
    description="Testing Pravaha Python deployment pipeline"
)

@app.get("/")
def root():
    return {
        "message":   "🌊 Namaste from Pravaha!",
        "platform":  "Pravaha — Rooted in wisdom. Engineered to flow.",
        "language":  "Python / FastAPI",
        "timestamp": datetime.utcnow().isoformat(),
        "status":    "deployed successfully"
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "pravaha-fastapi-test"}
