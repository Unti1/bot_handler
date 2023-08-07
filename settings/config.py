# Для бота
from aiogram import *
from aiogram.types import InlineKeyboardButton
from aiogram.dispatcher import Dispatcher
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor

# Стандарт
import re
import configparser

settings_file = "settings"
config = configparser.ConfigParser()
config.read('settings/settings.ini')


def config_update():
    with open(settings_file, 'w') as fl:
        config.write(fl)
    config.read(settings_file)