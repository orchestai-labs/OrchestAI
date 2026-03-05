from fastapi import FastAPI

app = FastAPI()

# task queue
tasks = []


@app.get("/")
def home():
    return {"status": "OrchestAI Server Running"}


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