import hmac
import hashlib
from fastapi import Request, HTTPException
from config import GITHUB_WEBHOOK_SECRET

async def verify_github_signature(request: Request):
    signature = request.headers.get("X-Hub-Signature-256")
    if signature is None:
        raise HTTPException(status_code=400, detail="Missing signature")

    body = await request.body()
    mac = hmac.new(GITHUB_WEBHOOK_SECRET.encode(), body, hashlib.sha256)
    expected_signature = "sha256=" + mac.hexdigest()
    if not hmac.compare_digest(expected_signature, signature):
        raise HTTPException(status_code=401, detail="Invalid signature")
