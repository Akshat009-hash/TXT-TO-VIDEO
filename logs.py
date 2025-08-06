# Don't Remove Credit Tg - @spidy_bots
import logging
import requests

# Configure the logging
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Telegram Bot Token and Channel ID
TELEGRAM_BOT_TOKEN = '8127956088:AAFxffMamwVs8O3AW2k_yHbedy3rvJK8whQ'
TELEGRAM_CHANNEL_ID = '1002623740817'  # or use channel ID

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHANNEL_ID,
        'text': message
    }
    requests.post(url, json=payload)

def log_info(message):
    logging.info(message)
    send_telegram_message(message)

def log_warning(message):
    logging.warning(message)
    send_telegram_message(message)

def log_error(message):
    logging.error(message)
    send_telegram_message(message)

def log_debug(message):
    logging.debug(message)
    send_telegram_message(message)

if __name__ == "__main__":
    log_info("This is an info message.")
    log_warning("This is a warning message.")
    log_error("This is an error message.")
    log_debug("This is a debug message.")
