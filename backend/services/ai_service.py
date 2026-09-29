from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq()


async def generate_questions_intro(job_title, job_description, resume_text):
    SYSTEM_PROMPT = f"""
        You are an AI interview expert who generates interview questions based on
        the candidate's job title, job description, and resume.

        You need to:
        1. Find the candidate's name from the resume.
        2. Generate a short introduction text.
        3. Generate 2-3 interview questions based on the job title,
           job description, and skills mentioned in the resume.

        Input:
            job_title: {job_title}
            job_description: {job_description}
            resume_text: {resume_text}

        Output:
            Return ONLY valid JSON.
            Do not include markdown.
            Do not include ```json.
            Do not include any explanation before or after the JSON.

        Required JSON structure:
        {{
            "questions": ["question 1", "question 2", "question 3"],
            "introText": "Introduction text",
            "candidate_name": "Candidate Name"
        }}

        Rules:

        For Questions:
            - Generate 2-3 questions.
            - Questions should progress from easy to difficult.
            - Consider the candidate's experience and skills.
            - Questions must be relevant to the job title.
            - Questions must be relevant to the job description.
            - Questions must only use skills and technologies mentioned
              in the resume, job description, or job title.
            - Keep questions short and to the point.
            - Some questions can be scenario-based.

        For Introduction Text:
            - It will be played in the browser before the interview starts.
            - Include the candidate's name.
            - Include the job title.
            - Keep it simple and professional.
            - You can add some creativity.

        For Candidate Name:
            - Extract the candidate's name from the resume.
            - If the candidate's name cannot be found, use "Candidate".

        Example:

        Input:
            job_title: Senior Java Developer
            job_description: Candidate should have experience with Core Java,
            Spring Boot and Spring Security.
            resume_text: Name - LoopKaka, Skills: Java, Spring, Node JS, React JS

        Output:
        {{
            "questions": [
                "What is Java?",
                "What is the difference between List and Set?",
                "How would you secure a Spring Boot REST API?"
            ],
            "introText": "Hi LoopKaka, this is your mock interview for the Senior Java Developer role.",
            "candidate_name": "LoopKaka"
        }}
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]
    )

    content = response.choices[0].message.content

    print("\n===== GROQ QUESTIONS RESPONSE =====")
    print(repr(content))
    print("====================================\n")

    return json.loads(content)


async def generate_report(answers=None):
    if answers is None:
        answers = []

    answers_data = [
        {
            "question": a.question,
            "answer": a.answer,
            "skip": a.skip
        }
        for a in answers
    ]

    answers_json = json.dumps(answers_data, indent=2)

    SYSTEM_PROMPT = f"""
You are an expert technical interviewer evaluating a candidate's interview.

Candidate interview data:
{answers_json}

Your task is to evaluate EVERY question and answer individually.

Evaluation philosophy:
- Evaluate the candidate's UNDERSTANDING, not exact wording.
- A relevant and technically correct answer should be considered correct
  even if it is short or does not contain every possible detail.
- Do NOT require the candidate to reproduce an ideal/model answer.
- Do NOT penalize an answer simply because it lacks additional details.
- Different wording or explanation is completely acceptable if the meaning
  is technically correct.
- If the answer demonstrates the main concept correctly, mark it correct.
- If the answer is partially correct but misses an important part, mark it incorrect.
- If the answer is fundamentally wrong, irrelevant, or does not answer the
  question, mark it incorrect.
- If skip is true, mark it incorrect.
- Do not judge grammar or wording unless it makes the technical meaning unclear.

For EACH question:
1. Understand what the question is asking.
2. Read the candidate's actual answer.
3. Determine whether the candidate demonstrates the required understanding.
4. Mark it either CORRECT or INCORRECT.

Scoring:
- correct_answer = number of CORRECT answers.
- total_questions = number of questions.
- score = (correct_answer / total_questions) * 100.
- Round the score to the nearest whole number.
- Never return 0% unless all answers are actually incorrect or skipped.

Output ONLY valid JSON.
Do not include markdown.
Do not include ```json.
Do not include explanations outside the JSON.

Required JSON structure:

{{
    "score": "percentage",
    "correct_answer": 0,
    "improvment_area": [
        "area 1",
        "area 2"
    ]
}}

Rules for improvement areas:
- Provide useful areas based on the candidate's actual weaknesses.
- Do not criticize an answer for missing optional details.
- Do not provide more than 5 improvement areas.
- If the candidate performed well, provide only the most relevant areas for improvement.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]
    )

    content = response.choices[0].message.content

    print("\n===== GROQ REPORT INPUT =====")
    print(answers_json)
    print("=============================\n")

    print("\n===== GROQ REPORT RESPONSE =====")
    print(repr(content))
    print("=================================\n")

    return json.loads(content)
