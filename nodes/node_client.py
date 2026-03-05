import platform
import psutil
import time


def get_node_info():

    info = {
        "system": platform.system(),
        "cpu_cores": psutil.cpu_count(),
        "ram_gb": round(psutil.virtual_memory().total / (1024**3), 2)
    }

    return info


def start_node():

    print("OrchestAI Node Started")

    node_info = get_node_info()

    print("Node Info:", node_info)

    while True:
        print("Node waiting for tasks...")
        time.sleep(10)


if __name__ == "__main__":
    start_node()