from aiogram import types

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State



import sys 
import os 
from pathlib import Path
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from appShedulerFunc.Sample import sendMessageAfter2minutes, scheduler, sendMessageAfter3Hours

from datetime import datetime, timedelta






async def startBotHandlerUser(message : types.Message):
    if cur.execute("SELECT * FROM users WHERE id = ?", (message.from_user.id,)).fetchone() is None:
        cur.execute("INSERT INTO users VALUES(?, ?)", (message.from_user.id, message.from_user.username))
        conn.commit()


    sendPhoto = "AgACAgIAAxkBAAMEZogk5rdeu5Xgvk2erRl1alJhir4AAmrcMRv9KEBIfdip4J7IxE8BAAMCAAN5AAM1BA"
    sendText = """
Привет, это Света Бабаблог)
Начнем с главного: 
⠀
Без лишних слов хочу сразу предложить тебе увеличить продажи от 2 до 10 раз🤘, внедрив всего один инструмент креативного маркетинга для себя или своих клиентов.
⠀
🔥 Только представь...
⠀
— Влюбляешь клиентов в продукт или услугу с первого взгляда.
— Получаешь фанатов бренда, которые скупают все товары.
— Реклама становится в разы дешевле, бренд обрастает виральным охватом. 

И это подходит для любых бизнесов: как для продажи товаров в офлайне и в онлайне, продажи услуг, а также для личных брендов. ⠀
Звучит слишком круто и слабо верится, да?

Дай мне пару минут и я докажу тебе, что это реально 👇🏻
"""

    sendKb = InlineKeyboardMarkup().add(InlineKeyboardButton("Смотреть видео", url = "https://vk.com"))

    await message.answer_photo(caption=sendText, photo = sendPhoto, reply_markup=sendKb)

    
    scheduler.add_job(sendMessageAfter2minutes, trigger="date", run_date = datetime.now() + timedelta(seconds=15), args=[message.from_user.id, bot])
    #scheduler.add_job(sendMessageAfter2minutes, trigger="date", run_date = datetime.now() + timedelta(minutes=2), args=[message.from_user.id, bot])

    scheduler.add_job(sendMessageAfter3Hours, trigger="date", run_date = datetime.now() + timedelta(seconds=180), args=[message.from_user.id, bot])
    # scheduler.add_job(sendMessageAfter3Hours, trigger="date", run_date = datetime.now() + timedelta(hours = 3), args=[message.from_user.id, bot])

    

    