#%% Graph 1: Hello World Graph
from typing import Dict, TypedDict

# framework that helps you design and manage the flow of tasks in your application using a graph
from langgraph.graph import StateGraph

#%% AgentState 
class AgentState(TypedDict):
	"""
	State Schema
	"""
	message: str
	
def greeting_node(state: AgentState) -> AgentState:
	"""
	Simple node that adds a greeting message to the state
	"""
	state["message"] = f"Hello {state['message']}!"

	return state

#%% langgraph.graph
graph = StateGraph(state_schema=AgentState)

graph.add_node("greeter", greeting_node)

graph.set_entry_point("greeter")

graph.set_finish_point("greeter")

app = graph.compile()
# %% Display graph
from IPython.display import Image, display

display(Image(app.get_graph().draw_mermaid_png()))

# %% Run graph

result = app.invoke({"message": "robit"})
result
result["message"]

# %% Exercise for Graph 1: Create a personalized compliment agent using LangGraph

def compliment_node(state: AgentState) -> AgentState:
	"""
	Simple node that adds a compliment message to the message state
	"""
	state["message"] = f"{state['message']}, you're doing an amazing job learning LangGraph!"

	return state

#%% Compliment Graph

compliment_graph = StateGraph(state_schema=AgentState)

compliment_graph.add_node("complimenter", compliment_node)

compliment_graph.set_entry_point("complimenter")

compliment_graph.set_finish_point("complimenter")

compliment_app = compliment_graph.compile()

# %% Compliment Graph Result

compliment_result = compliment_app.invoke({"message": "bobit"})
compliment_result["message"]

# %%
