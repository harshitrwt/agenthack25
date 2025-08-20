from fastapi import FastAPI
from routers import incidents, issues

app = FastAPI(title="AI Incident Agent")

app.include_router(incidents.router, prefix="/webhook", tags=["incidents"])
app.include_router(issues.router, prefix="/webhook", tags=["issues"])

@app.get("/")
def root():
    return {"message": "Sentinel Bot is running!"}

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
