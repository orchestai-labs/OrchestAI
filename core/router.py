def route_task(task):

    task = task.lower()

    # coding related tasks
    coding_keywords = [
        "code", "python", "program", "build", "script",
        "software", "function", "api", "bug", "debug",
        "algorithm", "develop"
    ]

    # research related tasks
    research_keywords = [
        "research", "study", "analysis", "learn",
        "data", "information", "explain", "investigate"
    ]

    # AI generation tasks
    ai_keywords = [
        "ai", "generate", "create", "story",
        "write", "text", "content"
    ]

    for word in coding_keywords:
        if word in task:
            return "coding_agent"

    for word in research_keywords:
        if word in task:
            return "research_agent"

    for word in ai_keywords:
        if word in task:
            return "ai_agent"

    return "general"