from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from asyncio import sleep

API_TOKEN = '' #write your token api 
bot = Bot(token=API_TOKEN) #bot
dp = Dispatcher(bot) #dispatcher

games_keyboard = ReplyKeyboardMarkup( #keyboard
    keyboard = [
        [
            KeyboardButton(text="Football ⚽️"),
            KeyboardButton(text="Basketball 🏀"),
        ],
        [
            KeyboardButton(text="Dice 🎲"),
            KeyboardButton(text="Bowling 🎳"),
        ]
    ],resize_keyboard=True
)

@dp.message_handler(text="/start") #start command
async def salam(message:types.Message):
    await message.answer(f"Assalomu Alaykum,{message.from_user.full_name}👤\nGame botga xush kelibsiz!📱\nO'yin tanlang🎮",reply_markup=games_keyboard)
    user_full_name = message.from_user.full_name
    user_id = message.from_user.id
    with open('users.txt','a') as file:
        file.write(f"Full name:{user_full_name}\nUser ID:{user_id}") #create user information notes 

@dp.message_handler(text="/help") #help command
async def yordam(message:types.Message):
    await message.answer(f"Yordam uchun:@Jaxa_dev")

@dp.message_handler(text="Dice 🎲") #dice game
async def football(message:types.Message):
    await message.answer("Narda o'yinni boshlaymiz!🎲\n")
    await sleep(2)
    await message.answer("Mening yurushim!")
    bot_data = await message.answer_dice()
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await message.answer("Sizning yurushingiz!")
    await sleep(2)
    user_data = await message.answer_dice()
    user_data = user_data['dice']['value']
    await sleep(5)
    if user_data > bot_data:
        await message.answer("Siz yutdingiz!\nTabriklayman🏆")
    elif user_data == bot_data:
        await message.answer("Durrang⚖️")
    elif bot_data > user_data:
        await message.answer("Men yutdim!🤖🦾")

@dp.message_handler(text="Football ⚽️") #football game
async def football(message:types.Message):
    await message.answer("Futbol o'yinni boshlaymiz!⚽️\n")
    await sleep(2)
    await message.answer("Mening yurushim!")
    bot_data = await message.answer_dice('⚽️')
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await message.answer("Sizning yurushingiz!")
    await sleep(2)
    user_data = await message.answer_dice('⚽️')
    user_data = user_data['dice']['value']
    await sleep(5)
    if user_data > bot_data:
        await message.answer("Siz yutdingiz!\nTabriklayman🏆")
    elif user_data == bot_data:
        await message.answer("Durrang⚖️")
    elif bot_data > user_data:
        await message.answer("Men yutdim!🤖🦾")

@dp.message_handler(text="Basketball 🏀") #basketball game
async def football(message:types.Message):
    await message.answer("Basketball o'yinni boshlaymiz!🏀\n")
    await sleep(2)
    await message.answer("Mening yurushim!")
    bot_data = await message.answer_dice('🏀')
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await message.answer("Sizning yurushingiz!")
    await sleep(2)
    user_data = await message.answer_dice('🏀')
    user_data = user_data['dice']['value']
    await sleep(5)
    if user_data > bot_data:
        await message.answer("Siz yutdingiz!\nTabriklayman🏆")
    elif user_data == bot_data:
        await message.answer("Durrang⚖️")
    elif bot_data > user_data:
        await message.answer("Men yutdim!🤖🦾")

@dp.message_handler(text="Bowling 🎳") #bowling game
async def football(message:types.Message):
    await message.answer("Bouling o'yinni boshlaymiz!🎳\n")
    await sleep(2)
    await message.answer("Mening yurushim!")
    bot_data = await message.answer_dice('🎳')
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await message.answer("Sizning yurushingiz!")
    await sleep(2)
    user_data = await message.answer_dice('🎳')
    user_data = user_data['dice']['value']
    await sleep(5)
    if user_data > bot_data:
        await message.answer("Siz yutdingiz!\nTabriklayman🏆")
    elif user_data == bot_data:
        await message.answer("Durrang⚖️")
    elif bot_data > user_data:
        await message.answer("Men yutdim!🤖🦾")

if __name__ == '__main__': #start bot
    executor.start_polling(dp, skip_updates=True)   
