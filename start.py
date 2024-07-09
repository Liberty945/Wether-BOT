from handlers import *
from aiogram import executor
from SUandSD import on_shutdown, on_startup

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown,
                           )                            #функция запуска БОТа