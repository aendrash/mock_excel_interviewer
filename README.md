# AI-Powered Excel Mock Interviewer

## 📖 Project Overview

The **AI-Powered Excel Mock Interviewer** is an automated system designed to assess candidates' Microsoft Excel skills efficiently and consistently. As our company rapidly expands its Finance, Operations, and Data Analytics teams, we need a scalable and intelligent solution to evaluate technical proficiency without relying on time-consuming and inconsistent manual interviews.

This project simulates a real-world interview experience by dynamically generating Excel-related questions, evaluating responses, providing feedback, and adjusting difficulty based on performance. At the end of each session, candidates receive a comprehensive report summarizing their strengths and areas for improvement.

---

## 🎯 Problem Statement

- Manual Excel interviews are resource-intensive and inconsistent.
- A scalable, automated solution is needed to screen candidates faster.
- The system must provide a structured interview experience with intelligent evaluation.
- It must handle sessions dynamically, provide feedback, and generate performance reports.

---

## 🚀 Features

✅ Structured multi-turn interview with a conversational flow  
✅ Domain-specific questions tailored to Data Analysis, Finance, or Operations  
✅ Real-time answer evaluation using a language model (LLM)  
✅ Adaptive difficulty based on candidate performance  
✅ Detailed feedback after each question  
✅ Summary report with scoring and explanations  
✅ Resume session management and dynamic state tracking  
✅ Support for next candidate interviews  

---

## 🛠 Technology Stack

- **Ollama API** – LLM integration for question generation and answer evaluation  
- **FastAPI** – Backend framework for managing sessions and API endpoints  
- **Streamlit** – Frontend interface for candidate interaction and feedback  
- **Python** – Programming language powering the entire system  

---

## 📂 Project Structure

```
excel_interviewer_project/
├── backend/
│   ├── __init__.py          # Marks backend as a Python package
│   ├── main.py              # FastAPI app handling API endpoints
│   └── interview_logic.py   # Core logic for question generation, scoring, and saving reports
├── frontend/
│   └── app.py              # Streamlit app for UI and interaction
├── report/                 # Folder where transcripts are saved
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

---

## 📥 Installation Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd excel_interviewer_project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure you have Python 3.8+ installed.

### 3. Run the backend server

```bash
cd backend
uvicorn main:app --reload
```

The backend will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 4. Run the frontend app

```bash
cd frontend
streamlit run app.py
```

The frontend will open in your browser.

---

## ⚙ Environment Variables

You can configure the following environment variables:

- **OLLAMA_URL** – URL of the LLM API (default: http://localhost:11434/api/generate)
- **OLLAMA_MODEL** – Model to use for question generation (default: mistral:7b)
- **MAX_LLM_RETRIES** – Number of retries when contacting the API (default: 2)
- **API_URL** – URL of the FastAPI backend (default: http://127.0.0.1:8000)

You can create a `.env` file or set them in your environment before running the apps.

---

## 📊 Example Prompts

### Question Generation Prompt:
```
You are a knowledgeable Excel interviewer specialized in Data Analysis. The candidate has answered 3 interview questions with 2 correct and 1 wrong answers so far. Ask the next question at difficulty level 5 (0=easy, 10=hard). Provide a clear, practical Excel interview question and an ideal answer as reference.
```

### Evaluation Prompt:
```
You are an expert Excel interviewer evaluator. Given the interview question: "How do you sum values in column B where column A equals 'X'?" and the candidate's answer, evaluate correctness and provide a numeric score between 0 and 1.
```

---

## 📈 Future Improvements

✔ Collect transcripts to refine scoring and question prompts  
✔ Incorporate candidate feedback for better usability  
✔ Integrate with cloud storage for scalability  
✔ Fine-tune models based on real-world data  
✔ Add analytics and reporting dashboards  

---

## 📜 License

This project is for educational purposes and internal use only.

---

## 🙌 Acknowledgments

- Powered by Python, FastAPI, Streamlit, and Ollama.
- Inspired by the need for scalable and intelligent recruitment solutions.

If you encounter any issues or have suggestions, feel free to open an issue or contribute via pull requests!

---

**Need help with deployment or additional features?**

Let me know if you want me to:
✔ Tailor it further for deployment environments (Heroku, Streamlit Cloud, etc.)  
✔ Add sample `.env` file templates or detailed API specs  
✔ Help you push this to GitHub with commit messages and organization guidelines 📂📑✅