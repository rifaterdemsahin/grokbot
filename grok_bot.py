"""
GrokBot - Proof of Concept (PoC)
First-Principles AI Agent powered by xAI Grok
"""

import os
import sys
from dotenv import load_dotenv

# Load local environment variables from .env
load_dotenv()

def main():
    api_key = os.getenv("XAI_API_KEY")
    base_url = os.getenv("XAI_BASE_URL", "https://api.x.ai/v1")
    model = os.getenv("GROK_MODEL", "grok-2-latest")

    print("=" * 60)
    print("⚡ GrokBot: First-Principles AI Agent")
    print("=" * 60)

    if not api_key or api_key == "xai-your-api-key-here":
        print("\n⚠️  [Setup Required]: XAI_API_KEY not found or is default.")
        print("1. Get your API key from: https://console.x.ai")
        print("2. Add it to a .env file: XAI_API_KEY=\"your_key_here\"")
        print("3. Or run: export XAI_API_KEY=\"your_key_here\"\n")
        print("Simulating local test response for demonstration:\n")
        
        sim_query = sys.argv[1] if len(sys.argv) > 1 else "Why is GrokBot unique from first principles?"
        print(f"User Query: {sim_query}")
        print("\n🤖 [GrokBot (First Principles Simulation)]:")
        print("1. Information Latency: Collapsing time between real-world events and intelligence to near zero using live X telemetry.")
        print("2. Epistemic Integrity: Prioritizing empirical physics and mathematical truth over corporate alignment filters.")
        print("3. Supercomputing Scale: Powered by Memphis Colossus 100k+ liquid-cooled GPU cluster.\n")
        print("=" * 60)
        return

    try:
        from openai import OpenAI
    except ImportError:
        print("\n❌ openai package is not installed. Run:")
        print("   pip install openai python-dotenv")
        sys.exit(1)

    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    query = sys.argv[1] if len(sys.argv) > 1 else "Explain why GrokBot is unique from first principles."

    system_prompt = (
        "You are GrokBot, an AI assistant inspired by Hitchhiker's Guide to the Galaxy. "
        "You reason strictly from first principles. Break problems down to fundamental truths, "
        "eliminate corporate fluff, and deliver witty, mathematically sound, empirical answers."
    )

    print(f"\nUser Query: {query}\n")
    print("🤖 GrokBot is reasoning...\n")

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
            stream=True,
        )

        for chunk in response:
            delta = chunk.choices[0].delta.content or ""
            sys.stdout.write(delta)
            sys.stdout.flush()
        print("\n")
    except Exception as e:
        print(f"\n❌ Error communicating with xAI API: {e}")

if __name__ == "__main__":
    main()
