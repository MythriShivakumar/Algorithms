def get_root(parent, node):
    if parent[node] != node:
        parent[node] = get_root(parent, parent[node]) 
    return parent[node]


def merge_components(parent, rank, u, v):
    root_u = get_root(parent, u)
    root_v = get_root(parent, v)
    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1
        return True
    return False


def solve(n, m, k, edges):
    # ----------------------------- #
    edges.sort(key=lambda edge: edge[2])
    parent = list(range(n)) 
    rank = [0] * n  
    total_weight = 0  
    trees = n  
    for u, v, weight in edges:
        u -= 1  
        v -= 1  
        if merge_components(parent, rank, u, v):
            total_weight += weight  
            trees -= 1  
            if trees == k:
                break
    # ----------------------------- #
    return {
        'total_weight': total_weight  # you should set this field to an appropriate value defined in the problem.
    }


def read_input():
    n, m, k = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    return n, m, k, edges


if __name__ == "__main__":
    n, m, k, edges = read_input()
    res = solve(n, m, k, edges)
    print(res['total_weight'])
