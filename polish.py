import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

# Встав свій токен від BotFather
TELEGRAM_BOT_TOKEN = "7967420653:AAH-6PM5sdr-ghERx7TyaoacD0ZfDhgFzyE"

# Ініціалізація бота та диспетчера
bot = Bot(7967420653:AAH-6PM5sdr-ghERx7TyaoacD0ZfDhgFzyE)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    await message.answer("Cześć! Я твій віртуальний вчитель польської мови. Ось кілька корисних команд:\n/help - Довідка\n/word - Слово дня")

@dp.message_handler(commands=['help'])
async def help_command(message: Message):
    await message.answer("Я можу допомогти тобі вивчати польську!\n/word - Отримати слово дня\n/grammar - Граматичне правило")

@dp.message_handler(commands=['word'])
async def word_of_the_day(message: Message):
    words = ["kot - кіт", "pies - пес", "dom - будинок", "szkoła - школа", "nauczyciel - вчитель"]
    await message.answer(f"Слово дня: {random.choice(words)}")

@dp.message_handler(commands=['grammar'])
async def grammar_rule(message: Message):
    rules = ["В польській мові є три роди: чоловічий, жіночий, середній.",
             "Дієслова змінюються за особами та числами.",
             "У польській мові 7 відмінків, як в українській."]
    await message.answer(f"Граматичне правило: {random.choice(rules)}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
