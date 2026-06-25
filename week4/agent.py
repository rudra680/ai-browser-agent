import os

from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools import navigate_to, click_element, type_text

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

agent = create_agent(
    model=llm,
    tools=[
        navigate_to,
        click_element,
        type_text
    ]
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Open github.com"
            }
        ]
    }
)

print(result)