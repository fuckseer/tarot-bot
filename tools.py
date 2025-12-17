import random
import requests
from langchain_core.tools import tool
from logger import logger


@tool
def get_crypto_price(coin: str) -> str:
    """
    ПОЛУЧИТЬ КУРС В РЕАЛЬНОМ ВРЕМЕНИ.
    Вызывать ВСЕГДА, когда упоминается криптовалюта (bitcoin, btc, ton, eth...),
    даже если цена уже упоминалась в чате ранее.
    Цены меняются мгновенно, старые данные использовать нельзя.
    """
    coin_clean = coin.lower().strip()
    logger.info(f"🔧 TOOL CALL: [get_crypto_price] запрос к API для '{coin_clean}'")

    try:
        url = "https://api.coinlore.net/api/tickers/?start=0&limit=100"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return "Духи интернета блокируют связь (Ошибка API CoinLore)."

        data = response.json()
        coins_list = data.get("data", [])

        found_item = None

        for item in coins_list:
            if (item['symbol'].lower() == coin_clean or
                    item['name'].lower() == coin_clean or
                    item['nameid'] == coin_clean):
                found_item = item
                break

        if found_item:
            name = found_item['name']
            symbol = found_item['symbol']
            price = found_item['price_usd']
            change_24h = found_item['percent_change_24h']

            res = (f"💰 {name} ({symbol}): ${price}\n"
                   f"📊 Изменение за 24ч: {change_24h}%")
        else:
            res = f"Карты не видят монету '{coin}' в топ-100 рынка."

    except Exception as e:
        res = f"Произошла мистическая ошибка сети: {e}"

    logger.info(f"✅ TOOL RESULT: {res}")
    return res


@tool
def currency_calculator(amount: float, rate: float) -> str:
    """
    Перевести одну валюту в другую.
    Принимает сумму (amount) и курс (rate).
    Используй это, чтобы посчитать итоговую стоимость, когда знаешь курс.
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