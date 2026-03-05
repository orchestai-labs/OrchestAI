from core.node_manager import nodes


def get_best_node():

    if not nodes:
        return None

    best = max(nodes, key=lambda n: n["cpu_cores"])

    return best


def distribute_task(task):

    node = get_best_node()

    if not node:
        return "No nodes available"

    return f"Task '{task}' assigned to node with {node['cpu_cores']} CPU cores"