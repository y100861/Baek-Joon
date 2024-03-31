from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for list in graph:
    list.sort()

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)


def dfs(v, visited_dfs):
    visited_dfs[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if visited_dfs[i] == False:
            dfs(i, visited_dfs)


def bfs(v, visited_bfs):
    q = deque()
    q.append(v)
    visited_bfs[v] = True

    while q:
        k = q.popleft()
        print(k, end=" ")

        for i in graph[k]:
            if visited_bfs[i] == False:
                q.append(i)
                visited_bfs[i] = True
            
dfs(v, visited_dfs)
print()
bfs(v, visited_bfs)