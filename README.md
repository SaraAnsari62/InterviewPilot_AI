# InterviewPilot AI

An LLM-powered interview preparation assistant built with Python, LangChain, OpenAI and Gradio.

## Overview

InterviewPilot AI helps candidates prepare for technical and professional job interviews by generating tailored interview questions, preparation tips and example answers based on their target role and experience level.

## Features

- Role-specific interview preparation
- Technical, behavioral and HR interview categories
- Customizable experience levels
- AI-generated interview questions
- Suggested answers and practical preparation tips
- Interactive web interface

## Technology Stack

- Python
- LangChain
- OpenAI GPT-4.1
- Gradio
- uv (Python package and environment management)

## Architecture

The application uses a LangChain prompt pipeline to structure user input, send requests to an LLM and generate interview preparation content.

## Installation

Clone the repository:

```bash
git clone git@github.com:SaraAnsari62/InterviewPilot_AI.git
cd InterviewPilot_AI
```

Install dependencies:

```bash
uv sync
```

Set your OpenAI API key in your environment or configure your local `.env` file.

Run the application:

```bash
uv run python src/interviewapp.py
```

Open http://127.0.0.1:7860 in your browser.

## Future Improvements

- Interactive mock interview sessions
- Retrieval-Augmented Generation (RAG) for job-specific preparation
- Agentic AI workflows
- Job description analysis
- Personalized interview feedback

## Author

Computer Scientist | Research Software Engineer | AI Engineering

