from aiogram.types import InlineKeyboardButton
from aiogram import Bot, Dispatcher, types


keyboard1 = types.InlineKeyboardMarkup()
start_button = types.InlineKeyboardButton(text="Начать/Start", callback_data="st.start")
keyboard1.add(start_button)

sell = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton(text="Plati.Market", callback_data="mr.PM")
button2 = types.InlineKeyboardButton(text="GGSel.net", callback_data="mr.GGS")
button3 = types.InlineKeyboardButton(text="WMCentre.net", callback_data="mr.WMC")
sell.add(button1, button2, button3)

lang = types.InlineKeyboardMarkup()
ru = types.InlineKeyboardButton(text="РУССКИЙ🇷🇺️", callback_data="l.ru")
en = types.InlineKeyboardButton(text="ENGLISH🇬🇧️", callback_data="l.en")
lang.add(ru, en)

ok = types.InlineKeyboardMarkup()
ok_bt = types.InlineKeyboardButton(text="Согласен/Agree", callback_data="k.ok")
ok.add(ok_bt)

ok1 = types.InlineKeyboardMarkup()
ok_bt1 = types.InlineKeyboardButton(text="Согласен/Agree", callback_data="k.ok1")
ok1.add(ok_bt1)

okk2 = types.InlineKeyboardMarkup()
okk_bt2 = types.InlineKeyboardButton(text="Согласен/Agree", callback_data="ko.ok2")
okk2.add(okk_bt2)

okk3 = types.InlineKeyboardMarkup()
okk_bt3 = types.InlineKeyboardButton(text="Согласен/Agree", callback_data="ko.ok3")
okk3.add(okk_bt3)

go = types.InlineKeyboardMarkup()
go_bt = types.InlineKeyboardButton(text="Согласен/Agree", url="https://t.me/+4_jNFwiqEMc5MWMy")
go.add(go_bt)
