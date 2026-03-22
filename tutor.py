import anthropic
import os


def _get_client() -> anthropic.Anthropic:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set.")
    return anthropic.Anthropic(api_key=api_key)


def ai_tutor(question: str) -> str:
    if not question.strip():
        return "Please ask a question."
    try:
        client = _get_client()
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": (
                    "You are a friendly coding tutor for beginners. "
                    "Answer clearly in simple English (or Hindi if the user writes in Hindi). "
                    "Give examples wherever helpful. Keep answers beginner-friendly.\n\n"
                    f"Question: {question}"
                )
            }]
        )
        return message.content[0].text
    except ValueError as e:
        return f"Configuration Error: {str(e)}"
    except anthropic.APIConnectionError:
        return "Error: Could not connect to Claude API. Check your internet connection."
    except anthropic.AuthenticationError:
        return "Error: Invalid API key. Please check your ANTHROPIC_API_KEY."
    except anthropic.RateLimitError:
        return "Error: Rate limit exceeded. Please wait a moment and try again."
    except Exception as e:
        return f"Unexpected error: {str(e)}"
