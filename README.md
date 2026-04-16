# 🦜 LangChain & ReAct Agent Learning Project

A hands-on, notebook-driven course covering the fundamentals of **LangChain** — from basic LLM calls to advanced agentic AI systems with real database integration.

---

## 📁 Project Structure

```
langchain-project/
│
├── 📂 .venv/                              # Virtual environment (not committed)
│
├── 📂 CH-1 — LangChain Fundamentals
│   ├── 1_LLM_CALL.ipynb                   # Your first LLM chain
│   ├── 2_MESSAGES.ipynb                   # Messages, prompts & templates
│   └── 3_Structured_output.ipynb          # JSON & Pydantic structured outputs
│
├── 📂 CH-2 — Chains
│   ├── 1_FIRST_CHAIN.ipynb                # Building your first chain
│   ├── 2_CHAIN_WITH_CUSTOM_RUNNABLE.ipynb # Custom runnables & multi-step chains
│   ├── 3_Parallel_chain.ipynb             # Parallel chains with RunnableParallel
│   └── 4_conditional_chain.ipynb          # Conditional/branching chains with RunnableBranch
│
├── 📂 CH-3 — ReAct Agents
│   ├── 📂 SalesDB/
│   │   └── sales.db                       # SQLite sales database
│   ├── 1_reAct_agent_intro.ipynb          # ReAct agent with web & Wikipedia tools
│   ├── 2_reAct_db_agent.ipynb             # SQL database agent
│   ├── demo.py                            # Database query demo
│   └── init_db.py                         # SQLite database setup script
│
├── .env                                   # API keys (not committed)
├── .gitignore                             # Git ignore rules
├── .python-version                        # Pinned Python version (for pyenv/uv)
├── main.py                                # Project entry point
├── pyproject.toml                         # Project metadata & dependencies
├── README.md                              # This file
└── uv.lock                                # Locked dependency versions (uv)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- A [Groq API key](https://console.groq.com/) (free tier available)

### Installation

This project uses **[uv](https://docs.astral.sh/uv/)** as the package manager (faster alternative to pip). Dependencies and their exact versions are locked in `uv.lock`.

```bash
# Clone the repo
git clone <your-repo-url>
cd langchain-project

# Install uv (if you don't have it)
pip install uv

# Install all dependencies from uv.lock (fast & reproducible)
uv sync
```

> **Prefer plain pip?** You can still use it:
> ```bash
> python -m venv .venv
> # Windows: .venv\Scripts\activate | Mac/Linux: source .venv/bin/activate
> pip install langchain langchain-groq langchain-community langgraph pydantic python-dotenv
> ```

### Environment Setup

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Database Setup (for CH-3)

```bash
cd CH-3
python init_db.py   # Creates SalesDB/sales.db with sample data
python demo.py      # Verify the database is working
```

---

## 📚 Chapter Breakdown

### CH-1 — LangChain Fundamentals

> **Goal:** Understand the core building blocks of LangChain.

| Notebook | What You'll Learn |
|---|---|
| `1_LLM_CALL.ipynb` | Instantiate a `ChatGroq` LLM, create a `ChatPromptTemplate`, and pipe them together with `StrOutputParser` into your first chain |
| `2_MESSAGES.ipynb` | Use `HumanMessage` / `SystemMessage` directly, build dynamic prompts with `PromptTemplate`, and control tone with input variables |
| `3_Structured_output.ipynb` | Guide the LLM with prompt engineering, enforce schemas with **Pydantic** (`BaseModel`) and **TypedDict** using `with_structured_output()` |

**Key concepts:** `ChatGroq`, `ChatPromptTemplate`, `StrOutputParser`, `PromptTemplate`, `with_structured_output`, `BaseModel`, `TypedDict`

---

### CH-2 — Chains

> **Goal:** Master LangChain's composable pipeline (LCEL — LangChain Expression Language).

| Notebook | What You'll Learn |
|---|---|
| `1_FIRST_CHAIN.ipynb` | Build a chain with the `|` pipe operator; understand manual vs chain invocation |
| `2_CHAIN_WITH_CUSTOM_RUNNABLE.ipynb` | Inject custom Python logic using `RunnableLambda`; build a multi-step chain that generates a LinkedIn post from any input |
| `3_Parallel_chain.ipynb` | Run multiple chains simultaneously with `RunnableParallel`; generate LinkedIn + Instagram posts in one shot |
| `4_conditional_chain.ipynb` | Route output through different chains based on conditions using `RunnableBranch`; classify movie reviews and generate platform-specific posts |

**Key concepts:** LCEL (`|` operator), `RunnableLambda`, `RunnableParallel`, `RunnableBranch`, `chain.invoke()`

---

### CH-3 — ReAct Agents

> **Goal:** Build autonomous AI agents that reason, use tools, and take actions.

| Notebook | What You'll Learn |
|---|---|
| `1_reAct_agent_intro.ipynb` | Create a ReAct agent with 3 tools: DuckDuckGo web search, Wikipedia, and a custom enterprise tool; stream agent reasoning step-by-step |
| `2_reAct_db_agent.ipynb` | Connect an agent to a real SQLite database using `SQLDatabaseToolkit`; ask natural language questions and get SQL-powered answers |

**Key concepts:** `create_react_agent` (LangGraph), `@tool` decorator, `DuckDuckGoSearchRun`, `WikipediaQueryRun`, `SQLDatabaseToolkit`, `bind_tools`, agent streaming

**The Sales Database (`SalesDB/sales.db`):**

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Auto-increment primary key |
| `customer_name` | TEXT | Customer's name |
| `prod_name` | TEXT | Product sold |
| `quantity` | INTEGER | Units sold |
| `price` | REAL | Price per unit |
| `total` | REAL | Total value (quantity × price) |

Sample customers: Vinay, Rahul, Priya, Amit, Sneha, Rohit, Neha — selling Laptops, Phones, and Tablets.

---

## 🔑 Key Libraries

| Library | Purpose |
|---|---|
| `langchain-groq` | Groq-hosted LLM integration (`llama-3.3-70b-versatile`) |
| `langchain-core` | Core primitives — prompts, messages, parsers, runnables |
| `langchain-community` | Community tools — DuckDuckGo, Wikipedia, SQL |
| `langgraph` | `create_react_agent` for building stateful agents |
| `pydantic` | Structured output schema definitions |
| `python-dotenv` | Load API keys from `.env` |

---

## 💡 Learning Path

Follow the chapters in order for the best experience:

```
CH-1: LLM Call → Messages → Structured Output
         ↓
CH-2: First Chain → Custom Runnable → Parallel → Conditional
         ↓
CH-3: ReAct Agent → DB Agent
```

Each notebook is self-contained and builds on the previous concepts. By the end of CH-3, you'll be building agents that can autonomously query databases and search the web to answer real questions.

---

## ⚙️ Model Used

All notebooks use **`llama-3.3-70b-versatile`** via [Groq](https://groq.com/) — a fast, free-tier-accessible LLM inference platform. No GPU required.

---

## 📝 Notes

- Keep your `.env` file out of version control — add it to `.gitignore`
- Run `init_db.py` before the CH-3 notebooks to create the database
- The `recursion_limit: 15` in agent calls prevents infinite reasoning loops
- Temperature `0` is used for deterministic outputs in most notebooks; `0.7` where creativity is needed
