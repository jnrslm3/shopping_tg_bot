import asyncio
from aiogram import Bot, Dispatcher
from databases.models import *
import sys, logging
from config import TOKEN
from commands.command import command_router
from databases.models import create_tables
from databases.querysets import *
from commands.admin import admin_router
# from scrap.parsing import * 

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(command_router, admin_router)
    await dp.start_polling(bot)

    # await create_tables()
    # await add_product()





if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())