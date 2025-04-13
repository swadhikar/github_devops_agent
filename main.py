import os

from pydantic_ai import Agent
from dotenv import load_dotenv
from github_tools import get_repo_summary

load_dotenv()
# create agent with GitHub tool
agent = Agent(
    model=os.getenv('MODEL_GEMINI_1_FLASH'),
    tools=[get_repo_summary],
    system_prompt='You are a DevOps assistant that helps to summarize GitHub repositories.'
)

user_input = input('User: ')
while user_input.lower() not in ('exit', 'quit', 'bye'):
    response = agent.run_sync(user_input)
    print(f'Agent: {response.data}')
    user_input = input('User: ')
