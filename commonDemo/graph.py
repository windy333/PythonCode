# 邻接矩阵
graph = {
    1: [(2, 3), (3, 4)],
    2: [(3, 5), (4, 2), (5, 4)],
    3: [(4, 3)],
    4: [(5, 1)],
    5: []
}

# 深度搜索
def dfs(source, target, current_s, shortest_s, visited, current_path, shortest_path):
    # 剪枝
    if current_s >= shortest_s:
        return shortest_s

    # 标记
    visited.add(source)

    # 更新
    if source == target:
        shortest_s = current_s
        shortest_path.clear()
        shortest_path.extend(current_path)

    # 遍历
    for neighbor, distance in graph[source]:
        if neighbor not in visited:
            current_path.append(neighbor)
            shortest_s = dfs(neighbor, target, current_s + distance, shortest_s, visited, current_path, shortest_path)
            current_path.pop()

    # 回溯
    visited.remove(source)
    return shortest_s

# 存储所有点到点5的最短距离和路径
shortest_ss = {}
shortest_paths = {}
target_node = 5

for source_node in graph.keys():
    if source_node != target_node:
        initial_distance = 0
        initial_shortest_s = float('inf')
        visited_nodes = set()
        current_path = [source_node]
        shortest_path = []

        shortest_path_distance = dfs(source_node, target_node, initial_distance, initial_shortest_s, visited_nodes, current_path, shortest_path)

        if shortest_path_distance == float('inf'):
            shortest_ss[source_node] = "没有找到从节点 {} 到节点 {} 的路径。".format(source_node, target_node)
            shortest_paths[source_node] = []
        else:
            shortest_ss[source_node] = shortest_path_distance
            shortest_paths[source_node] = shortest_path

for node in graph.keys():
    if node != target_node:
        print("节点 {} 到节点 {} 的最短路径距离为：{}".format(node, target_node, shortest_ss[node]))
        print("最短路径为：", shortest_paths[node])