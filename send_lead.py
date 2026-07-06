from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    name = data.get('name', '')
    contact = data.get('contact', '')
    service = data.get('service', '')
    message = data.get('message', '')

    text = (
        f"🔔 Новая заявка с сайта!\n\n"
        f"👤 Имя: {name}\n"
        f"📞 Контакт: {contact}\n"
        f"🛠 Услуга: {service}\n"
        f"💬 Сообщение: {message}"
    )

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": ADMIN_ID, "text": text}
    )

    return jsonify({"ok": True})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
