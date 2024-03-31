import sys
from collections import deque

input = sys.stdin.readline

a, b, n, m = map(int, input().split())

graph = [0] * (max(n, m) + 1)

def bfs(start):
    q = deque([start])

    while q:
        now = q.popleft()

        for v in (now-1, now+1, now-a, now+a, now-b, now+b, now*a, now*b):
            if 0<=v<(max(n, m) + 1) and graph[v] == 0:
                graph[v] = graph[now] + 1
                q.append(v)
    
    return graph[m]

print(bfs(n))