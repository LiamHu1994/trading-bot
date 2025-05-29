from flask import Flask, request
from telegram_notify import send_telegram_message
from order_executor import execute_order  # 若你有自定下單邏輯可加上

app = Flask(__name__)

@app.route('/')
def index():
    return '🚀 Trading Bot is running.'

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        print(f"Webhook received: {data}")

        # ✅ 發送 Telegram 通知
        send_telegram_message(f"[Webhook] Signal received:\n{data}")

        # ✅ 若有 side 指令，可進一步處理
        side = data.get("side", "").lower()
        if side in ["buy", "sell"]:
            execute_order(side)  # ⚠️ 這行僅當你已寫好下單邏輯
            return {"status": "order executed"}, 200
        else:
            return {"status": "invalid signal"}, 400

    except Exception as e:
        send_telegram_message(f"❌ Webhook Error:\n{str(e)}")
        return {"error": str(e)}, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
