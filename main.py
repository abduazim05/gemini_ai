import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

user_chats = {}

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Salom! savollaringiz bolsa yozing😊")

@dp.message()
async def chat_with_gemini(message: types.Message):
    user_id = message.from_user.id
    
    if user_id not in user_chats:
        user_chats[user_id] = model.start_chat()
    
    chat = user_chats[user_id]
    
    
    response = chat.send_message(message.text)
    
    
    await message.answer(response.text)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
