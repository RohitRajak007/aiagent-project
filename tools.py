rom dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()

# Proper search query as a string
search_query = 'AI in healthcare trends 2023'

# Call the tool with the correct argument
result = tool.search(search_query=search_query)