from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import IDFilter, ChatTypeFilter



async def resending_message(message: types.Message):
    if message.photo:
        await message.bot.send_photo(chat_id=-1001989276198, photo=message.photo[-1].file_id, caption=message.text)        
    elif message.document:
        await message.bot.send_document(chat_id=-1001989276198, document=message.document.file_id, caption=message.text)
    elif message.text:
        await message.bot.send_message(-1001989276198, text=message.text)


def register_resend_message_handlers(dp: Dispatcher) -> None:
    dp.register_channel_post_handler(resending_message, content_types=[types.ContentType.PHOTO, types.ContentType.DOCUMENT, types.ContentType.TEXT])
    dp.register_message_handler(resending_message, content_types=[types.ContentType.PHOTO, types.ContentType.DOCUMENT, types.ContentType.TEXT])
