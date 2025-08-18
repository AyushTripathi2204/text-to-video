import os
from dotenv import load_dotenv
load_dotenv()  # Loads .env file, must be called before using os.environ.get()!

from openai import OpenAI

# 1. Try both possible environment variables, fail fast if neither is set
openrouter_key = os.environ.get("OPENROUTER_API_KEY")
openai_key = os.environ.get("OPENAI_API_KEY")
api_key = openrouter_key or openai_key

if not api_key:
    raise RuntimeError(
        "No API key found! Set OPENROUTER_API_KEY or OPENAI_API_KEY in your .env file."
    )

# 2. Use OpenRouter endpoint by default
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

def generate_manim_code(prompt):
    system_prompt = (
        "You are an expert Python/Manim code writer. For any math, science, or algorithm prompt, return only a single Python code block "
        "defining a Manim Scene class called 'PromptScene' (for Manim CE 0.19+).\n"
        "- Your code must create an animated visual scene that teaches, explains, demonstrates, or helps discover the answer, based on the prompt.\n"
        "- Use diagrams, shapes, MathTex, graphs, etc. as needed.\n"
        "- Label all graphics clearly.\n"
        "- For non-visual or text-based concepts, show relevant information as animated text.\n"
        "- The code must be ready to copy-paste and render with 'manim -pql'.\n"
        "Do not include any explanation or text outside the code block."
    )
    user_msg = f'Prompt: "{prompt}", interpret visually for general education use.'

    response = client.chat.completions.create(
    model="openai/gpt-4o",  # <-- Use the valid model name!
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_msg}
    ],
    max_tokens=700,
    temperature=0.3,
)

    return response.choices[0].message.content
