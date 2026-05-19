from graph import build_graph


def main():
    print("\n" + "="*50)
    print("     MULTI-AGENT BLOG PIPELINE")
    print("="*50)
    print("Researcher → Writer → Editor\n")

    graph = build_graph()

    while True:
        topic = input("Enter blog topic (or 'quit'): ").strip()

        if not topic:
            continue

        if topic.lower() == "quit":
            print("\nGoodbye!")
            break

        print(f"\nProcessing: {topic}")
        print("-"*50)

        initial_state = {
            "topic": topic,
            "research": "",
            "draft": "",
            "final": ""
        }

        result = graph.invoke(initial_state)

        print("\n" + "="*50)
        print("FINAL BLOG POST:")
        print("="*50)
        print(result["final"])

        print("\n" + "="*50)
        print(f"Pipeline complete!")
        print(f"Research: {len(result['research'])} chars")
        print(f"Draft:    {len(result['draft'])} chars")
        print(f"Final:    {len(result['final'])} chars")


if __name__ == "__main__":
    main()