import os
import sqlite3
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.sqlite import SqliteSaver
from tools import tools_list
from logger import logger

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    logger.error("❌ OШИБКА: Не найден OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
llm_with_tools = llm.bind_tools(tools_list)


def reasoner_node(state: MessagesState):
    messages = state["messages"]
    last_msg = messages[-1].content

    logger.info(f"🧠 LLM INPUT: '{last_msg}'")

    response = llm_with_tools.invoke(messages)

    if response.tool_calls:
        tool_names = ", ".join([t['name'] for t in response.tool_calls])
        logger.info(f"👉 LLM DECISION: Выбраны инструменты -> [{tool_names}]")
    else:
        logger.info(f"🗣 LLM ANSWER: Текст")

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