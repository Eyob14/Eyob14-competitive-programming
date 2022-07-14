def find_path_bfs(s, e, grid):
    queue = [(s, [])]  # start point, empty path
    visited = set()
    while len(queue) > 0:
        node, path = queue.pop(0)
        path.append(node)
        visited.add((node, v))
        if node == e:
            return path

        adj_nodes = get_neighbors(node, grid)
        for item in adj_nodes:
            if not is_visited(item, v):
                queue.append((item, path[:]))

    return None  # no path found