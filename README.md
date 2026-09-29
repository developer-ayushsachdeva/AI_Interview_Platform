# 🤖 AI Interview Platform

A voice-based AI interview platform that simulates an interactive technical interview using a candidate's **resume, target job role, and job description**.

The platform combines **AI-powered interview generation, Text-to-Speech, Speech-to-Text, and automated evaluation** to create a conversational interview experience.

🔗 **Live Demo:** https://ai-mockinterview-platform.onrender.com/

---

## 🎯 Project Overview

Traditional interview preparation often involves reading questions and typing answers.

This project takes a different approach.

The candidate provides:

* Target Job Role
* Job Description
* Resume

The platform then uses this information to conduct an interactive voice-based interview.

The AI interviewer:

1. Greets the candidate
2. Generates interview questions
3. Speaks the questions using Text-to-Speech
4. Waits for the candidate's spoken response
5. Converts the response using Speech-to-Text
6. Processes and evaluates the response
7. Continues with the next question
8. Generates a final interview report and result

---

## ✨ Key Features

### 📄 Resume-Based Interview

The candidate's resume is provided as context so the interview can be tailored to their background.

### 💼 Job-Specific Interview

The user enters the target job role and job description.

This allows the interview to be conducted in the context of the position being targeted.

### 🔊 Text-to-Speech

Interview questions are converted into speech so the candidate can hear questions from the AI interviewer rather than simply reading them.

### 🎙️ Speech-to-Text

The candidate answers through their microphone.

The spoken response is converted into text for processing and evaluation.

### 🤖 AI-Powered Interview

AI is used to generate interview questions and process candidate responses throughout the interview.

### ⏳ Interactive Interview Flow

The interviewer waits for the candidate's response before continuing.

The interaction follows:

```text
AI asks
   ↓
Candidate listens
   ↓
Candidate speaks
   ↓
Speech-to-Text
   ↓
Response processing
   ↓
AI evaluation
   ↓
Next question
```

### 📊 Final Interview Report

After the interview is completed, the platform presents the final result and generated feedback.

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │       Candidate      │
                    │ Resume + Job Details │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     React Frontend   │
                    └──────────┬───────────┘
                               │
                               │ REST API
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    │       Python         │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
       ┌──────────────────┐        ┌──────────────────┐
       │   AI Integration │        │ Speech Services  │
       │                  │        │                  │
       │ Question         │        │ Text-to-Speech   │
       │ Generation       │        │ Speech-to-Text   │
       │ Evaluation       │        │                  │
       └────────┬─────────┘        └────────┬─────────┘
                │                           │
                └─────────────┬─────────────┘
                              ▼
                    ┌──────────────────────┐
                    │ Interview Controller │
                    │                      │
                    │ Question → Listen →  │
                    │ Answer → Evaluate    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Final Interview      │
                    │ Report & Result      │
                    └──────────────────────┘
```

---

# 🔄 Complete Interview Workflow

```text
Job Role
   +
Job Description
   +
Resume
   ↓
Start Interview
   ↓
AI Greeting
   ↓
Generate Question
   ↓
Text-to-Speech
   ↓
Candidate Hears Question
   ↓
Candidate Speaks
   ↓
Speech-to-Text
   ↓
Response Processing
   ↓
AI Evaluation
   ↓
Generate Next Question
   ↓
Repeat
   ↓
Interview Completed
   ↓
Final Report
   ↓
Result
```

---

# 🛠️ Tech Stack

## Frontend

* React
* JavaScript
* HTML
* CSS

## Backend

* Python
* FastAPI
* REST APIs

## AI

* OpenAI API
* AI-powered question generation
* AI-powered response processing/evaluation

## Voice

* Speech-to-Text
* Text-to-Speech
* Microphone-based candidate interaction

## Development

* Git
* GitHub
* Postman
* VS Code

## Deployment

* Render

---

# 🎯 Why I Built This

Interview preparation is usually focused on question banks and written practice.

I wanted to explore what happens when interview preparation becomes interactive and conversational.

The project was also an opportunity to understand how multiple technologies can work together:

**Frontend + Backend + AI + Voice Processing + Deployment**

rather than treating an AI model as an isolated feature.

---

# 🧠 Key Learning

Building this project helped me gain practical experience with:

* React application development
* FastAPI backend development
* REST API design
* Frontend-backend integration
* AI API integration
* Prompt-based AI workflows
* Speech-to-Text integration
* Text-to-Speech integration
* Microphone-based interaction
* Handling asynchronous application workflows
* Processing user responses
* Deployment of a full-stack application

---

# 🚀 Future Scope

## 1. Adaptive Interviews

Dynamically change question difficulty based on the candidate's previous responses.

```text
Candidate Performance
        ↓
AI Analysis
        ↓
Difficulty Adjustment
        ↓
Next Question
```

---

## 2. Role-Specific Interview Rounds

Support dedicated interview types such as:

* Software Developer
* Backend Developer
* Frontend Developer
* Java Developer
* Python Developer
* Data Analyst
* ML Engineer

---

## 3. Follow-Up Questions

Instead of immediately moving to a completely new question, the interviewer could ask deeper foll
