from bot.handler import Handler
import bot.telegram_client


class MessagePhotoEcho(Handler):
    def can_handle(self, update: dict) -> bool:
        return ("message" in update and 
                "photo" in update["message"])

    def handle(self, update: dict) -> bool:
        photos = update["message"]["photo"]
        largest_photo = max(photos, key=lambda x: x["file_size"])
        file_id = largest_photo["file_id"]
        
        bot.telegram_client.sendPhoto(
            chat_id=update["message"]["chat"]["id"],
            photo=file_id
        )
        return False