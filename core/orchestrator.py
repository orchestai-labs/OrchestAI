from agents.research_agent import research
from agents.coding_agent import generate_code
from agents.ai_agent import ai_generate

from core.router import route_task
from core.task_router import send_task


def handle_task(task):

    # decide which agent will handle the task
    agent = route_task(task)

    result = ""

    if agent == "research_agent":
        result = research(task)

    elif agent == "coding_agent":
        result = generate_code(task)

    elif agent == "ai_agent":
        result = ai_generate(task)

    else:
        result = f"OrchestAI received task: {task}"

    # send task to cluster
    try:
        cluster_status = send_task(task)
    except Exception as e:
        cluster_status = f"Cluster error: {e}"

    response = f"""
==============================
🤖 Agent Response
==============================

{result}

==============================
☁️ Cluster Status
==============================

{cluster_status}
"""

    return response