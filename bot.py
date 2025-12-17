import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from agent import graph_app
from logger import logger

TOKEN = os.getenv("TG_BOT_TOKEN")

dp = Dispatcher()
bot = Bot(token=TOKEN)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🔮 Приветствую. Я Финансовый Таролог.\n\n"
        "Мои инструменты:\n"
        "1. 📈 Узнать курс (Bitcoin, TON...)\n"
        "2. 🧮 Посчитать прибыль (Конвертер)\n"
        "3. 🎲 Спросить судьбу (Бросок кубика)\n\n"
        "Что тебя тревожит?"
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
        await message.answer("Духи возмущены (произошла ошибка сервера).")


async def main():
    logger.info("🚀 Бот запускается...")
    os.makedirs("data", exist_ok=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())