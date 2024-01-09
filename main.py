import telebot, database as db, buttons as bt
from geopy import Nominatim
bot = telebot.TeleBot('6839367065:AAFokYIndQs1NhcHMxalHVsVDn8RSjI8xRs')
geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id,"Добро пожаловать,выберите язык",reply_markup=bt.language())
    if message.text == "ru":
       bot.register_next_step_handler(message,ru)
    else:
        pass
def ru(message):
    user_id = message.from_user.id
    check = db.checker(user_id)
    if check:
        bot.send_message(user_id, f'Добро пожаловать, {message.from_user.first_name}!',
                         reply_markup=bot.inline_handlers)
    else:
        bot.send_message(user_id, "Здравствуйте, добро пожаловать!\n Давайте начнем "
                                  "регистрацию!")
        # Переход на этап получения имени
        bot.register_next_step_handler(message, get_name)
def get_name(message):
    user_id = message.from_user.id
    bot.send_message(user_id,"Напиши свое имя:")
    name = message.text
    bot.register_next_step_handler(message,num,name)
def num(message,name):
    user_id = message.from_user.id
    bot.send_message(user_id,"Замечательно,а теперь свой номер:",reply_markup=bt.num())
    if message.contact:
        number = message.contact.phone_number
        bot.send_message(user_id, 'Супер! Последний этап: отправь локацию',
                         reply_markup=bt.loc())
        # Этап получения локации
        bot.register_next_step_handler(message,loc, name, number)
    # Если юзер отправил номер не по кнопке
    else:
        bot.send_message(user_id, 'Отправьте номер через кнопку',
                         reply_markup=bt.num())
        # Этап получения номера
        bot.register_next_step_handler(message,num, name)
def loc(message,name,number):
    user_id = message.from_user.id
    if message.location:
        location = str(geolocator.reverse(f'{message.location.latitude}, '
                                      f'{message.location.longitude}'))
        db.register( user_id,name, number, location)
        db.register(user_id, name, number, location)
        bot.send_message(user_id, 'Регистрация прошла успешно')

    # Если юзер отправил локацию не по кнопке
    else:
        bot.send_message(user_id, 'Отправьте локацию через кнопку',
                         reply_markup=bt.loc())
        # Этап получения номера
        bot.register_next_step_handler(message, loc, name, number)
bot.polling(non_stop=True)