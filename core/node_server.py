from fastapi import FastAPI
from core.node_manager import register_node, nodes

app = FastAPI()

# task storage
tasks = []


@app.get("/")
def home():
    return {"status": "OrchestAI Node Server Running"}


# -------- NODE REGISTRATION --------

@app.post("/register_node")
def register(node: dict):

    register_node(node)

    return {
        "message": "Node registered",
        "total_nodes": len(nodes)
    }


# -------- CLUSTER INFO --------

@app.get("/cluster_info")
def cluster():

    total_cpu = sum(n["cpu_cores"] for n in nodes)
    total_ram = sum(n["ram_gb"] for n in nodes)

    return {
        "nodes": len(nodes),
        "total_cpu": total_cpu,
        "total_ram": total_ram
    }


# -------- DASHBOARD --------

@app.get("/dashboard")
def dashboard():

    total_cpu = sum(n["cpu_cores"] for n in nodes)
    total_ram = sum(n["ram_gb"] for n in nodes)

    return {
        "nodes_online": len(nodes),
        "total_cpu_cores": total_cpu,
        "total_ram_gb": total_ram,
        "tasks_in_queue": len(tasks)
    }


# -------- TASK SYSTEM --------

@app.post("/add_task")
def add_task(task: dict):

    tasks.append(task)

    return {
        "message": "Task added",
        "total_tasks": len(tasks)
    }


@app.get("/get_task")
def get_task():

    if tasks:
        task = tasks.pop(0)
        return {"task": task}

    return {"task": None}