from bot.handler import Handler
import json
import bot.database_client


class Dispatcher:
    def __init__(self):
        self._handlers: list[Handler] = []

    def add_handler(self, *handlers: list[Handler]) -> None:
        for handler in handlers:
            self._handlers.append(handler)

    def _get_telegram_id_from_update(self, update: dict) -> int | None:
        if "message" in update:
            return update["message"]["from"]["id"]
        elif "callback_query" in update:
            return update["callback_query"]["from"]["id"]
        return None

    def dispatch(self, update: dict) -> None:
        for handler in self._handlers:
            if handler.can_handle(update):
                signal = handler.handle(update)
                if not signal:
                    break