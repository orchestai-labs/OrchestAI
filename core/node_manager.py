nodes = []


def register_node(node_info):

    nodes.append(node_info)

    print("Node registered:", node_info)


def get_cluster_info():

    total_cpu = sum(node["cpu_cores"] for node in nodes)
    total_ram = sum(node["ram_gb"] for node in nodes)

    return {
        "nodes": len(nodes),
        "total_cpu": total_cpu,
        "total_ram": total_ram
    }