<div align="center">

# 🤖 LangChain Agents + Tool Calling

### Autonomous AI Agent using ReAct Pattern + Custom Tools
*Powered by LangChain + Google Gemini + Custom Tool Calling*

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-green?style=for-the-badge&logo=chainlink&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-API-orange?style=for-the-badge&logo=google&logoColor=white)
![ReAct](https://img.shields.io/badge/ReAct-Pattern-purple?style=for-the-badge)

<br/>

**Built by [Manpreet Kaur](https://github.com/manuu231)**
MS Data Science @ Clarkson University | AI/ML Engineer | 3+ Years @ Wipro

</div>

---

## 📌 What Does This Project Do?

A LangChain Agent that thinks, decides, and acts autonomously using the **ReAct (Reasoning + Acting)** pattern with 4 custom tools.

```
Normal Chain:
Input → Step 1 → Step 2 → Output (fixed, no thinking)

Agent:
Input → Think → Choose Tool → Act → Observe → 
Think Again → Done? Yes → Output ✅
```

---

## 🧠 What is the ReAct Pattern?

**ReAct = Reasoning + Acting**

```
Question: "What is 1234 * 5678?"

Thought:  I need to calculate this mathematically
Action:   Calculator
Input:    1234 * 5678
Result:   7006652
Thought:  I have the answer
Answer:   1234 * 5678 = 7,006,652 ✅
```

Agent keeps thinking and acting until it finds the final answer!

---

## 🔧 4 Custom Tools

| Tool | What it does | Example |
|------|-------------|---------|
| 🧮 **Calculator** | Math calculations | `1234 * 5678` |
| 🔄 **Unit Converter** | Convert between units | `100 km to miles` |
| 📝 **Text Analyzer** | Analyze text statistics | Word count, sentence count |
| 📚 **Knowledge Base** | AI/ML topic information | RAG, LangChain, FAISS |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Programming language |
| 🔗 LangChain | Agent framework |
| 🤖 Google Gemini | LLM brain of the agent |
| 🔧 Custom Tools | Agent capabilities |
| 📐 ReAct Pattern | Agent thinking framework |

---

## 🔄 How the Agent Works

```
User Question
      │
      ▼
Agent Thinks (Gemini)
"What tool do I need?"
      │
      ▼
Chooses Right Tool
Calculator / Converter / Analyzer / Knowledge
      │
      ▼
Uses Tool
Gets Result
      │
      ▼
Thinks Again
"Is this enough to answer?"
      │
    Yes ──────────────────────────────▶ Final Answer ✅
      │
     No
      │
      ▼
Uses Another Tool → Repeats
```

---

## ⚙️ Setup and Installation

### Step 1 — Clone Repository
```bash
git clone https://github.com/manuu231/LangChain_Agents_Tool_Calling.git
cd LangChain_Agents_Tool_Calling
```

### Step 2 — Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Set Up API Key
Create a `.env` file:
```
GOOGLE_API_KEY=your_gemini_key_here
```

### Step 5 — Run
```bash
python3 Agents.py
```

---

## 🚀 Example Outputs

### Calculator Tool:
```
❓ What is 1234 multiplied by 5678?

Thought: I need to calculate this
Action: Calculator
Input: 1234 * 5678
Result: 7006652

✅ FINAL ANSWER: 7,006,652
```

### Unit Converter Tool:
```
❓ Convert 100 km to miles

Thought: I need to convert units
Action: UnitConverter
Input: 100 km to miles
Result: 62.14 miles

✅ FINAL ANSWER: 100 km = 62.14 miles
```

### Knowledge Base Tool:
```
❓ What is RAG in machine learning?

Thought: I need to look this up
Action: KnowledgeBase
Input: RAG
Result: RAG (Retrieval Augmented Generation)...

✅ FINAL ANSWER: RAG is a technique that retrieves...
```

---

## 🔐 API Key Safety

| Platform | How to store key |
|----------|-----------------|
| Local | `.env` file — never commit to GitHub! |
| GitHub | Add `.env` to `.gitignore` |
| Production | Environment variables |

---

## 📁 Project Structure

```
LangChain_Agents_Tool_Calling/
│
├── Agents.py            ← Main agent code
├── requirements.txt     ← Dependencies
├── .env                 ← API keys (never commit!)
├── .gitignore           ← Excludes .env from GitHub
└── README.md            ← This file
```

---

## 🔭  AI Engineering Journey

| Project | Status |
|---------|--------|
| Interview Bot | ✅ Done |
| Smart Document Assistant | ✅ Done |
| HR Knowledge Bot — Pinecone | ✅ Done |
| Local RAG — Mistral + Ollama | ✅ Done |
| LangChain Agents + Tool Calling | ✅ Done |
| Prompt Engineering | ✅ Done |
| LangGraph + CrewAI | 🔒 Coming |

---

## 📄 License
MIT License — free to use and modify!

---

<div align="center">

⭐ **Star this repo if you found it helpful!**

Made with ❤️ by [Manpreet Kaur](https://github.com/manuu231)

🔗 [GitHub](https://github.com/manuu231) | 
🤗 [Hugging Face](https://huggingface.co/Manpreet02)

</div>
