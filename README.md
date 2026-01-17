**AI Assistant using LangChain + LangGraph + Groq**
- This project is a simple AI agent built using:
- LangChain (Agent Framework)
- LangGraph (Workflow engine behind agent)
- Groq API (Free LLM - Llama 3.3 70B)
- Python + uv (fast environment manager)

The assistant can chat with users and use tools when needed.

**Features**
- Conversational AI agent
- Tool calling support
- Uses Groq free model
- Secure API key handling
- Built with LangChain

**Tech Stack**
- Python 3.11
- Groq API
- uv package manager

**Setup Instructions**
**1. Clone the repo**
```git clone <your_repo_link>```
```cd project1```

**2. Install dependencies using uv**
```uv sync```

**3. Create .env file**
```touch .env```
Add your groq key inside:
```GROQ_API_KEY=your_key_here```

**4. Run the assistant**
```uv run main.py```





