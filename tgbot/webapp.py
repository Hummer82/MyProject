from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot("6513613001:AAHZZ4GtQwRXpctL7L_KHasq1QRToDX-UY8")
dp = Dispatcher(bot)

@dp.message_handler(commands=['web'])
async def website(message: types.Message):
    await message.answer(f'{message}')

@dp.message_handler(commands=['start','menu'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton('Открыть сайт', web_app=WebAppInfo(url='https://rc44.ru')))
    markup.add(types.KeyboardButton('Написать менеджеру', callback_data='send_manager'))
    markup.add(types.KeyboardButton('Создать заказ',  callback_data='create_order'))
    markup.add(types.KeyboardButton('Вход', callback_data='login'))
    fn = message.chat.first_name if message.chat.first_name != None else ""
    ln = message.chat.last_name if message.chat.last_name != None else ""
    await message.answer(f'{fn} {ln}, выберите действие',reply_markup=markup)

@dp.callback_query_handler()
async def sendmanager(call):
    if call.data == 'send_manager':
        myid = call.message['from']['id']
        await bot.send_message(6039681226,f'От: {myid}\n text', reply_to_message_id=myid)
    else:
        await call.message.answer(call)
    
@dp.message_handler(content_types=['text','photo','video','voice'])
async def mess(message: types.Message):
    reply_id = message.reply_to_message['from']['id']
    await bot.send_message(reply_id,'ooh')
    # if int(message.reply_to_message['from']['id']) != int(message['from']['id']):
    #     await bot.send_message(message.reply_to_message['from']['id'], message.text)
    # else:
    #     await message.answer(message)


executor.start_polling(dp)