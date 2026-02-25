import gradio as gr
import pandas as pd
import ollama
import os
from datetime import datetime

EXCEL_FILE = "candidates_data.xlsx"
RESUME_FOLDER = "resumes"
os.makedirs(RESUME_FOLDER, exist_ok=True)

# -------- OLLAMA CALL --------
def ask_phi(prompt):
    response = ollama.chat(
        model="phi:latest",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


# -------- GENERATE QUESTIONS --------
def generate_questions(tech_stack):
    prompt = f"""
Generate exactly 5 interview questions for a candidate skilled in:
{tech_stack}

Return only numbered questions.
"""
    result = ask_phi(prompt)
    questions = [q.strip() for q in result.split("\n") if q.strip()]
    return questions[:5]


# -------- RATE ANSWER --------
def rate_answer(question, answer):
    prompt = f"""
Rate this answer from 0 to 10.

Question: {question}
Answer: {answer}

Return only a number.
"""
    score = ask_phi(prompt)

    try:
        return float(score.strip())
    except:
        return 5.0


# -------- SAVE RESUME --------
def save_resume(file):
    if file is None:
        return "No Resume"

    filename = os.path.basename(file.name)
    path = os.path.join(RESUME_FOLDER, filename)

    with open(file.name, "rb") as src:
        with open(path, "wb") as dst:
            dst.write(src.read())

    return filename


# -------- GENERATE QUESTIONS BUTTON --------
def step1(name, email, phone, role, exp, location, tech, resume):

    filename = save_resume(resume)
    questions = generate_questions(tech)

    return (
        questions,
        0,
        [],
        filename,
        f"### Question 1:\n{questions[0]}"
    )


# -------- NEXT QUESTION --------
def next_question(answer, q_index, questions, scores):

    if not questions:
        return q_index, scores, "", "⚠️ Generate questions first"

    score = rate_answer(questions[q_index], answer)
    scores = scores + [score]

    q_index += 1

    if q_index >= len(questions):
        return q_index, scores, "", "✅ All questions done. Click Finish."

    return (
        q_index,
        scores,
        "",  # clears answer box
        f"### Question {q_index+1}:\n{questions[q_index]}"
    )


# -------- FINISH INTERVIEW --------
def finish(name, email, phone, role, exp, location, tech, filename, scores):

    if not scores:
        return "⚠️ No answers recorded."

    avg = sum(scores) / len(scores)

    data = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Role": role,
        "Experience": exp,
        "Location": location,
        "Tech Stack": tech,
        "Resume": filename,
        "Final Rating": round(avg, 2),
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    df = pd.DataFrame([data])

    if os.path.exists(EXCEL_FILE):
        old = pd.read_excel(EXCEL_FILE)
        df = pd.concat([old, df], ignore_index=True)

    df.to_excel(EXCEL_FILE, index=False)

    return f"""
## 🎉 Interview Completed

⭐ **Average Score:** {round(avg,2)} / 10

Your resume will be reviewed by the recruiter.
They will contact you soon.

You may close this window now.
"""


# -------- UI --------
with gr.Blocks(theme=gr.themes.Soft()) as app:

    gr.Markdown("# 🤖 TalentScout Hiring Assistant")
    gr.Markdown("👋 Welcome! Please fill your details.")

    with gr.Column():
        name = gr.Textbox(label="Full Name")
        email = gr.Textbox(label="Email")
        phone = gr.Textbox(label="Phone")
        role = gr.Textbox(label="Desired Position")
        exp = gr.Textbox(label="Years of Experience")
        location = gr.Textbox(label="Location")
        tech = gr.Textbox(label="Tech Stack")
        resume = gr.File(label="Upload Resume (PDF)")

    generate_btn = gr.Button("🚀 Generate Questions")

    question_box = gr.Markdown()
    answer_box = gr.Textbox(label="Your Answer")

    next_btn = gr.Button("➡️ Next Question")
    finish_btn = gr.Button("🏁 Finish Interview")

    final_status = gr.Markdown()

    # STATES
    questions_state = gr.State([])
    q_index_state = gr.State(0)
    scores_state = gr.State([])
    resume_file_state = gr.State("")

    generate_btn.click(
        step1,
        inputs=[name, email, phone, role, exp, location, tech, resume],
        outputs=[
            questions_state,
            q_index_state,
            scores_state,
            resume_file_state,
            question_box
        ]
    )

    next_btn.click(
        next_question,
        inputs=[answer_box, q_index_state, questions_state, scores_state],
        outputs=[
            q_index_state,
            scores_state,
            answer_box,
            question_box
        ]
    )

    finish_btn.click(
        finish,
        inputs=[name, email, phone, role, exp, location, tech, resume_file_state, scores_state],
        outputs=final_status
    )

app.launch(share=True)