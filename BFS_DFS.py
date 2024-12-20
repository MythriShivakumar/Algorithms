from collections import deque

def BFS_DFS(n, m, s, t, edges):

    result = "no"
    full_graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        full_graph[u].append(v)
        full_graph[v].append(u)
    visted_node = set() 
    connection_queue = deque([s])
    visted_node.add(s)
    while connection_queue:
        current_node = connection_queue.popleft()
        if current_node == t:
            result = "yes"
        for adjacent_node in full_graph[current_node]:
            if adjacent_node not in visted_node:
                visted_node.add(adjacent_node)
                connection_queue.append(adjacent_node)
    return result


def read_input():
    n, m = map(int, input().split())
    s, t = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, m, s, t, edges


if __name__ == "__main__":
    n, m, s, t, edges = read_input()
    result = BFS_DFS(n, m, s, t, edges)
    print(result)
