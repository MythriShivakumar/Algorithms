def solve(n, m, edges):
    # ----------------------------- #
    infinity = float('inf')
    shortest_distances = [infinity] * n
    shortest_distances[1] = 0  
    for i in range(n - 1): 
        for from_vertex, to_vertex, weight in edges:
            if shortest_distances[from_vertex - 1] + weight < shortest_distances[to_vertex - 1] and shortest_distances[from_vertex - 1] != infinity:
                shortest_distances[to_vertex - 1] = shortest_distances[from_vertex - 1] + weight
    if shortest_distances[n - 1] != infinity:
        shortest_path = shortest_distances[n - 1]
    else:
        shortest_path = 'INFINITY'
    # ----------------------------- #
    return {
        'shortest_path': shortest_path # you should set this field to the length of the shortest path between nodes 2 and n.
        ### don't forget to put "INFINITY" in case there is no valid path from node 2 to node n.
    }


def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    return n, m, edges


if __name__ == "__main__":
    n, m, edges = read_input()
    res = solve(n, m, edges)
    print(res['shortest_path'])
