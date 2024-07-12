
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
<b>Видео-разбор продаж товаров на 3 млн+ с помощью креативного маркетинга доступен на ссылке ниже</b> ⬇️ 

За 2 года тестов креативного маркетинга в своем бизнесе я накопила много практического опыта. Привлекла более 5000 тысяч клиентов в свои магазины, сделала 9-значные обороты 
проекта, хакнула систему маркетинга в продаже товаров и услуг. 

🎥 Весь этот опыт я упаковала в видео-разбор. В нем за 11 минут я даю выжимку с примерами того, что сработало именно у меня. 

Пока урок доступен в бесплатном формате, советую перейти к просмотру 👇🏻
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
<b>3х дневный Интенсив по креативному маркетингу</b> со скидкой 72%

<b>1й день:</b>
✨Какие креативные эффекты помогут увеличить выручку бизнеса в 2-10 раз?

<b>2й день:</b>
✨Как придумывать креативные идеи? Пошаговая инструкция для креативных и не очень.
✨3 упражнения для развития креативности из британской системы образования. Выходим за рамки. 

<b>3й день:</b>
✨Сколько стоит креативная реклама? Считаем затраты и эффективность.
✨Где искать подрядчиков и как делегировать создание креативной рекламы.

<b>Бонус:</b>
🎁 50 идей креативного маркетинга, которые можно внедрить уже сегодня с небольшим бюджетом, и как адаптировать идеи под свой бизнес.
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
<b>А я предупреждала…</b>

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
<b>Топ-5 фишек креативного маркетинга</b>, которые в разы подняли наши продажи, и вы можете внедрить их у себя:

<b>Фишка №1.</b>
✔️Привлечь внимание с первых секунд
У меня сработал яркий необычный вид промоутеров/стендов/роликов. То, что люди не ожидают увидеть, и замечают среди прочего рекламного шума.

<b>Фишка №2.</b>
✔️ Давать действительно выгодный оффер, который будет ограничен по времени. 
Людям должно быть не только красиво, но и выгодно. Избегайте клише типа «прикоснись к прекрасному» и «окунись в атмосферу стиля и красоты». У клиента должна быть причина прийти и купить сейчас, а ваш оффер должен быть как выигрыш в лотерею - самый желанный. 

<b>✔️Фишка №3.</b>
Вызывать эмоции.
Флаер или коммикс, от которого хочется улыбнуться или елка, вокруг которой летает снег, создающая wow-эффект. 
Когда реклама вызывает у человека восторг, смех, радость, она запоминается. 

<b>✔️Фишка №4.</b>
Выделяться среди остальных. 
Например, наша необычная елка привлекла не только своей яркостью, но и динамикой с разлетающимся снегом, вокруг обычных елок других брендов. Достаточно сделать на 10% лучше остальных, чтобы получить в разы больше клиентов. 

<b>✔️Фишка №5.</b>
Думать о пользователе. 
Делая упаковку для своих товаров, мы помним об удобстве, чтобы покупатель сохранил ее, а не хотел выкинуть. И натыкаясь взглядом на пакет или шопер с нашим брендингом дома, клиент вспоминает про наш магазин. 

Мне нравится, как креативный маркетинг работает в моем бизнесе.
Сейчас на рынке минимум конкуренции, потому что большинство брендов делают одно и тоже, повышают ставки за клиентов, показывая им однотипный контент и рекламу. Креативный маркетинг используют менее 1% брендов, и я предлагаю быть вам в их числе, и захватить внимание аудитории. 

<b>Внедряйте и масштабируйте свои результаты🔥</b>

Приглашаю вас на 3х дневный Интенсив по созданию креативного контента и рекламы:
На интенсиве мы разберем 50 креативных идей, которые вы можете внедрить для своего бизнеса уже сегодня с небольшими бюджетами. 🔽


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

<b>У меня есть еще кое-что интересное...</b>

В своем телеграм-канале я выкладываю посты про креативный маркетинг, тесты и факапы, разборы классных креативных идей и новые тренды.

Подписывайся: https://t.me/babablog


"""

    # sendKb = InlineKeyboardMarkup().add(InlineKeyboardButton("Оплатить интенсив", callback_data= "Купить"))

    await bot.send_message(chat_id=chat_id, text=sendText)
    








async def sendPayInvoice(chat_id, bot:Bot, textInButton:str):
    sendKb = InlineKeyboardMarkup().add(InlineKeyboardButton(textInButton, pay=True))
    await bot.send_invoice(
    chat_id,
    title="Оплата доступа",
    description="Оплати доступ к интенсиву и переходи в закрытый телеграм-канал",
    provider_token=TEST_PAY_TOKEN,
    currency='rub',
    is_flexible=False,  # True если конечная цена зависит от способа доставки
    prices=[SERVICE_PRICE],
    start_parameter='service-pay',
    payload='some-invoice-payload-for-our-internal-use',
    reply_markup=sendKb
)


async def kickUser(user_id, channelId, bot:Bot):
    await bot.kick_chat_member(chat_id=channelId, user_id=user_id)
    
