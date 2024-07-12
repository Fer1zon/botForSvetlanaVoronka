from aiogram import types

from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State



import sys 
import os 
sys.path.append(os.path.dirname(__file__) + '/..')
from importantFiles.helps import States, dp,bot, cur,conn

from asyncio import sleep




async def responseMailing(message:types.Message, state:FSMContext):
    await state.update_data(text = "", img = "")

    sendText = """
Отправьте в чат фото и текст, после наполнения рассылки используйте команду /start_mailing
Текст без фото не должен превышать 4096 символов
Текст с фото не должен превышать 1024 символа"""

    await message.answer(sendText)

    await States.ADMIN_MAILING.set()



async def getImg(message:types.Message, state:FSMContext):
    img = message.photo[-1].file_id
    async with state.proxy() as data:
        text = data["text"]
        data["img"] = img


    sendText = "Итоговое сообщение👇"

    if text == "":
        await message.answer(sendText)
        await message.answer_photo(img)

    elif len(text) > 1024:
        await message.answer("Текст с фотографией не должен превышать 1024 символа")
        await state.update_data(text = "")

    else:
        await message.answer(sendText)
        await message.answer_photo(img, caption=text)


async def getText(message:types.Message, state:FSMContext):
    text = message.text
    async with state.proxy() as data:
        img = data["img"]

    sendText = "Итоговое сообщение👇"
    if img != "" and len(text) > 1024: 
        await message.answer("Текст с фотографией не должен превышать 1024 символа")

    elif len(text) > 4096:
        await message.answer("Текст без фото не должен превышать 4096 символов")
    
    elif img == "":
        await state.update_data(text = text)
        await message.answer(sendText)
        await message.answer(text)

    else:
        await state.update_data(text = text)
        await message.answer(sendText)
        await message.answer_photo(img, caption=text)



async def startMailing(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        text = data["text"]
        img = data["img"]

    if text == "" and img == "":
        return await message.answer("Вы не задали не текста, не фото")
    
    sendText = "Рассылка начата, бот сообщит когда она закончиться"
    await message.answer(sendText)
    await States.ADMIN_MAIN_MENU.set()
    await state.reset_data()

    count = 0

    for dataId in cur.execute("SELECT id FROM users"):


        userId = dataId[0]
        if img != "" and text != "":
            await bot.send_photo(userId, img, caption=text)

        elif img != "" and text == "":
            await bot.send_photo(userId, img)

        elif img == "" and text != "":
            await bot.send_message(userId, text)

        if count == 5:
            count = 0
            await sleep(5)
            continue

    await message.answer("Рассылка окончена!")


        




        
        














