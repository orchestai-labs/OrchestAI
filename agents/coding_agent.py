def generate_code(task):

    print("💻 Coding Agent started...")

    topic = task.replace("code", "").replace("build", "").strip()

    if not topic:
        topic = task

    result = f"""
💻 Coding Agent Report

Task:
{topic}

Steps:
• Understanding programming requirement
• Designing solution structure
• Generating code logic
• Preparing implementation plan

Result:
Code generation process completed for: {topic}
"""

    return result