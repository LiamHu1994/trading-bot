from flask import Flask, request
from order_executor import execute_order

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data:
        execute_order(data)
        return 'Order Executed', 200
    return 'No data received', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)