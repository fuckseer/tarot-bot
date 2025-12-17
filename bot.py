import asyncio
import os
from dotenv import load_dotenv  # <--- Импорт

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from agent import graph_app
from logger import logger

load_dotenv()

TOKEN = os.getenv("TG_BOT_TOKEN")

if not TOKEN:
    logger.error("❌ ОШИБКА: Токен TG_BOT_TOKEN не найден! Проверь файл .env")
    exit(1)

dp = Dispatcher()
bot = Bot(token=TOKEN)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🔮 Я Финансовый Таролог.\n"
        "Спроси меня про курс крипты, попроси конвертировать монеты или просто попроси знак судьбы"
    )


@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    text = message.text

    logger.info(f"📩 USER MSG [{user_id}]: {text}")

    config = {"configurable": {"thread_id": str(user_id)}}

    try:
        input_msg = {"messages": [("user", text)]}
        final_state = graph_app.invoke(input_msg, config=config)

        bot_answer = final_state["messages"][-1].content
        await message.answer(bot_answer)

    except Exception as e:
        logger.error(f"❌ ERROR: {e}")
        await message.answer("Туман войны скрыл ответ (ошибка).")


async def main():
    logger.info("🚀 Бот запускается...")
    os.makedirs("data", exist_ok=True)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())