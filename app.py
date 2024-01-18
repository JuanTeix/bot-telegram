import requests
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import time

load_dotenv()
# Configuración de la API de YouTube
youtube_api_key = os.environ['YOUTUBE_API_KEY']
youtube_channel_id = os.environ['YOUTUBE_CHANNEL_ID']
youtube_api_service_name = 'youtube'
youtube_api_version = 'v3'

# Configuración de la API de Telegram
telegram_bot_token = os.environ['TELEGRAN_TOKEN_BOT']
telegram_chat_id = os.environ['TELEGRAN_CHAT_ID']

# Crea un cliente de API de YouTube
youtube_client = build(youtube_api_service_name, youtube_api_version, developerKey=youtube_api_key)

def get_latest_video_id():
    request = youtube_client.search().list(part='id', channelId=youtube_channel_id, order='date', maxResults=1)
    response = request.execute()
    return response['items'][0]['id']['videoId']

def send_telegram_message(video_id):
    message = f"Nuevo video en el canal: https://www.youtube.com/watch?v={video_id}"
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_chat_id}&text={message}"
    requests.get(url)

def main():
    last_video_id = None
    while True:
        try:
            current_video_id = get_latest_video_id()
            if current_video_id != last_video_id:
                send_telegram_message(current_video_id)
                last_video_id = current_video_id
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(3600)  # Espera 1 hora antes de comprobar de nuevo

if __name__ == "__main__":
    main()
