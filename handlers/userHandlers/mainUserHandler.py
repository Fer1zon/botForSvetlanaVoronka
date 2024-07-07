from aiogram import types

from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State



import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from importantFiles.config import closedChatId




async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)



async def paySuccess(message:types.Message, state:FSMContext):
    
    await state.update_data(pay = "True")


    link = await bot.create_chat_invite_link(closedChatId, member_limit = 1)

    sendText = f"""
Благодарим за оплату!
Вот ваша ссылка на канал: {link.invite_link} . Она одноразовая, поэтому не давайте ее не кому другому!"""
    
    await message.answer(sendText)


















    

