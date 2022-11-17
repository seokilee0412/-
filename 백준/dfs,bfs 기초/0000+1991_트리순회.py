N = int(input())

# tree =[[] for _ in range(N)]
tree = []
V = set()
for _ in range(N):
    e1, e2, e3 = input().split()
    tree.append([e1, e2, e3])
    V.add(e1)
    V.add(e2)
    V.add(e3)
visited = [False] * (N)
path = []
def dfs(vertex, graph, visited):
    if vertex != '.':
        vertex2int = ord(vertex) - ord('A')
        if visited[vertex2int] == False:
            path.append(vertex)
            visited[vertex2int] = True
            for v in graph:
                if v[0] == vertex:
                    if v[1] != '.':
                        left = ord(v[1]) - ord('A')
                        if visited[left] != True:
                            dfs(v[1], graph, visited)
                    if v[2] != '.':
                        right = ord(v[2]) - ord('A')
                        if visited[right] != True:
                            dfs(v[2], graph, visited)


dfs('A', tree, visited)
print(path)

visited = [False] * (N)
path = []
def dfs_2(vertex, graph, visited):
    if vertex != '.':
        vertex2int = ord(vertex) - ord('A')
        if visited[vertex2int] == False:
            path.append(vertex)
            visited[vertex2int] = True
            for v in graph:
                if v[0] == vertex:
                    if v[1] != '.':
                        left = ord(v[1]) - ord('A')
                        if visited[left] != True:
                            dfs(v[1], graph, visited)
                    if v[2] != '.':
                        right = ord(v[2]) - ord('A')
                        if visited[right] != True:
                            dfs(v[2], graph, visited)

def find_root(tree, vertex):
    for v in tree:
        if v[0] == vertex:
            if v[1] != '.':
                find_root(tree, v[1])
            else:
                return 

dfs_2('A', tree, visited)
print(path)
