import os
from dotenv import load_dotenv
from groq import Groq
from ollama import chat

load_dotenv()

GROQ_API = os.getenv("groq_api")

if not GROQ_API:
    raise ValueError("groq_api is not set in environment variables.")

print("Environment loaded.")


class Office:
    def __init__(self):
        self.groq_client = Groq(api_key=GROQ_API)

    def ollama_respond(self, model: str, system_prompt: str, history: str, speaker_name: str) -> str:
        prompt = (
            f"Here is the conversation so far:\n\n{history}\n\n"
            f"Now write {speaker_name}'s reply. "
            f"Write ONLY the message — no name prefix, no quotes, no stage directions. "
            f"2–4 sentences max."
        )
        response = chat(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            think=False,
        )
        return response.message.content

    def groq_respond(self, model: str, system_prompt: str, history: str, speaker_name: str) -> str:
        prompt = (
            f"Here is the conversation so far:\n\n{history}\n\n"
            f"Now write {speaker_name}'s reply. "
            f"Write ONLY the message — no name prefix, no quotes, no stage directions. "
            f"2–4 sentences max."
        )
        completion = self.groq_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.9,
            max_completion_tokens=300,
        )
        return completion.choices[0].message.content

    def read_policy(self) -> str:
        with open("Policy.md", "r") as f:
            return f.read()

    def read_position(self, path: str) -> str:
        with open(path, "r") as f:
            return f.read()
