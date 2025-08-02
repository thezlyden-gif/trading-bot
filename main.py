import requests
import time

bot_token = "8392693204:AAEDJvZhNvukxx4nnYDRZYrFyUo8PkQqIr8"
chat_id = "AZMAT_CHAT_ID"  # Замени на свой числовой chat_id

def send_message(text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

if __name__ == "__main__":
    send_message("🤖 Бот запущен и работает на Render 24/7!")
    while True:
        # Можно вставить сюда любые торговые функции или обновления
        time.sleep(3600)  # Пинг раз в час, чтобы бот не засыпал
        send_message("✅ Бот всё ещё работает!")
