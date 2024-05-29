import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

def bfs(start, k):
    cnt = 0
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()

        for v in graph[now]:
            if visited[v[0]] == 0 and (v[1] >= k):
                cnt += 1
                visited[v[0]] = 1
                q.append(v[0])
    
    return cnt

for _ in range(Q):
    visited = [0] * (N + 1)
    k, v = map(int, input().split())
    cnt = bfs(v, k)
    print(cnt)