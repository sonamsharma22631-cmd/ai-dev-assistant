from flask import Flask, request, render_template_string
from utils import explain_code, detect_bug, improve_code, review_code, generate_tests, add_docstrings
from tutor import ai_tutor

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Dev Assistant</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 900px; margin: 40px auto; padding: 0 20px; background: #f5f5f5; }
        h1 { color: #2c3e50; }
        h3 { color: #34495e; }
        textarea, input[type=text] { width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #ccc; font-size: 14px; box-sizing: border-box; }
        button { margin: 5px 5px 5px 0; padding: 10px 18px; border: none; border-radius: 6px; background: #2c3e50; color: white; cursor: pointer; font-size: 14px; }
        button:hover { background: #1a252f; }
        .result { background: white; border-left: 4px solid #2c3e50; padding: 15px; margin-top: 20px; border-radius: 4px; white-space: pre-wrap; font-size: 14px; }
        .section { background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 1px 4px rgba(0,0,0,0.1); }
        hr { border: none; border-top: 1px solid #ddd; margin: 30px 0; }
    </style>
</head>
<body>
    <h1>🤖 AI Dev Assistant</h1>
    <p>Powered by Claude AI — Explain, debug, improve, review, test, and document your code.</p>

    <div class="section">
        <h3>🔧 Code Tools</h3>
        <form method="post">
            <textarea name="code" placeholder="Paste your code here..." rows="10"></textarea><br><br>
            <button name="action" value="explain">📖 Explain</button>
            <button name="action" value="bug">🐛 Detect Bug</button>
            <button name="action" value="improve">⚡ Improve</button>
            <button name="action" value="review">🔍 Full Review</button>
            <button name="action" value="tests">🧪 Generate Tests</button>
            <button name="action" value="docstrings">📝 Add Docstrings</button>
        </form>
    </div>

    <div class="section">
        <h3>🎓 AI Tutor</h3>
        <form method="post">
            <input type="text" name="question" placeholder="Ask any programming question (English or Hindi)..."><br><br>
            <button name="action" value="tutor">💬 Ask Tutor</button>
        </form>
    </div>

    {% if result %}
    <div class="result">
        <strong>Result:</strong><br><br>{{ result }}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        action = request.form.get("action", "")

        if action == "tutor":
            question = request.form.get("question", "").strip()
            result = ai_tutor(question)
        else:
            code = request.form.get("code", "").strip()
            if action == "explain":
                result = explain_code(code)
            elif action == "bug":
                result = detect_bug(code)
            elif action == "improve":
                result = improve_code(code)
            elif action == "review":
                result = review_code(code)
            elif action == "tests":
                result = generate_tests(code)
            elif action == "docstrings":
                result = add_docstrings(code)

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
