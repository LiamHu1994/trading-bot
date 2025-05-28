# Binance 自動下單機器人（主網版）

## 使用方式
1. 安裝套件
```bash
pip install -r requirements.txt
```

2. 啟動 webhook 接收器
```bash
python webhook_receiver.py
```

3. TradingView 設定 webhook：
網址填入：
```
http://你的伺服器IP:5000/webhook
```

內容：
```json
{ "side": "buy" }
或
{ "side": "sell" }
```