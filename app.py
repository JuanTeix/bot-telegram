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
telegram_chat_id_priv = os.environ['TELGRAM_CHAT_PRIV']

# Crea un cliente de API de YouTube
youtube_client = build(youtube_api_service_name, youtube_api_version, developerKey=youtube_api_key)

def get_latest_video_info():
    try:
        # Realiza la solicitud a la API de YouTube para obtener el video más reciente
        request = youtube_client.search().list(
            part='snippet', 
            channelId=youtube_channel_id, 
            order='date', 
            maxResults=1,
            type='video'
        )
        response = request.execute()

        # Agrega impresiones de depuración para ver la respuesta
        # print("Respuesta de la API:", response)

        # Obtiene el ID y el título del video
        video_id = response['items'][0]['id']['videoId']
        video_title = response['items'][0]['snippet']['title']

        return video_id, video_title
    except Exception as e:
        print(f"Error al obtener la información del video: {e}")
        return None, None

def send_telegram_message(video_id, video_title, chat):
    # Si chat = 1 envia mensaje al grupo publico
    if chat == 1:
        message = f"Nuevo video en el canal \n {video_title} \n https://www.youtube.com/watch?v={video_id}"
    # Si chat = 0 envia mensaje al grupo privado
    elif chat == 0:
        message = "Bot Activo"
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_chat_id_priv}&text={message}"
    requests.get(url)


def main():
    send_telegram_message("","",0)
    last_video_id = None
    while True:
        try:
            current_video_id, current_video_title = get_latest_video_info()
            if current_video_id != last_video_id:
                send_telegram_message( current_video_id, current_video_title, 1)
                last_video_id = current_video_id
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(3600)  # Espera 1 hora antes de comprobar de nuevo

if __name__ == "__main__":
    
    main()
