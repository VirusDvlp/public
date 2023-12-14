from aiogram import executor

from handlers import register_all_handlers
from create_bot import dp


async def on_startup(dp):
    register_all_handlers(dp)


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
