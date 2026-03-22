import anthropic
import os


def _get_client() -> anthropic.Anthropic:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set.")
    return anthropic.Anthropic(api_key=api_key)


def _ask_claude(prompt: str) -> str:
    try:
        client = _get_client()
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
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


def explain_code(code: str) -> str:
    if not code.strip():
        return "Please provide some code to explain."
    return _ask_claude(
        f"Explain this code clearly and concisely for a developer. "
        f"Describe what it does, how it works, and any important concepts:\n\n```\n{code}\n```"
    )


def detect_bug(code: str) -> str:
    if not code.strip():
        return "Please provide some code to analyze."
    return _ask_claude(
        f"Analyze this code for bugs, errors, logical issues, and potential problems. "
        f"Be specific about line numbers and explain why each issue is a problem:\n\n```\n{code}\n```"
    )


def improve_code(code: str) -> str:
    if not code.strip():
        return "Please provide some code to improve."
    return _ask_claude(
        f"Suggest concrete improvements for this code covering: "
        f"readability, performance, best practices, and security. "
        f"Show improved version where possible:\n\n```\n{code}\n```"
    )


def review_code(code: str) -> str:
    if not code.strip():
        return "Please provide some code to review."
    return _ask_claude(
        f"Do a full professional code review. Cover: overall structure, "
        f"security concerns, edge cases, error handling, and specific suggestions:\n\n```\n{code}\n```"
    )


def generate_tests(code: str) -> str:
    if not code.strip():
        return "Please provide some code to generate tests for."
    return _ask_claude(
        f"Write comprehensive unit tests for this code using pytest. "
        f"Cover normal cases, edge cases, and error cases:\n\n```\n{code}\n```"
    )


def add_docstrings(code: str) -> str:
    if not code.strip():
        return "Please provide some code to document."
    return _ask_claude(
        f"Add proper docstrings and type hints to this Python code. "
        f"Return the complete updated code:\n\n```\n{code}\n```"
    )
