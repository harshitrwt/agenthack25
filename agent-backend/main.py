from fastapi import FastAPI
from routers import ingest, ci

app = FastAPI(title="AI Incident Agent")

# Routers
app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
app.include_router(ci.router, prefix="/webhook", tags=["ci"])

@app.get("/")
def root():
    return {"message": "AI Incident Agent is running"}
