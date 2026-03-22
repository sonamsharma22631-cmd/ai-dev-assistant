# AI Dev Assistant 🤖

An open source AI-powered developer assistant built with [Claude API](https://www.anthropic.com/) by Anthropic.

Helps developers **explain**, **debug**, **improve**, **review**, **test**, and **document** their code — plus an integrated **AI Tutor** for beginners (supports English & Hindi).

---

## Features

| Feature | Description |
|---|---|
| 📖 Explain Code | Understand what any code does |
| 🐛 Detect Bug | Find bugs and logical errors |
| ⚡ Improve Code | Get refactoring and performance suggestions |
| 🔍 Full Review | Professional-level code review |
| 🧪 Generate Tests | Auto-generate pytest unit tests |
| 📝 Add Docstrings | Add type hints and docstrings |
| 🎓 AI Tutor | Ask any programming question (English/Hindi) |

---

## Tech Stack

- **AI:** Claude API (`claude-opus-4-5`) by Anthropic
- **Web:** Flask
- **CLI:** Python 3.8+

---

## Installation

```bash
git clone https://github.com/your-username/ai-dev-assistant.git
cd ai-dev-assistant
pip install -r requirements.txt
```

Set your API key:

```bash
# Linux / Mac
export ANTHROPIC_API_KEY=your_api_key_here

# Windows
set ANTHROPIC_API_KEY=your_api_key_here
```

---

## Usage

### Web App
```bash
python app.py
```
Open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### CLI
```bash
python cli.py
```

---

## Project Structure

```
ai-dev-assistant/
├── app.py           # Flask web application
├── cli.py           # Terminal interface
├── utils.py         # Claude API - code tools
├── tutor.py         # Claude API - AI tutor
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Vision & Social Impact

- 🌍 Makes AI coding tools accessible to everyone — free & open source
- 🇮🇳 Supports Hindi-speaking beginners in India
- 🎓 Helps students in rural areas learn programming
- 👐 Welcomes contributors of all skill levels

---

## Roadmap

- [ ] Voice-based tutor (speech input/output)
- [ ] Multi-language support (more Indian languages)
- [ ] VS Code extension
- [ ] GitHub PR review bot

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## License

MIT License — free to use, modify, and distribute.
