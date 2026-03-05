from core.orchestrator import handle_task

print("OrchestAI System Started")

while True:
    task = input("Enter task: ")
    result = handle_task(task)
    print(result)