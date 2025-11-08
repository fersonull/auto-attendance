import os
import dotenv
import requests

class DiscordWebhook:
    def __init__(self):
        dotenv.load_dotenv()
        self.webhook_url = os.getenv("WEBHOOK_URL")

    def send(self, content):
        data = {
            "content": content
        }

        try:
            response = requests.post(self.webhook_url, json=data)

            if response.status_code == 204:
                return True
        except requests.RequestException as e:
            return False
