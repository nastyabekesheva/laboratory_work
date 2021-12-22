graph = [
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1]
]
visited = set()
stack = []
tree = []
def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        print(f"Node : {node}")
        for i in range(len(graph)):
            if graph[i][node] == 1 and graph[i][node] not in visited and graph[i][node] not in stack:
                stack.insert(0, i)
        print(f"Stack : {stack}")
        for neighbour in stack:
            try:
                stack.remove(neighbour)
                tree.append([node, neighbour])
                dfs(visited, graph, neighbour)
            except ValueError as ve:
                tree.append(set([node, neighbour]))
                dfs(visited, graph, neighbour)

def main():
    dfs(visited, graph, 0)
    bintree = [sub for sub in tree if len(set(sub)) == len(sub)]
    for i in bintree:
        print(f"{i[0]} -> {i[1]}")
    

main()
