from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from tools import (
    get_student_info,
    get_student_marks,
    calculator,
    get_passing_rules,
)

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

tools = [
    get_student_info,
    get_student_marks,
    calculator,
    get_passing_rules,
]

agent = create_agent(
    model=model,
    tools=tools,
)

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    print("\nAgent:", result["messages"][-1].text)