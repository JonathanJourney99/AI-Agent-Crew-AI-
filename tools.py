from crewai_tools import SerperDevTool
from dotenv import load_dotenv
load_dotenv()
import os


tool = SerperDevTool(api_key=os.getenv('SERPER_API_KEY'))