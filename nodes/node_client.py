import platform
import psutil
import time
import requests
import uuid

# -------------------------------
# SERVER CONFIG
# -------------------------------

SERVER = "http://127.0.0.1:8000"

REGISTER_URL = SERVER + "/register_node"
GET_TASK_URL = SERVER + "/get_task"


# -------------------------------
# NODE INFO
# -------------------------------

def get_node_info():

    info = {
        "node_id": str(uuid.uuid4()),
        "system": platform.system(),
        "cpu_cores": psutil.cpu_count(),
        "ram_gb": round(psutil.virtual_memory().total / (1024**3), 2)
    }

    return info


# -------------------------------
# REGISTER NODE
# -------------------------------

def register_node(info):

    try:

        r = requests.post(REGISTER_URL, json=info)

        print("📡 Node registered to server:", r.json())

    except Exception as e:

        print("❌ Server connection failed:", e)


# -------------------------------
# GET TASK FROM SERVER
# -------------------------------

def get_task():

    try:

        r = requests.get(GET_TASK_URL)

        data = r.json()

        return data.get("task")

    except Exception as e:

        print("⚠️ Task fetch error:", e)

        return None


# -------------------------------
# TASK EXECUTION
# -------------------------------

def execute_task(task):

    print("\n⚡ Executing task:", task)

    try:

        if isinstance(task, dict) and "task" in task:

            task_text = task["task"]

            # Demo execution
            result = f"Task completed successfully: {task_text}"

        else:

            result = "Invalid task format"

        print("✅ Result:", result)

    except Exception as e:

        print("❌ Execution error:", e)


# -------------------------------
# NODE LOOP
# -------------------------------

def start_node():

    print("\n🚀 OrchestAI Node Started\n")

    node_info = get_node_info()

    print("🖥 Node Info:", node_info)

    register_node(node_info)

    print("\n🟢 Node active and waiting for tasks...\n")

    while True:

        task = get_task()

        if task:

            execute_task(task)

        else:

            print("⏳ No task available...")

        time.sleep(5)


# -------------------------------
# START
# -------------------------------

if __name__ == "__main__":
    start_node()