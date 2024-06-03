from dataclasses import dataclass
import os
os.environ['BOT_TOKEN'] = '6700083729:AAGQ8UPYOi3HB4mIpyB7t9c3_KsWYlw8tic' # не скрыто в учебных целях

@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    return Config(tg_bot=TgBot(token=os.environ.get('BOT_TOKEN')))