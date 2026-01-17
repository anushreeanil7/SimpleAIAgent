from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """
    Useful for performing basic arithmetic calculations with numbers
    """
    print("Tool has been called")
    return f"The sum of {a} and {b} is {a + b}"


def main():
    model = ChatGroq(model="llama-3.3-70b-versatile",temperature = 0)

    tools = [calculator]

    agent_executor = create_agent(model=model, tools=tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == 'quit':
            break

        response = agent_executor.invoke(
            {"messages" : [HumanMessage(content=user_input)]}
        )

        print("\nAssistant:", response["messages"][-1].content)

if __name__ == "__main__":
    main()