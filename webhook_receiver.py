from flask import Flask, request
import json
import requests

# === Telegram config ===
TELEGRAM_TOKEN = "你的 BOT TOKEN"
TELEGRAM_CHAT_ID = "你的 CHAT ID"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    headers = {"Content-Type": "application/json"}
    try:
        requests.post(url, data=json.dumps(payload), headers=headers)
    except Exception as e:
        print(f"❌ Failed to send Telegram message: {e}")

# === Flask app ===
app = Flask(__name__)

@app.route('/')
def index():
    return '✅ Bot is running.'

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        print(f"📨 Webhook received: {data}")
        send_telegram_message(f"📨 Webhook Received:\n{data}")
        return {'status': 'ok'}, 200
    except Exception as e:
        send_telegram_message(f"❌ Error in webhook:\n{str(e)}")
        return {'error': str(e)}, 500

@app.route('/test')
def test():
    data = {"side": "buy"}
    print(f"🧪 Test webhook triggered: {data}")
    send_telegram_message(f"🧪 Test Trigger:\n{data}")
    return {"status": "test buy sent"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
