
# YouTube to Telegram Bot

## Descripción
Este bot de Python está diseñado para monitorear un canal específico de YouTube y enviar una notificación a un grupo de Telegram cada vez que se publica un nuevo video. Utiliza la API de YouTube Data v3 para obtener información sobre los videos más recientes y la API de Bot de Telegram para enviar mensajes.

## Funcionalidades
- Monitoreo automático de canales de YouTube.
- Notificaciones en tiempo real en Telegram cuando se sube un nuevo video.
- Fácil de configurar y personalizar para cualquier canal de YouTube y grupo de Telegram.

## Requisitos Previos
- Python 3.x
- Paquetes de Python: `requests`, `google-api-python-client` ,`dotenv`, `os`, `time`
- Clave de API de Google con acceso a la YouTube Data API v3
- Token de Bot de Telegram

## Instalación
1. Clona este repositorio.
   ```bash
   git clone https://github.com/JuanTeix/bot-telegram.git
   ```
2. Instala las dependencias necesarias.
   ```bash
   pip install -r requirements.txt
   ```
3. Crea archivo .env y define las variables de entorno
   YOUTUBE_API_KEY
   YOUTUBE_CHANNEL_ID
   TELEGRAN_TOKEN_BOT
   TELEGRAN_CHAT_ID
   

## Configuración
1. Abre `app.py` y rellena las siguientes variables:
   - `youtube_api_key`: Tu clave de API de Google.
   - `youtube_channel_id`: El ID del canal de YouTube que quieres monitorear.
   - `telegram_bot_token`: El token de tu bot de Telegram.
   - `telegram_chat_id`: El ID del chat de tu grupo de Telegram.
2. Guarda los cambios en `app.py`.

## Uso en local
Ejecuta el bot con el siguiente comando:
```bash
python main.py
```

## Uso en Docker
Ejecuta el bot con el siguiente comando:
```bash
docker build --tag jteixbot . 
docker run --rm jteixbot
```

El bot comenzará a monitorear el canal de YouTube especificado y enviará un mensaje a tu grupo de Telegram cada vez que se detecte un nuevo video.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, por favor haz un fork del repositorio y realiza tus cambios. Luego, envía un pull request para su revisión.

## Licencia
[MIT](https://opensource.org/licenses/MIT)

## Créditos
Desarrollado con ❤️ por JTeixCode 😊
