import os

from dotenv import load_dotenv

load_dotenv()

from aiogram.types import LabeledPrice

TOKEN = os.environ['TOKEN']
TEST_TOKEN = os.environ['TEST_TOKEN']

TEST_PAY_TOKEN = os.environ['TEST_PAY_TOKEN']
PAY_TOKEN = os.environ['PAY_TOKEN']

closedChatId = -1002143556313

adminId = [5530562487]


SERVICE_PRICE = LabeledPrice(label = "Оплата доступа", amount = 900 * 100)

dataBasePath = os.path.dirname(__file__) + '/dataBase/data_base.db'