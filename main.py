from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='5170745477:AAFZEplB-mXBovnRFfpqW7LHwJATbZ-862o')

dp = Dispatcher(bot)

@dp.message_handler()
async  def get_message(message: types.Message):
    # chat_id = message.chat.id
    # text = 'Hello мир!'
    # sent_message = await bot.send_message(chat_id=chat_id, text = text)
    # print(sent_message.to_python())

    # sent_message = await bot.send_photo(chat_id=384405346, photo='https://images.firma-gamma.ru/images/f/0/d76088708684l.jpg')
    # print(sent_message.photo[-1].file_unique_id)

    executor.start_polling(dp)
