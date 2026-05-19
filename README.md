# Week 11 - Multi-Agent Blog Pipeline

A multi-agent system that automatically researches, writes, 
and edits blog posts using three specialised AI agents 
orchestrated with LangGraph.

## What it does
- Researcher agent gathers facts, statistics, and insights
- Writer agent drafts a structured blog post from the research
- Editor agent improves quality, flow, and engagement
- All three agents share state through a LangGraph pipeline
- Produces publication-ready blog posts autonomously

## What I learned
- Multi-agent architecture — specialised agents vs one generalist
- LangGraph — building agent pipelines as stateful graphs
- StateGraph — nodes, edges, entry points, and END
- TypedDict — typed state schemas for safe data flow
- State as shared memory between agents
- Conditional vs sequential edges
- Why specialised agents outperform generalist agents

## Architecture
Topic input
    ↓
Researcher → gathers key facts and statistics
    ↓
Writer → drafts structured blog post
    ↓
Editor → improves quality and engagement
    ↓
Final blog post

## Tech Stack
- LangGraph (agent orchestration)
- Claude Haiku (all three agents)
- langchain-anthropic (LangChain wrapper)

## How to run
1. Clone the repo
2. Create virtual environment and activate it
3. pip install anthropic python-dotenv langgraph langchain-anthropic
4. Create .env with your ANTHROPIC_API_KEY
5. python main.py
6. Enter any blog topic
