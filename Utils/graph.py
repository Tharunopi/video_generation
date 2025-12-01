from Utils.state import AgentState
from langgraph.graph import StateGraph

class Graph:
    @staticmethod
    def get_graph():
        return StateGraph(AgentState)