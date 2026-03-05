from core.orchestrator import handle_task
from core.task_distributor import distribute_task
from core.node_manager import register_node

print("🚀 OrchestAI System Started")

# Test node registration
register_node({
    "system": "local",
    "cpu_cores": 12,
    "ram_gb": 8
})

while True:

    task = input("\nEnter task: ")

    if task.lower() == "exit":
        print("🛑 OrchestAI shutting down...")
        break

    agent_result = handle_task(task)

    print("🤖 Agent Response:", agent_result)

    node_result = distribute_task(task)

    print("🖥 Node Assignment:", node_result)