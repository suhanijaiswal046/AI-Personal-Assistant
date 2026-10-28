# 

from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

app = Flask(__name__)

# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY not found in your .env file")

# Initialize Groq
client = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=api_key,
    temperature=0.7,
    max_tokens=512
)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    try:
        question = request.form.get("question", "").strip()

        if not question:
            return jsonify({"error": "Please enter a question"}), 400

        response = client.invoke(
            "Act like a helpful personal assistant.\n"
            f"User question: {question}"
        )

        return jsonify({"response": response.content}), 200

    except Exception as e:
        app.logger.exception("Error in /ask")
        return jsonify({"error": str(e)}), 500


@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        email_text = request.form.get("email", "").strip()

        if not email_text:
            return jsonify({"error": "Please enter email text"}), 400

        response = client.invoke(
            "Act like an expert email assistant. "
            "Summarize the following email in 2-3 sentences, "
            "including important details and action items.\n\n"
            f"Email:\n{email_text}"
        )

        return jsonify({"response": response.content}), 200

    except Exception as e:
        app.logger.exception("Error in /summarize")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
