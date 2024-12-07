#!/usr/bin/env python3
"""_summary_
    This file contains functions for the github checker endpoint
"""

from fastapi import FastAPI, Request
import hmac
import hashlib

class Github_check:
    app = FastAPI()

    def __init__(self, repo, token = None):
        self.repo = []
        self.events_last_ids = [0] * len(repo)
        self.token = token

    async def check_signature(self, request):
        if self.token is None:
            return "No signature", 400
        signature = request.headers.get('X-Hub-Signature-256')
        sha, signature = signature.split('=')
        if sha != "sha256":
            return "Bad signature", 400
        payload = request.get_data()
        hmac_ = hmac.new(self.token.encode(), payload, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(hmac_.hexdigest(), signature):
            return "Invalide signature", 403
        return hmac_

    @app.post("/github_check") # put this in endpoints routes
    async def check_github(self, request: Request):
        """_summary_
            The endpoint allowing a user to check if there was a push in the selected repositorie.
        Returns:
            Response: _description_: The data to send back to the user as a response.
        """
        # get repo list from user, user must be able to stock repo list in db
        self.repo = ["https://api.github.com/repos/bazar-de-komi/terarea/events"]
        signature = self.get_signature(request)
        if not signature:
            return {"error": "Invalid signature"}

        event = request.headers.get('X-GitHub-Event', 'ping')
        if event == "push":
            data = await request.json()
            print(f"Received push event on repo: {data['repository']['full_name']}")
            return {"message": "Push event received", "repository": data['repository']['full_name']}
        elif event == "ping":
            return {"message": "Ping received!"}
        return {"message": "Event not supported"}
