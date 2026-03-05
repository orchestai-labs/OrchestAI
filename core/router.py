def route_task(task):

    task = task.lower()

    if "code" in task or "python" in task:
        return "coding_agent"

    elif "research" in task or "ai" in task:
        return "research_agent"

    else:
        return "general"