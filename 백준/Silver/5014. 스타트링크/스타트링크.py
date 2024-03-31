import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

visited = [0] * (f + 1)

def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()

        if now == g:
            break

        for v in (now+u, now-d):
            if v > f or v < 1:
                continue
            
            if visited[v] == 0:
                if v == g:
                    visited[v] = visited[now]
                    break
                visited[v] = visited[now] + 1
                q.append(v)

bfs(s)

if s == g:
    print(0)
elif visited[g] == 0:
    print("use the stairs")
else:
    print(visited[g])