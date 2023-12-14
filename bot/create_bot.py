from os import getenv

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv


load_dotenv()


TOKEN = "6985821840:AAFoYIVkSxOUyiLvUNi_voDw0UdxrDKuEKo"

bot = Bot(TOKEN)
dp = Dispatcher(bot)
