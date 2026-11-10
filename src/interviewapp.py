from dotenv import load_dotenv
import os

# load the environment variables from the .env file, here API_key
load_dotenv(os.path.expanduser("~/.env"))

# Check that the key is available
print("API key loaded:", bool(os.getenv("OPENAI_API_KEY")))

from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
import gradio as gr

# 1. Define the prompt template
interview_prompt = PromptTemplate(
    template="""
You are an experienced technical interviewer and career coach.

Help the user prepare for a job interview.

Target job role: {job_role}
Experience level: {experience_level}
Interview category: {interview_type}

Please provide the following:

## 1. Interview Preparation Tips
Give 5 practical tips specific to this role.

## 2. Potential Interview Questions
Generate 5 relevant questions with a mix of
technical and practical questions where appropriate.

## 3. Suggested Answers
Provide example answers for the questions.
Explain what makes each answer effective.

## 4. Important Skills
List the technical and soft skills the candidate
should demonstrate during the interview.

Make the response structured, professional,
and relevant to the specified role.
""",
    input_variables=[
        "job_role",
        "experience_level",
        "interview_type"
    ]
)


# 2. Initialize the LLM
model = init_chat_model(
    "gpt-4.1",
    model_provider="openai",
    temperature=0.3
)


# 3. Build the LangChain pipeline
chain = interview_prompt | model


# 4. Define the application function
def generate_interview_prep(job_role, experience_level, interview_type):

    if not job_role.strip():
        return "Please enter a job role."

    try:
        response = chain.invoke({
            "job_role": job_role,
            "experience_level": experience_level,
            "interview_type": interview_type
        })

        return response.content

    except Exception as e:
        print("ERROR:", repr(e))
        return f"An error occurred: {str(e)}"

# 5. Build the Gradio interface
demo = gr.Interface(
    fn=generate_interview_prep,

    inputs=[
        gr.Textbox(
            label="Target Job Role",
            placeholder="e.g. AI Engineer, Data Scientist, Python Developer"
        ),

        gr.Dropdown(
            choices=["Entry Level", "Mid Level", "Senior Level"],
            label="Experience Level",
            value="Mid Level"
        ),

        gr.Dropdown(
            choices=[
                "Technical Interview",
                "Behavioral Interview",
                "HR Interview",
                "Mixed Interview"
            ],
            label="Interview Type",
            value="Mixed Interview"
        )
    ],

    outputs=gr.Markdown(label="Interview Preparation"),

    title="InterviewPilot AI",
    description=(
        "Your AI-powered interview preparation assistant. "
        "Generate tailored interview questions, preparation tips "
        "and suggested answers based on your target job role."
    ),

    examples=[
        ["AI Engineer", "Mid Level", "Technical Interview"],
        ["Data Scientist", "Senior Level", "Mixed Interview"],
        ["Python Developer", "Entry Level", "Technical Interview"]
    ]
)


# 6. Launch the application
if __name__ == "__main__":
    demo.launch()
