from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents import researcher, writer, editor


class BlogState(TypedDict):
    topic: str
    research: str
    draft: str
    final: str


def build_graph():
    graph = StateGraph(BlogState)

    graph.add_node("researcher", researcher)
    graph.add_node("writer", writer)
    graph.add_node("editor", editor)

    graph.set_entry_point("researcher")
    graph.add_edge("researcher", "writer")
    graph.add_edge("writer", "editor")
    graph.add_edge("editor", END)

    return graph.compile()