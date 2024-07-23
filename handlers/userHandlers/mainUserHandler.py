from aiogram import types

from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from datetime import datetime, timedelta


import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from importantFiles.config import closedChatId

from appShedulerFunc.Sample import kickUser, scheduler

from importantFiles.config import closedChatId




async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)



async def paySuccess(message:types.Message, state:FSMContext):
    
    await state.update_data(pay = "True")


    link = await bot.create_chat_invite_link(closedChatId, member_limit = 1)

    sendText = f"""
Благодарим за оплату!
Вот ваша ссылка на канал: {link.invite_link} . Она одноразовая, поэтому не давайте ее никому другому!"""
    
    await message.answer(sendText)

    scheduler.add_job(kickUser, "date", run_date = datetime.now() + timedelta(days=61), args=[message.from_user.id, closedChatId, bot])
    #scheduler.add_job(kickUser, "date", run_date = datetime.now() + timedelta(seconds=30), args=[message.from_user.id, closedChatId, bot])






















    

