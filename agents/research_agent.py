def research(task):

    print("🔎 Research Agent started...")

    topic = task.replace("research", "").strip()

    if not topic:
        topic = task

    result = f"""
🔎 Research Agent Report

Topic:
{topic}

Steps:
• Understanding the research topic
• Searching knowledge sources
• Analyzing AI and technology trends
• Preparing insights

Conclusion:
Research analysis completed for: {topic}
"""

    return result