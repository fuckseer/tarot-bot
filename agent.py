import os
import sqlite3
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage  # <--- Импортируем SystemMessage
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.sqlite import SqliteSaver
from tools import tools_list
from logger import logger

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
llm_with_tools = llm.bind_tools(tools_list)

SYSTEM_PROMPT = """Ты — Мистический Финансовый Таролог.
Твоя задача — сочетать эзотерику с АКТУАЛЬНЫМИ финансовыми данными.

КРИТИЧЕСКИ ВАЖНЫЕ ПРАВИЛА:
1. Финансовые рынки меняются каждую секунду. Данные из предыдущих сообщений СЧИТАЮТСЯ УСТАРЕВШИМИ.
2. Если пользователь спрашивает курс (цена, стоимость, 'почем', 'биток', 'эфир') — ТЫ ОБЯЗАН КАЖДЫЙ РАЗ вызывать инструмент `get_crypto_price`.
3. ЗАПРЕЩЕНО брать цены из истории диалога. Даже если ты называл цену 10 секунд назад — вызови инструмент снова!
4. Если ты видишь цену в истории сообщений — ИГНОРИРУЙ ЕЁ. Сделай новый запрос.
5. Для расчетов используй `currency_calculator`.
6. Для советов используй `fate_dice`.

Твой тон: загадочный, но цифры должны быть свежими и точными (из инструмента)."""


def reasoner_node(state: MessagesState):
    messages = state["messages"]
    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages

    last_msg = messages[-1].content
    logger.info(f"🧠 LLM INPUT: '{last_msg}'")

    response = llm_with_tools.invoke(messages)

    if response.tool_calls:
        tool_names = ", ".join([t['name'] for t in response.tool_calls])
        logger.info(f"👉 LLM DECISION: Выбраны инструменты -> [{tool_names}]")
    else:
        clean_content = response.content.replace('\n', ' ')[:100]
        logger.info(f"🗣 LLM ANSWER (Без тулов): {clean_content}...")

    return {"messages": [response]}


builder = StateGraph(MessagesState)
builder.add_node("reasoner", reasoner_node)
builder.add_node("tools", ToolNode(tools_list))

builder.add_edge(START, "reasoner")
builder.add_conditional_edges("reasoner", tools_condition)
builder.add_edge("tools", "reasoner")

db_path = "data/checkpoints.sqlite"
db_dir = os.path.dirname(db_path)
if db_dir:
    os.makedirs(db_dir, exist_ok=True)

conn = sqlite3.connect(db_path, check_same_thread=False)
memory = SqliteSaver(conn)

graph_app = builder.compile(checkpointer=memory)