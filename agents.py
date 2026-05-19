import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


def researcher(state):
    print("\n[RESEARCHER] Gathering information...")

    prompt = f"""You are a research specialist. Your job is to gather 
key facts, statistics, and insights about a topic.

Topic: {state["topic"]}

Provide:
1. 5-7 key facts or statistics
2. Current trends and developments
3. Key challenges or opportunities
4. Notable examples or case studies

Be specific and factual."""

    response = llm.invoke(prompt)
    state["research"] = response.content
    print(f"Research complete: {len(state['research'])} characters")
    return state


def writer(state):
    print("\n[WRITER] Drafting blog post...")

    prompt = f"""You are a professional blog writer. Write an engaging 
blog post based on the research provided.

Topic: {state["topic"]}

Research:
{state["research"]}

Write a structured blog post with:
- An engaging title
- Introduction (hook the reader)
- 3-4 main sections with subheadings
- Conclusion with key takeaway
- Target length: 400-500 words"""

    response = llm.invoke(prompt)
    state["draft"] = response.content
    print(f"Draft complete: {len(state['draft'])} characters")
    return state


def editor(state):
    print("\n[EDITOR] Improving the draft...")

    prompt = f"""You are a professional editor. Improve the blog post draft.

Original draft:
{state["draft"]}

Your tasks:
1. Improve the opening hook
2. Make the language more engaging and clear
3. Ensure smooth transitions between sections
4. Strengthen the conclusion
5. Fix any awkward phrasing

Return the complete improved blog post."""

    response = llm.invoke(prompt)
    state["final"] = response.content
    print(f"Editing complete: {len(state['final'])} characters")
    return state