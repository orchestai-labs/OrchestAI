from agents.research_agent import research
from agents.coding_agent import generate_code
from core.router import route_task


def handle_task(task):

    agent = route_task(task)

    if agent == "research_agent":
        return research(task)

    elif agent == "coding_agent":
        return generate_code(task)

    else:
        return "OrchestAI received task: " + task