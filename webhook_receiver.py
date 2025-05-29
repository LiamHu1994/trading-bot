from flask import Flask, request
import requests
import json
import os

# === 使用者設定（已寫死）===
API_KEY = "GeQa83eNuad2JB5mAO8u5S2wbNSV90E7YT9JaPvWuYcwIuQlcXMgWEOMLtzOR66l"
API_SECRET = "1aeeXUWUdv3tsWoDonVhRGH8DgJLQXHucZTl42E2YqgGyEdhUbEiKEak5JQlBLpz"
TG_TOKEN = "7760664257:AAGuJe4_jnKgAc3CzmAbWwqQWXdDJOhsmYA"
TG_CHAT_ID = "7661326054"

# === Telegram 發送訊息 ===
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    payload = {"chat_id": TG_CHAT_ID, "text": message}
    headers = {"Content-Type": "application/json"}
    try:
        res = requests.post(url, data=json.dumps(payload), headers=headers)
        print("✅ Telegram 發送成功")
        print("Response:", res.text)
    except Exception as e:
        print(f"❌ Telegram 發送失敗: {e}")

# === Flask App ===
app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Webhook bot is running.'

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        print(f"📨 收到 Webhook: {data}")
        send_telegram_message(f"📨 Webhook 訊號:\n{data}")
        return {'status': 'ok'}, 200
    except Exception as e:
        print(f"❌ webhook 錯誤: {e}")
        send_telegram_message(f"❌ Webhook 錯誤:\n{e}")
        return {'error': str(e)}, 500

@app.route('/test')
def test():
    data = {"side": "buy"}
    print("🧪 測試 webhook")
    send_telegram_message(f"🧪 測試訊號: {data}")
    return {'status': 'test sent'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
