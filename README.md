# ResearchMind

A polished AI-powered research assistant that combines multiple specialized agents to gather information, extract insights, write reports, and critique the final output.

ResearchMind is designed to showcase modern LLM application development using LangChain, LangGraph, Streamlit, and external tools such as Tavily search and web scraping.

## ✨ Project Overview

ResearchMind demonstrates a multi-agent workflow where different AI components collaborate to complete a research task end-to-end. Instead of relying on a single prompt, the system breaks the process into dedicated stages:

1. Search Agent gathers recent and relevant information
2. Reader Agent scrapes and extracts deeper content from selected sources
3. Writer Chain generates a professional research report
4. Critic Chain evaluates the report and provides improvement feedback

This makes the project highly relevant for demonstrating skills in:
- LLM orchestration
- Agent-based systems
- Prompt engineering
- Tool-using AI workflows
- Full-stack AI app development

## 🚀 Key Features

- Multi-agent research pipeline for topic exploration
- Web search integration using Tavily
- URL-based content scraping for deeper research
- Structured report generation with clear sections
- Built-in critique and scoring feedback loop
- Interactive Streamlit web interface for easy use
- Clean, modern UI designed for presentation and demos

## 🧠 How It Works

The application follows a four-step workflow:

- Search Agent: Finds recent and reliable web information related to a user topic
- Reader Agent: Chooses a relevant URL and extracts richer content
- Writer Chain: Converts gathered research into a well-structured report
- Critic Chain: Reviews the report and returns feedback with a score

## 🛠️ Tech Stack

- Python
- LangChain
- LangGraph
- Mistral AI
- Streamlit
- Tavily API
- BeautifulSoup
- Requests
- Python-dotenv

## 📁 Project Structure

```text
.
├── app.py
├── agents.py
├── pipeline.py
├── tools.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your API keys:

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## ▶️ Running the Project

### Streamlit Web App

```bash
streamlit run app.py
```

### CLI Pipeline

```bash
python pipeline.py
```

## 📌 Example Use Case

You can ask the system to research topics such as:
- Quantum computing breakthroughs
- CRISPR gene editing
- Fusion energy progress
- AI trends in 2025

The system will then generate a research-style report and feedback summary automatically.

## 🎯 Why This Project Is Resume-Ready

This project highlights practical experience with:
- Building AI agents with tool use
- Designing multi-step LLM workflows
- Connecting LLMs to real-world APIs
- Creating interactive user interfaces for AI tools
- Developing end-to-end AI applications beyond simple chatbots

## 🔮 Future Improvements

Possible enhancements include:
- Citation and source verification
- PDF report export
- Memory for long-running research sessions
- Multi-source comparison and synthesis
- User authentication and saved reports

## 📄 License

This project is open for educational and portfolio use.
