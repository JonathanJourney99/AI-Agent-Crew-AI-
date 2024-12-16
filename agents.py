from crewai import Agent, LLM
from tools import tool  
from dotenv import load_dotenv
import os


load_dotenv()

llm = LLM(
    model="gemini/gemini-pro", 
    verbose=True,
    temperature=0.5,
    api_key=os.getenv("GOOGLE_API_KEY")
)


news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory=False,  
    backstory=(
        "Driven by curiosity, you're at the forefront of "
        "innovation, eager to explore and share knowledge that could change "
        "the world also your are a great inventor in ideas."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)


news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=False, 
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)


print("Agents initialized successfully!...........")
