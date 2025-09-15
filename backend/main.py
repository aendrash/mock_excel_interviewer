from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
from datetime import datetime
import backend.interview_logic as interview_logic

app = FastAPI()

sessions = {}


class StartRequest(BaseModel):
    name: str
    email: str
    domain: str


class AnswerRequest(BaseModel):
    session_id: str
    answer: str


@app.post("/start")
def start_interview(data: StartRequest):
    domain = data.domain.strip().lower()
    if domain not in ['data analysis', 'finance', 'operation']:
        raise HTTPException(status_code=400, detail="Invalid domain")

    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "name": data.name,
        "email": data.email,
        "domain": domain,
        "history": [],
        "difficulty": 5,
        "num_asked": 0,
        "num_correct": 0,
        "num_wrong": 0,
        "finished": False
    }
    question, correct_answer = interview_logic.generate_question(
        sessions[session_id]["domain"],
        sessions[session_id]["difficulty"],
        sessions[session_id]["num_asked"],
        sessions[session_id]["num_correct"],
        sessions[session_id]["num_wrong"]
    )
    sessions[session_id]["current_question"] = question
    sessions[session_id]["correct_answer"] = correct_answer
    sessions[session_id]["num_asked"] = 1

    return {
        "session_id": session_id,
        "question": question,
        "question_number": sessions[session_id]["num_asked"]
    }


@app.post("/answer")
def answer_question(data: AnswerRequest):
    session = sessions.get(data.session_id)
    if not session or session.get("finished"):
        raise HTTPException(status_code=404, detail="Session not found or interview finished")

    score, explanation = interview_logic.evaluate_answer(
        data.answer,
        session["correct_answer"],
        session["current_question"]
    )

    session["history"].append({
        "question": session["current_question"],
        "user_answer": data.answer,
        "correct_answer": session["correct_answer"],
        "score": float(score),
        "explanation": explanation
    })

    # Update difficulty counters
    if float(score) > 0.7:
        session["num_correct"] += 1
        if session["difficulty"] < 10:
            session["difficulty"] = min(10, session["difficulty"] + 1)
    elif float(score) < 0.4:
        session["num_wrong"] += 1
        if session["difficulty"] > 0:
            session["difficulty"] = max(0, session["difficulty"] - 1)

    # Finish interview after 10 questions
    if session["num_asked"] >= 10:
        session["finished"] = True
        finished_time = datetime.now()
        interview_logic.save_transcript(
            session["name"],
            session["email"],
            session["history"],
            session["domain"],
            session["num_asked"],
            session["num_correct"],
            session["num_wrong"],
            finished_time
        )
        final_score = (session["num_correct"] / session["num_asked"]) * 100 if session["num_asked"] else 0

        return {
            "finished": True,
            "score_summary": {
                "asked": session["num_asked"],
                "correct": session["num_correct"],
                "wrong": session["num_wrong"],
                "final_score_percent": round(final_score, 2)  # ✅ Added this key
            },
            "history": session["history"]
        }

    # Otherwise increment and continue
    session["num_asked"] += 1
    question, correct_answer = interview_logic.generate_question(
        session["domain"],
        session["difficulty"],
        session["num_asked"],
        session["num_correct"],
        session["num_wrong"]
    )
    session["current_question"] = question
    session["correct_answer"] = correct_answer

    return {
        "finished": False,
        "score": float(score),
        "explanation": explanation,
        "next_question": question,
        "question_number": session["num_asked"]
    }


@app.post("/exit")
def exit_interview(data: AnswerRequest):
    session = sessions.get(data.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    session["finished"] = True
    finished_time = datetime.now()
    interview_logic.save_transcript(
        session["name"],
        session["email"],
        session["history"],
        session["domain"],
        session["num_asked"],
        session["num_correct"],
        session["num_wrong"],
        finished_time
    )
    final_score = (session["num_correct"] / session["num_asked"]) * 100 if session["num_asked"] else 0

    return {
        "finished": True,
        "score_summary": {
            "asked": session["num_asked"],
            "correct": session["num_correct"],
            "wrong": session["num_wrong"],
            "final_score_percent": round(final_score, 2)  # ✅ Already present here
        },
        "history": session["history"]
    }
