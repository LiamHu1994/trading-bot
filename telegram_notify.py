import requests
import json

with open("config.json", "r") as f:
    config = json.load(f)

def send_telegram_message(message):
    token = config["telegram_token"]
    chat_id = config["telegram_chat_id"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, json=data)
    except Exception as e:
        print("Telegram error:", e)