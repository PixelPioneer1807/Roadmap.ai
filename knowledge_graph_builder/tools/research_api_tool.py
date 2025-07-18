import os
import requests

class PatchedEuriClient:
    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model
        self.api_url = "https://api.euron.one/api/v1/euri/chat/completions"

    def generate_completion(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post(self.api_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

EURI_CLIENT = PatchedEuriClient(
    api_key=os.getenv("EURI_API_KEY"),
    model="gpt-4.1-nano"
)
