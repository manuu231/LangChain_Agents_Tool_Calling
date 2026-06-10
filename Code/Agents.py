# ============================================================
# Day 9 — LangChain Agents + Tool Calling
# No external APIs needed — all tools work locally!
# ============================================================

import os
import math
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain_core.prompts import PromptTemplate

# ---- Step 1: Load API Key -----------------------------------
os.environ["GOOGLE_API_KEY"] = "my_api_key"

# ---- Step 2: Create LLM -------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)
print("✅ LLM created!")

# ---- Step 3: Create Custom Tools ----------------------------
# These tools work 100% locally — no internet needed!

# Tool 1 — Calculator


def calculate(expression):
    """
    Performs math calculations
    Input: math expression like "25 * 48" or "sqrt(144)"
    """
    try:
        # Allow safe math operations
        allowed = {
            'sqrt': math.sqrt,
            'pi': math.pi,
            'pow': math.pow,
            'abs': abs,
            'round': round
        }
        result = eval(expression, {"__builtins__": {}}, allowed)
        return f"The result of {expression} = {result}"
    except Exception as e:
        return f"Error calculating: {str(e)}"


calculator_tool = Tool(
    name="Calculator",
    func=calculate,
    description="Use this for ANY math calculation. Input must be a math expression like '25 * 48' or 'sqrt(144)' or '100 / 4 + 50'"
)

# Tool 2 — Text Analyzer


def analyze_text(text):
    """
    Analyzes text and returns statistics
    Input: any text string
    """
    words = text.split()
    sentences = text.split('.')
    characters = len(text)
    return f"""Text Analysis Results:
    - Word count: {len(words)}
    - Sentence count: {len([s for s in sentences if s.strip()])}
    - Character count: {characters}
    - Average word length: {sum(len(w) for w in words) / len(words):.1f} chars
    - Longest word: {max(words, key=len)}"""


text_tool = Tool(
    name="TextAnalyzer",
    func=analyze_text,
    description="Use this to analyze any text — counts words, sentences, characters. Input should be the text you want to analyze."
)

# Tool 3 — Unit Converter


def convert_units(query):
    """
    Converts between common units
    Input: conversion query like "100 km to miles" or "50 celsius to fahrenheit"
    """
    query = query.lower()
    try:
        # Temperature conversions
        if "celsius to fahrenheit" in query or "c to f" in query:
            num = float(
                ''.join(filter(lambda x: x.isdigit() or x == '.', query.split()[0])))
            result = (num * 9/5) + 32
            return f"{num}°C = {result:.2f}°F"

        elif "fahrenheit to celsius" in query or "f to c" in query:
            num = float(
                ''.join(filter(lambda x: x.isdigit() or x == '.', query.split()[0])))
            result = (num - 32) * 5/9
            return f"{num}°F = {result:.2f}°C"

        # Distance conversions
        elif "km to miles" in query:
            num = float(
                ''.join(filter(lambda x: x.isdigit() or x == '.', query.split()[0])))
            result = num * 0.621371
            return f"{num} km = {result:.2f} miles"

        elif "miles to km" in query:
            num = float(
                ''.join(filter(lambda x: x.isdigit() or x == '.', query.split()[0])))
            result = num * 1.60934
            return f"{num} miles = {result:.2f} km"

        # Weight conversions
        elif "kg to pounds" in query or "kg to lbs" in query:
            num = float(
                ''.join(filter(lambda x: x.isdigit() or x == '.', query.split()[0])))
            result = num * 2.20462
            return f"{num} kg = {result:.2f} pounds"

        elif "pounds to kg" in query or "lbs to kg" in query:
            num = float(
                ''.join(filter(lambda x: x.isdigit() or x == '.', query.split()[0])))
            result = num * 0.453592
            return f"{num} pounds = {result:.2f} kg"

        else:
            return "Supported conversions: celsius/fahrenheit, km/miles, kg/pounds"

    except Exception as e:
        return f"Error converting: {str(e)}"


converter_tool = Tool(
    name="UnitConverter",
    func=convert_units,
    description="Use this to convert between units. Examples: '100 km to miles', '37 celsius to fahrenheit', '70 kg to pounds'"
)

# Tool 4 — Simple Knowledge Base


def knowledge_base(query):
    """
    Returns information about AI/ML topics
    """
    knowledge = {
        "langchain": "LangChain is a framework for building AI applications using LLMs. It provides tools for chains, agents, memory, and RAG pipelines.",
        "rag": "RAG (Retrieval Augmented Generation) is a technique that retrieves relevant documents and passes them to an LLM to generate accurate answers.",
        "ollama": "Ollama is a tool that lets you run AI models like Mistral and Llama3 locally on your machine without internet or API costs.",
        "mistral": "Mistral 7B is an open source large language model by Mistral AI (France) with 7 billion parameters that runs locally.",
        "faiss": "FAISS (Facebook AI Similarity Search) is a local vector database that stores and searches embeddings efficiently.",
        "pinecone": "Pinecone is a cloud vector database that stores vectors persistently, scales to millions of vectors, and supports namespace filtering.",
        "agent": "A LangChain Agent is an AI that can plan, make decisions, and use tools autonomously to complete complex tasks.",
        "embeddings": "Embeddings are numerical representations of text that capture semantic meaning, allowing computers to understand similarity between texts.",
        "chroma": "Chroma is a local vector database with persistence - data is saved to disk and survives system restarts.",
        "prompt engineering": "Prompt Engineering is the practice of designing and optimizing prompts to get better responses from AI models."
    }

    query_lower = query.lower()
    for key, value in knowledge.items():
        if key in query_lower:
            return value

    return f"I don't have specific information about '{query}' in my knowledge base. Try asking about: {', '.join(knowledge.keys())}"


knowledge_tool = Tool(
    name="KnowledgeBase",
    func=knowledge_base,
    description="Use this to get information about AI/ML topics like LangChain, RAG, Ollama, Mistral, FAISS, Pinecone, Agents, Embeddings, Chroma, Prompt Engineering."
)

# All tools list
tools = [calculator_tool, text_tool, converter_tool, knowledge_tool]
print(f"✅ {len(tools)} tools created!")
for tool in tools:
    print(f"   🔧 {tool.name}: {tool.description[:50]}...")

# ---- Step 4: Create ReAct Prompt ----------------------------
react_prompt = PromptTemplate.from_template("""You are a helpful AI assistant with access to tools.
Answer the question as best you can.

You have access to the following tools:
{tools}

Use the following format STRICTLY:
Question: the input question you must answer
Thought: think about what to do
Action: the action to take, must be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (repeat Thought/Action/Action Input/Observation N times)
Thought: I now know the final answer
Final Answer: the final answer to the original question

Begin!
Question: {input}
Thought:{agent_scratchpad}""")

print("✅ ReAct prompt created!")

# ---- Step 5: Create Agent -----------------------------------
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=5,
    handle_parsing_errors=True
)
print("✅ Agent created!")
print()
print("=" * 60)
print("🚀 LangChain Agent Ready!")
print("   Tools: Calculator + TextAnalyzer + UnitConverter + KnowledgeBase")
print("   Model: Gemini 1.5 Flash")
print("=" * 60)

# ---- Step 6: Test Agent -------------------------------------


def ask_agent(question):
    print(f"\n{'='*60}")
    print(f"❓ QUESTION: {question}")
    print('='*60)
    result = agent_executor.invoke({"input": question})
    print(f"\n✅ FINAL ANSWER: {result['output']}")
    return result['output']


# Test 1 — Calculator
ask_agent("What is 1234 multiplied by 5678?")

# Test 2 — Unit Converter
ask_agent("Convert 100 km to miles")

# Test 3 — Knowledge Base
ask_agent("What is RAG in machine learning?")

# Test 4 — Text Analysis
ask_agent("Analyze this text: LangChain is an amazing framework for building AI applications with large language models")

# Test 5 — Temperature conversion
ask_agent("Convert 37 celsius to fahrenheit")

# Test 6 — Multi step (uses calculator twice!)
ask_agent("What is 15 * 8 and also convert 50 kg to pounds?")
