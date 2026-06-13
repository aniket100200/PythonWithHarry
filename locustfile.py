from locust import HttpUser, task, between, events
import os
import uuid
import json
import random
from locust.exception import StopUser

# Config via environment variables (change as needed)
API_HOST = os.getenv("API_HOST", "")         # e.g. "https://your.api.host" (you can also pass --host to locust)
API_PATH = os.getenv("API_PATH", "/chat.postMessage")  # endpoint path, default matches your Java example
API_TOKEN = os.getenv("API_TOKEN", "")       # Bearer token used by getUserToken(...) in your system
CHANNEL = os.getenv("CHANNEL", "general")    # channel to post to
USER = os.getenv("USER", "testuser")         # optional, not used in header but for logging
SCHEMA = os.getenv("SCHEMA", "default")      # optional metadata
# Optional: set a bot username to simulate the Java logic that adds username when available
BOT_NAME = os.getenv("BOT_NAME", None)

# Some sample messages to pick randomly
SAMPLE_MESSAGES = [
    "Hello from load test!",
    "Automated test message",
    "Performance test ping",
    "Injected message for conversation.postpublic",
    "Locust user message " + str(uuid.uuid4())[:8]
]

class ChatUser(HttpUser):
    # wait time between tasks (random)
    wait_time = between(0.5, 2.0)  # seconds between tasks for each simulated user

    @task
    def post_message(self):
        """
        Simulate sending a message similar to your Java postMessage2 method:
        JSON body: { text, channel, client_msg_id, username? }
        Authorization: Bearer <API_TOKEN>
        """
        if not API_TOKEN:
            # If token not provided, stop the user and print a clear message.
            # Locust will show an error.
            raise StopUser("API_TOKEN not set - set env var API_TOKEN before running Locust")

        client_uuid = str(uuid.uuid4())
        text = random.choice(SAMPLE_MESSAGES)

        payload = {
            "text": text,
            "channel": CHANNEL,
            "client_msg_id": client_uuid
        }

        # add username if configured (mirrors your Java method's optional username)
        if BOT_NAME:
            payload["username"] = BOT_NAME

        headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json",
            # optional: pass USER/SCHEMA as custom headers if your API expects them
            "X-Test-User": USER,
            "X-Test-Schema": SCHEMA
        }

        # If host passed via --host flag, use relative path. Otherwise, API_HOST env can specify full host.
        url = API_PATH
        if API_HOST:
            # if API_HOST ends with / and API_PATH starts with /, remove duplicate slash
            url = (API_HOST.rstrip("/") + "/" + API_PATH.lstrip("/"))

        with self.client.post(url, data=json.dumps(payload), headers=headers, catch_response=True) as resp:
            # replicate Java behavior: throw/flag when response contains "error"
            text_resp = ""
            try:
                text_resp = resp.text or ""
            except Exception:
                text_resp = ""

            if "error" in text_resp.lower():
                resp.failure(f"API returned error: {text_resp}")
            elif resp.status_code >= 400:
                resp.failure(f"HTTP {resp.status_code}: {text_resp}")
            else:
                resp.success()

# Optional: print helpful message when starting Locust headlessly to remind env vars
@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("Starting Locust test. Config:")
    print(f"  API_HOST = {API_HOST or '(use --host to pass host)'}")
    print(f"  API_PATH = {API_PATH}")
    print(f"  CHANNEL = {CHANNEL}")
    print(f"  USER = {USER}")
    print(f"  SCHEMA = {SCHEMA}")
    print(f"  BOT_NAME = {BOT_NAME}")
    if not API_TOKEN:
        print("WARNING: API_TOKEN is not set. The test will stop immediately.")
