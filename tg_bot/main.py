import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from handler import router
import os
from dotenv import load_dotenv
load_dotenv()


async def main() -> None:
    TOKEN = os.getenv('TOKEN')

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(router)

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
