# 🔮 Crypto Tarot Bot (AI Agent)

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker)
![LangGraph](https://img.shields.io/badge/AI-LangGraph-orange?style=for-the-badge)
![Telegram](https://img.shields.io/badge/Bot-Aiogram-2CA5E0?style=for-the-badge&logo=telegram)

🌍 **Language / Язык / 语言:**
[🇺🇸 English](#-english) | [🇨🇳 中文 (Chinese)](#-中文-chinese) | [🇷🇺 Русский](#-русский)

---

## 🇺🇸 English

**Crypto Tarot Bot** is a smart AI agent that combines dry financial data with Tarot mysticism. The bot doesn't just answer questions; it "thinks," selects appropriate tools, and remembers the dialogue context.

> **Key Feature:** The bot uses **LangGraph** architecture for dialogue state management and **Function Calling** for decision-making.

### 🛠 Tools
The agent autonomously decides which tool to use based on the user's request:

1.  📈 **Crypto Price Tracker** (`get_crypto_price`)
    *   Fetches **real-time** market data via CoinLore API.
    *   Understands slang ("BTC", "Ether", "TON").
    *   Forces data updates on every request (prevents hallucinations).
2.  🧮 **Currency Calculator** (`currency_calculator`)
    *   Performs mathematical calculations.
    *   Works in conjunction with the first tool (remembers the rate from the previous message).
3.  🎲 **Fate Dice** (`fate_dice`)
    *   Random event generator (d20).
    *   Used for questions like "Should I buy?", "Give me a sign", etc.

### 🏗 Tech Stack
*   **Language:** Python 3.11
*   **LLM Orchestration:** [LangGraph](https://langchain-ai.github.io/langgraph/) (Stateful Agent)
*   **Model:** OpenAI GPT-4o-mini
*   **Interface:** Aiogram 3.x (Telegram Bot API)
*   **Database:** SQLite (Memory/Checkpoints)
*   **Infrastructure:** Docker & Docker Compose

### 🚀 Setup & Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/tarot-bot.git
    cd tarot-bot
    ```
2.  **Create `.env` file:**
    ```ini
    TG_BOT_TOKEN=your_telegram_token
    OPENAI_API_KEY=sk-your_openai_key
    ```
3.  **Run with Docker:**
    ```bash
    docker compose up --build -d
    ```

### 📊 Logging (Demo)
To see the agent's "Chain of Thought" and tool selection process:
```bash
docker compose logs -f
```
**Example Output:**
```text
INFO | 🧠 LLM INPUT: 'bitcoin price'
INFO | 👉 LLM DECISION: Selected tools -> [get_crypto_price]
INFO | 🔧 TOOL CALL: [get_crypto_price] API request for 'bitcoin'
INFO | ✅ TOOL RESULT: 💰 Bitcoin (BTC): $64,300
```

---

## 🇨🇳 中文 (Chinese)

**Crypto Tarot Bot** 是一个智能 AI 代理，它将枯燥的金融数据与塔罗玄学相结合。该机器人不仅回答问题，还会进行“思考”，选择合适的工具，并记住对话上下文。

> **特点：** 机器人使用 **LangGraph** 架构管理对话状态，并使用 **Function Calling**（函数调用）进行决策。

### 🛠 工具 (Tools)
代理根据用户请求自主决定使用哪种工具：

1.  📈 **加密货币价格追踪器** (`get_crypto_price`)
    *   通过 CoinLore API 获取**实时**市场数据。
    *   理解俚语（如 "BTC", "Ether", "TON"）。
    *   每次请求强制更新数据（防止 AI 幻觉）。
2.  🧮 **汇率计算器** (`currency_calculator`)
    *   执行数学计算。
    *   与第一个工具配合使用（记住上一条消息中的汇率）。
3.  🎲 **命运骰子** (`fate_dice`)
    *   随机事件生成器 (d20)。
    *   用于回答“我应该买吗？”、“给我一个信号”等问题。

### 🏗 技术栈
*   **语言:** Python 3.11
*   **LLM 编排:** [LangGraph](https://langchain-ai.github.io/langgraph/) (有状态代理)
*   **模型:** OpenAI GPT-4o-mini
*   **接口:** Aiogram 3.x (Telegram Bot API)
*   **数据库:** SQLite (记忆/检查点)
*   **基础设施:** Docker & Docker Compose

### 🚀 安装与运行

1.  **克隆仓库:**
    ```bash
    git clone https://github.com/your-username/tarot-bot.git
    cd tarot-bot
    ```
2.  **创建 `.env` 文件:**
    ```ini
    TG_BOT_TOKEN=你的telegram_token
    OPENAI_API_KEY=sk-你的openai_key
    ```
3.  **使用 Docker 运行:**
    ```bash
    docker compose up --build -d
    ```

### 📊 日志监控 (演示)
查看代理的“思维链”和工具选择过程：
```bash
docker compose logs -f
```
**输出示例:**
```text
INFO | 🧠 LLM INPUT: 'bitcoin price'
INFO | 👉 LLM DECISION: Selected tools -> [get_crypto_price]
INFO | 🔧 TOOL CALL: [get_crypto_price] API request for 'bitcoin'
INFO | ✅ TOOL RESULT: 💰 Bitcoin (BTC): $64,300
```

---

## 🇷🇺 Русский

**Crypto Tarot Bot** — это умный AI-агент, который объединяет сухие финансовые данные с мистикой Таро. Бот не просто отвечает на вопросы, он "думает", выбирает подходящие инструменты и помнит контекст диалога.

> **Особенность:** Бот использует архитектуру **LangGraph** для управления состоянием диалога и **Function Calling** для принятия решений.

### 🛠 Функциональность
Агент самостоятельно решает, какой инструмент использовать в зависимости от запроса пользователя:

1.  📈 **Crypto Price Tracker** (`get_crypto_price`)
    *   Получает **реальные** рыночные данные через CoinLore API.
    *   Понимает сленг ("биток", "эфир", "тон").
    *   Принудительно обновляет данные при каждом запросе (защита от галлюцинаций).
2.  🧮 **Currency Calculator** (`currency_calculator`)
    *   Выполняет математические расчеты.
    *   Работает в связке с первым инструментом (помнит курс из предыдущего сообщения).
3.  🎲 **Fate Dice** (`fate_dice`)
    *   Генератор случайных событий (d20).
    *   Используется для ответов на вопросы "Стоит ли покупать?", "Дай знак" и т.д.

### 🏗 Технический стек
*   **Язык:** Python 3.11
*   **LLM Orchestration:** [LangGraph](https://langchain-ai.github.io/langgraph/) (Stateful Agent)
*   **Model:** OpenAI GPT-4o-mini
*   **Interface:** Aiogram 3.x (Telegram Bot API)
*   **Database:** SQLite (хранение истории/чекпоинтов)
*   **Infrastructure:** Docker & Docker Compose

### 🚀 Установка и Запуск

1.  **Клонирование репозитория:**
    ```bash
    git clone https://github.com/your-username/tarot-bot.git
    cd tarot-bot
    ```
2.  **Настройка окружения:**
    Создайте файл `.env` в корне проекта:
    ```ini
    TG_BOT_TOKEN=ващ_телеграм_токен
    OPENAI_API_KEY=sk-ваш_ключ_openai
    ```
3.  **Запуск в Docker:**
    ```bash
    docker compose up --build -d
    ```

### 📊 Мониторинг и Логи (Демонстрация)
Проект настроен на подробное логирование процесса принятия решений. Вы можете видеть, как агент выбирает инструменты в реальном времени.

**Команда:**
```bash
docker compose logs -f
```

**Пример вывода:**
```text
INFO | 🧠 LLM INPUT: 'курс битка'
INFO | 👉 LLM DECISION: Выбраны инструменты -> [get_crypto_price]
INFO | 🔧 TOOL CALL: [get_crypto_price] запрос к API для 'bitcoin'
INFO | ✅ TOOL RESULT: 💰 Bitcoin (BTC): $64,300
```