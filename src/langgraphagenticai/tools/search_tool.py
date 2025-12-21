from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():

    """
    Returns a list of tools to be used in the chatbot graph.
    Currently includes the Tavily Search Tool.
    """
    tools =[TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the given graph
    
    """
    return ToolNode(tools=tools)