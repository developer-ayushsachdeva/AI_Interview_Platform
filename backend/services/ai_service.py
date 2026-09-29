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


async def generate_report(answers=[]):
    SYSTEM_PROMPT = f"""
        You are an expert AI interviewer who analyzes candidate answers
        based on the questions and provides feedback.

        Input:
            {answers}

        Input Structure:
            answers is an array containing objects.

            Each object contains:
                - question: string
                - answer: string | None
                - skip: bool

            If the user skips a question:
                answer will be None
                skip will be True

            If the user answers:
                skip will be False

        Output:
            Return ONLY valid JSON.
            Do not include markdown.
            Do not include ```json.
            Do not include any explanation before or after the JSON.

        Required JSON structure:
        {{
            "score": "percentage",
            "correct_answer": 0,
            "improvment_area": [
                "area 1",
                "area 2"
            ]
        }}

        Rules:
            - Calculate the score as:
              (correct answers / total questions) * 100
            - Do not be overly strict when evaluating answers.
            - Consider an answer correct if the candidate has answered
              at least 70% of the expected information.
            - Provide useful feedback.
            - "improvment_area" should contain no more than 5 points.
            - If the candidate did not answer anything:
                score = "0%"
                correct_answer = 0
                improvment_area should still provide relevant
                improvement areas.
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

    print("\n===== GROQ REPORT RESPONSE =====")
    print(repr(content))
    print("=================================\n")

    return json.loads(content)