import os
from typing import List

try:
    import openai
except ImportError:  # openai is optional
    openai = None


def generate_script(topic: str, lines: int = 4) -> List[str]:
    """Generate an inspirational short script.

    Args:
        topic: The topic or keyword for inspiration.
        lines: Desired number of lines in the script (3-6).

    Returns:
        List of strings, each representing one line.
    """
    lines = max(3, min(6, lines))

    api_key = os.getenv("OPENAI_API_KEY")
    if openai and api_key:
        openai.api_key = api_key
        prompt = (
            f"Write {lines} short inspirational lines about '{topic}'. "
            "Keep each line under 15 words." 
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        text = response.choices[0].message.content.strip()
        return [l.strip() for l in text.splitlines() if l.strip()]

    # Fallback if OpenAI is unavailable
    default = [
        f"Embrace the spirit of {topic}.",
        "Believe in your inner strength.",
        "Each step forward is progress.",
        "Let your heart guide the way.",
    ]
    return default[:lines]
