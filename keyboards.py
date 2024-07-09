from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(
        KeyboardButton('Узнать погоду'),
    )

    return keyboard   #Функция создания клавиатуры


def get_inline_keyboard() -> InlineKeyboardMarkup:
    inl_keyboard = InlineKeyboardMarkup(row_width=2)
    inl_keyboard.add(
        InlineKeyboardButton('Да', callback_data='kb_plus'),
        InlineKeyboardButton('Добавить расходы', callback_data='kb_minus'),
    )

    return inl_keyboard   #Функция создания инлайн клавиатуры