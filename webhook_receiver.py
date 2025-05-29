from flask import Flask, request
from order_executor import execute_order
from telegram_notify import send_telegram_message

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # ✅ 測試用訊息，會在任何訊號進來時通知 Telegram
    from telegram_notify import send_telegram_message
    send_telegram_message(f"[Webhook] Signal received: {data}")


    if data:
        send_telegram_message(f"📩 收到訊號：{data}")
        execute_order(data)
        return 'Order Executed', 200
    return 'No data received', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
send_telegram_message(f"[Webhook] Signal received: {data}")
