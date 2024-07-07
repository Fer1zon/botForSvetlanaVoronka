
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from aiogram import Bot

from aiogram.dispatcher import FSMContext

from importantFiles.helps import dp

from asyncio import sleep


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


from importantFiles.config import TEST_PAY_TOKEN, PAY_TOKEN, SERVICE_PRICE






scheduler = AsyncIOScheduler()





async def sendMessageAfter2minutes(chat_id, bot:Bot):
    
    
    sendPhoto = "AgACAgIAAxkBAAMGZogl_W0XU4TFQ6V3LYu9y6qM_EoAAnPcMRv9KEBIQ2BOdoDlz4YBAAMCAAN5AAM1BA"
    sendText = """
Ты тут? 

Хочу поделиться с тобой материалами, в которых расскажу, как я продаю товары на 3+ млн за короткий срок с помощью креативного маркетинга, а также как и зачем креативный маркетинг применяют мировые бренды на огромных масштабах. 

В следующей статье мы разберем 3 креативных инструмента на примере крупных брендов, и как их применять в своем бизнесе. 

❗️Но сначала попрошу ознакомиться с правилами.
1. Чтобы получать контент нужно сразу жать на все кнопки и не затягивать. 
Если ты этого не сделаешь, тебе придет напоминалка. Проигноришь и её, твой доступ к контенту сгорит, а тебя перекинет на следующий этап без права восстановления.
2. Не забираешь контент больше суток — все сгорает.

☝️ Так что не зевай. Ибо за этим контентом стоит много миллионов моей выручки, и тонна ошибок, которых ты можешь избежать.
"""

    sendKb = InlineKeyboardMarkup().add(InlineKeyboardButton("Забрать статью", url = "https://vk.com"))

    await bot.send_photo(chat_id=chat_id, caption=sendText, photo=sendPhoto, reply_markup=sendKb)

    scheduler.add_job(sendMessageAfter3Minutes, trigger="date", run_date = datetime.now() + timedelta(seconds=20), args=[chat_id, bot])



    
    # scheduler.add_job(sendMessageAfter3Minutes, trigger="date", run_date = datetime.now() + timedelta(minutes=3))



async def sendMessageAfter3Minutes(chat_id, bot:Bot):
    sendPhoto = "AgACAgIAAxkBAAMXZogo1ebNewkTNRfofzNDBZgjwiUAAofcMRv9KEBIUW125H1HK3wBAAMCAAN5AAM1BA"
    sendText = """
ВИДЕО РАЗБОР МОИХ ПРОДАЖ ТОВАРОВ НА 3млн+ С ПОМОЩЬЮ КРЕАТИВНОГО МАРКЕТИНГА ДОСТУПЕН ПО ССЫЛКЕ НИЖЕ ⬇️ 

За 2 года тестов креативного маркетинга в своем бизнесе я накопила много практического опыта. 
Привлекла более 5000 тысяч клиентов в свои магазины, сделала 9-значные обороты проекта, хакнула систему маркетинга в продаже товаров и услуг. 

Весь этот опыт я упаковала в видео-обзор. В нем за 11 минут я даю выжимку с примерами того, что сработало именно у меня. 

Пока урок доступен в бесплатном формате, советую перейти к просмотру 👇🏻
"""

    sendKb = InlineKeyboardMarkup().add(InlineKeyboardButton("Смотреть видео", url = "https://vk.com"))

    await bot.send_photo(chat_id=chat_id, caption=sendText, photo=sendPhoto, reply_markup=sendKb)

    # scheduler.add_job(sendMessageAfter10Minutes, trigger="date", run_date = datetime.now() + timedelta(minutes=10), args=[chat_id, bot])
    scheduler.add_job(sendMessageAfter10Minutes, trigger="date", run_date = datetime.now() + timedelta(seconds=40), args=[chat_id, bot])



async def sendMessageAfter10Minutes(chat_id, bot:Bot):
    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    await state.update_data(pay = "False")

    sendPhoto = "AgACAgIAAxkBAAMZZoguy5Dhd73blHIFBKCqZRgAAaEpAAKp3DEb_ShASGXJc0FJ9JWyAQADAgADeQADNQQ"
    sendText = """
3х дневный Интенсив по креативному маркетингу со скидкой 72%
1й день:
Какие креативные эффекты помогут увеличить выручку бизнеса в 2-10 раз?
2й день:
Как придумывать креативные идеи? Пошаговая инструкция для креативных и не очень.
3 упражнения для развития креативности из британской системы образования. Выходим за рамки. 

3й день:
Сколько стоит креативная реклама? Считаем затраты и эффективность.

Где искать подрядчиков и как делегировать создание креативной рекламы.

Бонус:
50 идей креативного маркетинга, которые можно внедрить уже сегодня с небольшим бюджетом (презентация), и как адаптировать идеи под свой бизнес. 
"""

    # sendKb = InlineKeyboardMarkup().add(InlineKeyboardButton("Купить интенсив", callback_data = "Купить"))

    await bot.send_photo(chat_id=chat_id, caption=sendText, photo=sendPhoto)
    

    

    # scheduler.add_job(sendMessageAfter3Minutes2, trigger="date", run_date = datetime.now() + timedelta(minutes=3), args = [chat_id, bot])
    scheduler.add_job(sendMessageAfter3Minutes2, trigger="date", run_date = datetime.now() + timedelta(seconds = 30), args = [chat_id, bot])

    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    data = await state.get_data()
    if data["pay"] == "False":
        await sendPayInvoice(chat_id, bot , textInButton="Купить интенсив")





async def checkPay(chat_id, bot:Bot):
    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    data = await state.get_data()
    if data["pay"] == "True":
        return

    sendPhoto = "AgACAgIAAxkBAAMbZogwDFKV0EBiLVAYKihpttLdjsgAArTcMRv9KEBILIe3exJ9AZMBAAMCAAN5AAM1BA"
    sendText = """
Спишь?

Тебе пора идти к следующим материалам, иначе все сгорит, и плакали твои миллионы. 
"""

    # sendKb = InlineKeyboardMarkup().add(InlineKeyboardButton("Оплатить интенсив", callback_data= "Купить"))

    await bot.send_photo(chat_id=chat_id, caption=sendText, photo=sendPhoto)
    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    data = await state.get_data()
    if data["pay"] == "False":
        await sendPayInvoice(chat_id, bot , textInButton="Оплатить интенсив")

    # await sleep(60 * 3)
    await sleep(30)

    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    data = await state.get_data()
    if data["pay"] == "True":
        return
    

    sendPhoto = "AgACAgIAAxkBAAMdZogwxP9z1JvwWd9FxjN4--dUFxoAArncMRv9KEBIkQNp6CECO6YBAAMCAAN5AAM1BA"
    sendText = """
А я предупреждала…

Последний шанс изучить материалы и ворваться в 1% успешных предпринимателей, которые уже внедрили креативный маркетинг.
Через год может быть уже поздно, ну ты знаешь, это как подписчики с рекламы по 10 рублей. Никогда не будет дешевле и эффективнее начать, чем прямо сейчас… 

"""

    
    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    data = await state.get_data()
    await bot.send_photo(chat_id=chat_id, caption=sendText, photo=sendPhoto)
    if data["pay"] == "False":
        await sendPayInvoice(chat_id, bot , textInButton="Срочно забрать материалы")




async def sendMessageAfter3Minutes2(chat_id, bot:Bot):
    sendText = """
Топ-5 фишек креативного маркетинга, которые в разы подняли наши продажи, и вы можете внедрить их у себя:

Фишка №1.
✔️Привлечь внимание с первых секунд
У меня сработал яркий необычный вид промоутеров/стендов/роликов. То, что люди не ожидают увидеть, и замечают среди прочего рекламного шума.

Фишка №2.
✔️ Давать действительно выгодный оффер, который будет ограничен по времени. 
Людям должно быть не только красиво, но и выгодно. Избегайте клише типа «прикоснись к прекрасному» и «окунись в атмосферу стиля и красоты». У клиента должна быть причина прийти и купить сейчас, а ваш оффер должен быть как выигрыш в лотерею - самый желанный. 

✔️Фишка №3.
Вызывать эмоции.
Флаер или коммикс, от которого хочется улыбнуться или елка, вокруг которой летает снег, создающая wow-эффект. 
Когда реклама вызывает у человека восторг, смех, радость, она запоминается. 

✔️Фишка №4.
Выделяться среди остальных. 
Например, наша необычная елка привлекла не только своей яркостью, но и динамикой с разлетающимся снегом, вокруг обычных елок других брендов. Достаточно сделать на 10% лучше остальных, чтобы получить в разы больше клиентов. 

✔️Фишка №5.
Думать о пользователе. 
Делая упаковку для своих товаров, мы помним об удобстве, чтобы покупатель сохранил ее, а не хотел выкинуть. И натыкаясь взглядом на пакет или шопер с нашим брендингом дома, клиент вспоминает про наш магазин. 

Мне нравится, как креативный маркетинг работает в моем бизнесе.
Сейчас на рынке минимум конкуренции, потому что большинство брендов делают одно и тоже, повышают ставки за клиентов, показывая им однотипный контент и рекламу. Креативный маркетинг используют менее 1% брендов, и я предлагаю быть вам в их числе, и захватить внимание аудитории. 

Внедряйте и масштабируйте свои результаты🔥

Приглашаю вас на 3х дневный Интенсив по созданию креативного контента и рекламы:
На интенсиве мы разберем 50 креативных идей, которые вы можете внедрить для своего бизнеса уже сегодня с небольшими бюджетами. 


"""

    # sendKb = InlineKeyboardMarkup().add(InlineKeyboardButton("Оплатить интенсив", callback_data= "Купить"))

    await bot.send_message(chat_id=chat_id, text=sendText)

    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    data = await state.get_data()
    if data["pay"] == "False":
        await sendPayInvoice(chat_id, bot , textInButton="Оплатить интенсив")

    # scheduler.add_job(checkPay, trigger="date", run_date = datetime.now() + timedelta(minutes=5))
    scheduler.add_job(checkPay, trigger="date", run_date = datetime.now() + timedelta(seconds=30), args=[chat_id, bot])






async def sendMessageAfter3Hours(chat_id, bot:Bot):
    state: FSMContext = dp.current_state(chat=chat_id, user=chat_id)
    data = await state.get_data()
    if data["pay"] == "True":
        return
    
    sendText = """
Спасибо, что дошел(а) до конца. 

У меня есть еще кое-что интересное...

В своем телеграм-канале я выкладываю посты про креативный маркетинг в моем бизнесе, тесты и факапы, разборы классных креативный идей и новые тренды.

Подписывайся: https://t.me/babablog


"""

    # sendKb = InlineKeyboardMarkup().add(InlineKeyboardButton("Оплатить интенсив", callback_data= "Купить"))

    await bot.send_message(chat_id=chat_id, text=sendText)
    








async def sendPayInvoice(chat_id, bot:Bot, textInButton:str):
    sendKb = InlineKeyboardMarkup().add(InlineKeyboardButton(textInButton, pay=True))
    await bot.send_invoice(
    chat_id,
    title="Оплата доступа",
    description="Оплати доступ в закрытый телеграмм канал на всегда!",
    provider_token=TEST_PAY_TOKEN,
    currency='rub',
    is_flexible=False,  # True если конечная цена зависит от способа доставки
    prices=[SERVICE_PRICE],
    start_parameter='service-pay',
    payload='some-invoice-payload-for-our-internal-use',
    reply_markup=sendKb
)
