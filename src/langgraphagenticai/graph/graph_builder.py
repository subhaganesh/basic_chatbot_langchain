from langgraph.graph import StateGraph
from src.langgraphagenticai.state.state import State
from langgraph.graph import START,END
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraphagenticai.nodes.ai_news_node import AINewsNode
class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """

        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        
        #add nodes
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        #add edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools_build_graph(self):
        """
        Builds a chatbot graph with tool integration using LangGraph.
        we are using tavily tools for this implementation.
        """
        #define tool and tool node 
        tools=get_tools()
        tool_node=create_tool_node(tools)

        #define llm
        llm=self.llm

        #define the chatbot
        obj_chatbot_with_node=ChatbotWithToolNode(llm)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)

        #add nodes and edges to the graph
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)
        #define conditional and direct edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot",END)


    def ai_news_builder_graph(self):
        """
        Builds an AI news graph using LangGraph.
        This method initializes a chatbot node specialized for AI news 
        and integrates it into the graph. The chatbot node is set as both 
        the entry and exit point of the graph.
        """

        ai_news_node=AINewsNode(self.llm)
        fetch_news_node=ai_news_node.fetch_news
        fetch_summary_node=ai_news_node.summarize_news
        fetch_save_node=ai_news_node.save_result


        
        #add nodes
        self.graph_builder.add_node("fetch_news",fetch_news_node)
        self.graph_builder.add_node("summarize_news",fetch_summary_node)
        self.graph_builder.add_node("save_result",fetch_save_node)
        
        #add edges
        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result",END)


    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "Chatbot with web search":
            self.chatbot_with_tools_build_graph()
        if usecase == "AI News":
            self.ai_news_builder_graph()

        return self.graph_builder.compile()
