import os
import sqlite3
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.sqlite import SqliteSaver
from tools import tools_list
from logger import logger

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
llm_with_tools = llm.bind_tools(tools_list)



def reasoner_node(state: MessagesState):
    messages = state["messages"]
    last_msg = messages[-1].content

    logger.info(f"🧠 LLM INPUT: Входящее сообщение: '{last_msg}'")

    response = llm_with_tools.invoke(messages)

    if response.tool_calls:
        tool_names = ", ".join([t['name'] for t in response.tool_calls])
        logger.info(f"👉 LLM DECISION: Выбраны инструменты -> [{tool_names}]")
    else:
        logger.info(f"🗣 LLM ANSWER: Отвечает текстом (без инструментов)")

    return {"messages": [response]}


builder = StateGraph(MessagesState)
builder.add_node("reasoner", reasoner_node)
builder.add_node("tools", ToolNode(tools_list))

builder.add_edge(START, "reasoner")
builder.add_conditional_edges("reasoner", tools_condition)
builder.add_edge("tools", "reasoner")

db_path = "data/checkpoints.sqlite"
conn = sqlite3.connect(db_path, check_same_thread=False)
memory = SqliteSaver(conn)

# Компиляция графа
graph_app = builder.compile(checkpointer=memory)