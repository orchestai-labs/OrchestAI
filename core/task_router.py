import requests

SERVER_URL = "http://127.0.0.1:8000/add_task"


def send_task(task):

    try:

        r = requests.post(SERVER_URL, json={"task": task})

        return "Task sent to OrchestAI cluster"

    except:

        return "Cluster connection failed"