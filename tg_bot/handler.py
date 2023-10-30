from aiogram.filters import Filter
from aiogram import Bot, Router
from aiogram.enums import ContentType
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


class MyFilter(Filter):
    def __init__(self, content) -> None:
        self.my_content = content

    async def __call__(self, message: Message) -> bool:
        return message.content_type == self.my_content


@router.message(CommandStart())
async def new_chat_delete(message: Message):
    await message.answer("<b>Привет!</b>\n"
                         "Данный бот выполняет функцию по удалению системных сообщений\n"
                         "Для использования добавьте этого бота в чат, и предоставьте ему права администратора")


@router.message(MyFilter(ContentType.NEW_CHAT_MEMBERS))
async def new_chat_delete(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


@router.message(MyFilter(ContentType.LEFT_CHAT_MEMBER))
async def left_chat_delete(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


@router.message(MyFilter(ContentType.DELETE_CHAT_PHOTO))
async def delete_chat_photo(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


@router.message(MyFilter(ContentType.NEW_CHAT_PHOTO))
async def new_chat_photo(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


@router.message(MyFilter(ContentType.NEW_CHAT_TITLE))
async def new_chat_title(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
