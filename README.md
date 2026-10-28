# 🤖 AI Personal Assistant

An AI-powered personal assistant built with **Python, Flask, and the OpenAI API**. This project provides a web interface for interacting with an AI model and is designed to support question answering and email summarization.

## ✨ Features

- 💬 **AI Question Answering** — Ask questions and receive AI-generated responses.
- 📧 **Email Summarization** — Summarize lengthy emails into concise, readable content.
- 🌐 **Web Interface** — Interact with the assistant through a Flask-powered web application.
- 🔗 **API Integration** — Connect the Flask backend to the OpenAI API.
- 🧩 **Dynamic HTML Templates** — Render web pages using Flask and Jinja2.
- 🔐 **Environment-Based Configuration** — Store API credentials in environment variables instead of hardcoding them.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework and routing |
| OpenAI API | AI-generated responses |
| HTML5 | Web page structure |
| CSS3 | User interface styling |
| JavaScript | Client-side interactions, if implemented |
| Jinja2 | Dynamic HTML templating |
| python-dotenv | Load environment variables |

## 📁 Project Structure

```text
AI-Personal-Assistant/
│
├── main.py                 # Flask application and routes
├── templates/
│   └── index.html          # Web interface
├── static/
│   ├── style.css           # Styles, if present
│   └── script.js           # Client-side logic, if present
├── .env                    # API key (not committed)
├── .gitignore              # Excludes secrets and local files
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

*The structure above is illustrative; adjust the filenames to match your actual repository.*

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/suhanijaiswal046/AI-Personal-Assistant.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Personal-Assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the core dependencies:

```bash
pip install flask openai python-dotenv
```

### 5. Configure Your API Key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Replace the placeholder with your own API key.

**Security:** Never commit your `.env` file or expose your API key in source code, screenshots, or public repositories.

### 6. Run the Application

```bash
python main.py
```

Open the local URL displayed in your terminal, commonly:

```text
http://127.0.0.1:5000/
```

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `OPENAI_API_KEY` | API credential used to authenticate OpenAI API requests |

An API key and sufficient API usage quota are required for requests to the OpenAI API.

## 🧠 How It Works

1. The user opens the assistant in a web browser.
2. Flask serves the HTML interface through the template system.
3. The user submits a question or text to summarize.
4. The backend processes the request and calls the OpenAI API.
5. The generated response is returned to the web interface.

## 🎯 Learning Outcomes

This project provides practical experience with:

- Building a web application using Flask.
- Creating routes and handling form submissions.
- Integrating a third-party AI API.
- Managing API credentials using environment variables.
- Rendering HTML templates with Jinja2.
- Connecting frontend interactions to backend logic.

## 🔮 Future Improvements

- Add conversation history and contextual responses.
- Support email summarization with customizable summary lengths.
- Improve input validation and error handling.
- Add loading indicators and clearer API error messages.
- Deploy the application to a cloud hosting platform.
- Add automated tests and application logging.

## 👩‍💻 Author

**Suhani Jaiswal**

- GitHub: [@suhanijaiswal046](https://github.com/suhanijaiswal046)
- Project: [AI-Personal-Assistant](https://github.com/suhanijaiswal046/AI-Personal-Assistant)

---

⭐ If you find this project useful, consider starring the repository.

