from aiogram import Bot, Dispatcher, executor, types

bot = Bot("6513613001:AAHZZ4GtQwRXpctL7L_KHasq1QRToDX-UY8")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Hi')

executor.start_polling(dp)