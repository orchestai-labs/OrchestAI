from agents.research_agent import research
from agents.coding_agent import generate_code

def handle_task(task):

    task = task.lower()

    if "research" in task:
        return research(task)

    elif "code" in task or "python" in task:
        return generate_code(task)

    else:
        return "OrchestAI received task: " + task