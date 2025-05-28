import ccxt
import json
from telegram_notify import send_telegram_message

with open('config.json', 'r') as f:
    config = json.load(f)

exchange = ccxt.binance({
    'apiKey': config['api_key'],
    'secret': config['api_secret'],
    'enableRateLimit': True,
    'options': {'defaultType': 'future'}
})

def execute_order(data):
    try:
        side = data.get("side")
        symbol = config["symbol"]
        amount = config["amount"]
        leverage = config["leverage"]

        exchange.fapiPrivate_post_leverage({'symbol': symbol.replace("/", ""), 'leverage': leverage})

        if side == "buy":
            order = exchange.create_market_buy_order(symbol, amount)
        elif side == "sell":
            order = exchange.create_market_sell_order(symbol, amount)
        else:
            send_telegram_message(f"⚠️ 無效交易方向: {side}")
            return

        msg = f"✅ 下單成功: {side.upper()}\n交易對: {symbol}\n數量: {amount}"
        send_telegram_message(msg)
        print("Order placed:", order)

    except Exception as e:
        send_telegram_message(f"❌ 下單失敗: {str(e)}")
        print("Order error:", e)