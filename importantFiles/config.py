import os

from dotenv import load_dotenv

load_dotenv()

from aiogram.types import LabeledPrice

TOKEN = os.environ['TOKEN']
TEST_TOKEN = os.environ.get('TEST_TOKEN')

TEST_PAY_TOKEN = os.environ.get('TEST_PAY_TOKEN')
PAY_TOKEN = os.environ['PAY_TOKEN']

closedChatId = -1002217820802

adminId = [5530562487, 386843844]


SERVICE_PRICE = LabeledPrice(label = "Оплата доступа", amount = 5555 * 100)

dataBasePath = os.path.dirname(__file__) + '/dataBase/data_base.db'