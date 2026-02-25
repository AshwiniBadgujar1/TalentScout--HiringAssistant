# 🤖 TalentScout Hiring Assistant

An AI-powered interview screening assistant that automates candidate evaluation by generating technical questions, rating answers, and storing results.

Built using Gradio UI and local LLM integration.

---

## 🚀 Features

- Collect candidate details
- Upload resume
- Generate technical interview questions based on tech stack
- Evaluate answers automatically using AI
- Calculate final rating
- Store candidate data in Excel
- Simple recruiter-ready workflow

---

## 🧠 Tech Stack

- Python
- Gradio (UI)
- Pandas
- Ollama (Local LLM)
- Excel for data storage

---

## 🌐 Application Modes

This project includes two versions of the application:

### 🖥️ Local Version — `app.py`

Runs only on your machine for development and testing.

Launch:

python app.py

App will open at:

http://127.0.0.1:7860

---

### 🌍 Public Share Version — `app1.py`

Generates a temporary public link using Gradio’s share feature.

Launch:

python app1.py

This will create:

- Local URL
- Temporary public URL accessible from any device

⚠️ Note:
The public link works only while the app is running.

---

## 📦 Installation

### 1️⃣ Clone the repository

git clone https://github.com/your-username/talentscout-hiring-assistant.git

cd talentscout-hiring-assistant

---

### 2️⃣ Create virtual environment (recommended)

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 3️⃣ Install dependencies

pip install -r requirements.txt

---

### 4️⃣ Install & run Ollama (required for AI)

Download Ollama from:
https://ollama.com

Pull the model used in this project:

ollama pull phi

Start Ollama before running the app.

---

## ▶️ How to Run

### Local Mode

python app.py

---

### Public Demo Mode

python app1.py

---

## 📁 Project Structure

TalentScout-Hiring-Assistant/
│
├── app.py              # Local version
├── app1.py             # Public share version
├── resumes/            # Uploaded resumes
├── candidates_data.xlsx
├── requirements.txt
├── README.md
└── .gitignore

---

## 📊 Workflow

1. Candidate enters details
2. Uploads resume
3. AI generates interview questions
4. Candidate answers questions
5. AI evaluates responses
6. Final score calculated
7. Data saved for recruiter review

---

## 📌 Deployment Note

Current version is designed for local execution.

For permanent online hosting, the app can be deployed on:

- Hugging Face Spaces
- Render
- Railway
- VPS server

---

## 🎯 Use Cases

- Initial candidate screening
- Technical assessment automation
- Recruiter productivity tools
- AI interview assistant demos

---

## 🧑‍💻 Author

TalentScout Hiring Assistant Project

By Ashwini Badgujar
www.linkedin.com/in/ashwini-badgujar2692

---

## 📜 License

MIT License
