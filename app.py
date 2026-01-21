"""Sample Python client for a local Ollama model built from the Modelfile."""
import ollama

MODEL_NAME = "Dev_assistant"


def chat(prompt: str) -> str:
    """Send a single prompt to the local model and return the reply."""
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]


def main() -> None:
    prompt = "Explain Python decorators in simple terms."
    print(f"Prompt: {prompt}\n")
    reply = chat(prompt)
    print(f"Reply:\n{reply}")


if __name__ == "__main__":
    main()
