from aiogram.dispatcher import Dispatcher

from aiogram.types import ContentTypes

import sys
import os


sys.path.append(os.path.dirname(__file__) + '/..')
from handlers.startBotHandlers.startBotHandlerAdmin import startBotHandlerAdmin
from handlers.startBotHandlers.startBotHandlerUser import startBotHandlerUser
from importantFiles.helps import States, dp,bot, cur,conn

from aiogram import types


from otherHandlers.mainOtherHandler import getPhotoId

from userHandlers.mainUserHandler import paySuccess, process_pre_checkout_query



from adminHandlers.mainAdminHandler import getImg, getText, responseMailing, startMailing

from importantFiles.config import adminId



def registerStartHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к началу пользования ботом
    dp.register_message_handler(startBotHandlerUser, lambda msg: msg.from_user.id not in adminId, commands="start")
    dp.register_message_handler(startBotHandlerAdmin,lambda msg: msg.from_user.id in adminId, commands="start")
    



def registerOtherHandler(dp:Dispatcher):#Регистратор хандлеров относящихся к прочему(Выходы, бэки и тп)
    #dp.register_message_handler(getPhotoId, content_types="photo", state = "*")
    pass


def registerUserHandler(dp:Dispatcher):#Регистрация юзерских хандлеров
    dp.register_message_handler(paySuccess, content_types = ContentTypes.SUCCESSFUL_PAYMENT)
    dp.register_pre_checkout_query_handler(process_pre_checkout_query, lambda query: True)
    




def registerAdminHandler(dp:Dispatcher):#Регистрация админ хандлеров
    dp.register_message_handler(startMailing, commands="start_mailing", state = States.ADMIN_MAILING)
    dp.register_message_handler(responseMailing, commands="mailing", state = States.ADMIN_MAIN_MENU)
    dp.register_message_handler(getImg, content_types="photo", state = States.ADMIN_MAILING)
    dp.register_message_handler(getText, content_types="text", state = States.ADMIN_MAILING)
    






def finalHandlerRegistrator(dp:Dispatcher):#Функция для регистрации всего, и дальнейшего его использования в launch.py
    registerStartHandler(dp)
    registerUserHandler(dp)
    registerAdminHandler(dp)
    registerOtherHandler(dp)