from telebot import types
def language():
    kb = types.InlineKeyboardMarkup(row_width=2)
    ru = types.InlineKeyboardButton(text="ru",callback_data="ru")
    uz = types.InlineKeyboardButton(text="uz",callback_data="uz")
    kb.add(ru,uz)
    return kb
def num():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    num = types.KeyboardButton("Отправить свой номер",request_contact=True)
    kb.add(num)
    return kb
def loc():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    loc = types.KeyboardButton("Отправить свою геолокацию",request_location=True)
    kb.add(loc)
    return kb