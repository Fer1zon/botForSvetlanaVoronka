
from aiogram import types

from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn








async def startBotHandlerAdmin(message : types.message, state:FSMContext):
    await state.reset_data()
    sendText = "/mailing - Для рассылки"

    await message.answer(sendText)

    await States.ADMIN_MAIN_MENU.set()