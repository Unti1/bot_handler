from settings import *
from .buttons import *
from .correct_mail import *
from .States import *

API_TOKEN = config['Telegram']['token']
bot = Bot(token=API_TOKEN)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Jpg
file_list = ['data\\1.jpg', 'data\\2.jpg', 'data\\3.jpg', 'data\\4.jpg', 'data\\5.jpg', 'data\\6.jpg', 'data\\7.jpg', 'data\\8.jpg', 'data\\9.jpg', ]
res_data = []
for file in file_list:
    with open(file, 'rb') as fl:
        res_data.append(fl.read())


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_photo(
        message.chat.id, res_data[0],
        "🇷🇺️ Уважаемый {0.first_name} ❗\n"
        "Внимательно читайте и делайте что вам пишут, и проблем не будет.\n"
        "Нажми НАЧАТЬ  на кнопке снизу👇️и мы начнем\n"
        "--------------------------------------\n"
        "🇬🇧️ Dear {0.first_name} ❗\n"
        "Read carefully and do what they write to you, and there will be no "
        "problems.\n"
        "Click the START button on the bottom 👇️ and we will begin\n"
        .format(message.from_user), reply_markup=keyboard1)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_photo(
        message.chat.id, res_data[0],
        "🇷🇺️ Уважаемый {0.first_name} ❗\n"
        "Внимательно читайте и делайте что вам пишут, и проблем не будет.\n"
        "Нажми НАЧАТЬ  на кнопке снизу👇️и мы начнем\n"
        "--------------------------------------\n"
        "🇬🇧️ Dear {0.first_name} ❗\n"
        "Read carefully and do what they write to you, and there will be no "
        "problems.\n"
        "Click the START button on the bottom 👇️ and we will begin\n"
        .format(message.from_user), reply_markup=keyboard1)
    await bot.delete_message(message.from_user.id, message.message.message_id)


@dp.callback_query_handler(lambda call: call.data == 'st.start')
async def mail_entry(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        res_data[1],
        "🇷🇺️ Напишите ПОЧТУ с которой вы покупали\n"
        "(которую вы вводили при покупке)👇️\n"
        "-----------------------------\n"
        "🇬🇧️ Write the MAIL with which you bought\n"
        "(which you entered when purchasing)👇️")

    await Form.mail.set()

@dp.message_handler(state=Form.mail)
async def mail_handler(message: types.Message, state: FSMContext):
    email = message.text
    if is_valid_email(email):

        async with state.proxy() as data:
            data['mail'] = message.text

        await bot.send_photo(
            message.chat.id, res_data[2],
            "🇷🇺️Напишите название ИГРЫ которую приобрели👇\n"
            "️---------------------------------\n"
            "🇬🇧️Write the name of the GAME you purchased👇️")
        await Form.next()
        print(email, "- mail")
    else:
        await bot.send_message(message.chat.id,
                         "Вас разве это попросили сделать⁉️")


@dp.message_handler(state=Form.game)
async def game_handler(message: types.Message, state: FSMContext):
    game = message.text
    await bot.send_photo(message.chat.id, res_data[3],
                   "🇷🇺️Выберите площадку на которой приобретали ИГРУ👇️\n"
                   "---------------------------------\n"
                   "🇬🇧️Select the site where you purchased the GAME👇️\n", reply_markup=sell)
    print(game, "- game")

    await state.finish()


@dp.callback_query_handler(text_contains='mr.')
async def Shops(call):
    if call.data == "mr.PM":
        print("Plati.Market")
    elif call.data == "mr.GGS":
        print("GGSel.net")
    elif call.data == "mr.WMC":
        print("WMCentre.net")
    await bot.send_photo(call.message.chat.id, res_data[4],
                   "🇷🇺️ Передача аккаунта третьим лицам строго ЗАПРЕЩЕНА, \n"
                   "влечет за собой ограничение на дальнейшие покупки и доступ в аккаунт\n"
                   "-------------------------------------------------------------\n"
                   "🇬🇧️ Transferring an account to third parties is strictly FORBIDDEN, \n"
                   "entails a restriction on further purchases and access to the account"
                   .format(call.message.from_user), reply_markup=ok)
    print("-----------------------------")


@dp.callback_query_handler(text_contains='k.')
async def okey(call):
    username = call.message.chat.username
    if call.data == "k.ok":
        await bot.send_photo(call.message.chat.id, res_data[5],
                       "🇷🇺Если вы купили с другом и вам попался одинаковый, не \n"
                       "паникуйте, напишете АДМИНУ и вам дадут другой аккаунт 👭️\n"
                       "------------------------------------------------\n"
                       "🇬🇧️If you bought with a friend and you got the same one, don't \n"
                       "panic, write to ADMIN and you will be given another account 👭️"
                       .format(call.message.from_user), reply_markup=ok1)


    elif call.data == "k.ok1":
        await bot.send_photo(call.message.chat.id, res_data[6],
                       username + " На каком языке продолжить⁉️\n"
                       "\n"
                       + username + " In which language to continue⁉️"
                       .format(call.message.from_user), reply_markup=lang)


@dp.callback_query_handler(text_contains='l.')
async def okey(call):
    if call.data == "l.ru":
        await bot.send_photo(call.message.chat.id, res_data[7],
                       "Если у вас возникнет проблема или появится вопрос, то не\n"
                       "нужно суетиться и кидаться в панику, там в ЧАТ-БОТЕ куда будут\n"
                       "приходить коды будет кнопка " + " ПОМОЩЬ " + ", вы обязательно\n"
                       "найдете свой ответ на вопрос или свяжетесь с АДМИНОМ, и\n"
                       "вам обязательно ответят и помогут, или заменят, или дадут \n"
                       "другой.\n"
                       "\n"
                       "И не начинайте с негатива😉️\n"
                       .format(call.message.from_user), reply_markup=okk2)

    elif call.data == "l.en":
        await bot.send_photo(call.message.chat.id, res_data[7],
                       "If you have a problem or a question, then there is no need to fuss\n"
                       "and panic, there in the CHAT-BOT where the codes will come there\n"
                       "will be a " + " HELP " + " button, you will definitely find your answer to the\n"
                       "question or contact the ADMIN, and they will definitely answer you\n"
                       "and help, or replace, or give another.\n"
                       "\n"
                       "And don't start with the negative😉️\n"
                       .format(call.message.from_user), reply_markup=okk3)


@dp.callback_query_handler(text_contains='ko.')
async def okkey(call):
    username = call.message.chat.username
    if call.data == "ko.ok3":
        await bot.send_photo(call.message.chat.id, res_data[8],
                       "Thank you very much " + username + "for doing everything right👍️❗️\n"
                       "Press the " + "GO" + " button👇️ you will be taken to the BOTA where \n"
                       "only CODES come, you do not need to enter anything there, you \n"
                       "enter the login and password in STEAM itself, as above in the \n"
                       "picture, and the CODE will come to the BOTA. After the transition,\n"
                       "click RUN (at the bottom of the screen).\n"
                       "And do not forget about the " + "HELP" + "button,"
                       " press it when you need it and they will help you. Good luck❗️️\n"
                       .format(call.message.from_user), reply_markup=go)

    elif call.data == "ko.ok2":
        await bot.send_photo(call.message.chat.id, res_data[8],
                       "Спасибо большое " + username + ", что все сделали правильно👍️❗️\n"
                       "Нажимайте на кнопку" + "ПЕРЕЙТИ" + "👇️ вы попадете в БОТА куда\n"
                       "приходят только КОДЫ, вводить туда ничего не нужно, логин и \n"
                       "пароль вы вводите в сам STEAM, как выше на картинке, а в \n"
                       "БОТА придет КОД. После перехода нажмите ЗАПУСТИТЬ (внизу экрана)\n"
                       "И не забывайте про кнопку" + "ПОМОЩЬ" + ", нажмёте её когда вам она"
                       "понадобится и вам помогут. Удачи❗️\n"
                       .format(call.message.from_user), reply_markup=go)

@dp.message_handler(content_types='text')
async def error(message: types.Message):
    await bot.send_message(
        message.chat.id,
        "Вас разве это попросили сделать⁉️")