import random
from langchain_core.tools import tool
from logger import logger


@tool
def get_crypto_price(coin: str) -> str:
    """
    Узнать текущую цену криптовалюты (bitcoin, eth, ton и т.д.) в USD.
    Принимает название монеты.
    """
    logger.info(f"🔧 TOOL CALL: [get_crypto_price] для монеты '{coin}'")

    prices = {
        "bitcoin": "64,300",
        "ethereum": "3,450",
        "ton": "7.2",
        "notcoin": "0.02"
    }
    price = prices.get(coin.lower())

    if price:
        res = f"Карты показывают, что {coin} стоит ${price}"
    else:
        res = f"Туман скрывает цену {coin} (нет данных)."

    logger.info(f"✅ TOOL RESULT: {res}")
    return res


@tool
def currency_calculator(amount: float, rate: float) -> str:
    """
    Перевести одну валюту в другую.
    Принимает сумму (amount) и курс (rate).
    Используй это, чтобы посчитать итоговую стоимость.
    """
    logger.info(f"🔧 TOOL CALL: [currency_calculator] {amount} * {rate}")

    total = amount * rate
    res = f"Итог: {total:.2f}. Не потрать все сразу."

    logger.info(f"✅ TOOL RESULT: {res}")
    return res


@tool
def fate_dice(query: str) -> str:
    """
    Бросить кость судьбы (d20), чтобы принять решение.
    Используй это, если пользователь просит совета, знака свыше или не знает, что делать.
    """
    logger.info(f"🔧 TOOL CALL: [fate_dice] Вопрос: '{query}'")

    roll = random.randint(1, 20)
    if roll == 1:
        res = "💀 1: Полный крах. Даже не думай."
    elif roll == 20:
        res = "🌟 20: Абсолютный успех! Вселенная благоволит."
    elif roll > 10:
        res = f"🎲 {roll}: Скорее да, чем нет."
    else:
        res = f"🎲 {roll}: Скорее нет. Опасно."

    logger.info(f"✅ TOOL RESULT: {res}")
    return res


tools_list = [get_crypto_price, currency_calculator, fate_dice]