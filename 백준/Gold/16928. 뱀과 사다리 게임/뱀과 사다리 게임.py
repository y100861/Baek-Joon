import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

ladder = {}
snake = {}

for i in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for i in range(m):
    u, v = map(int, input().split())
    snake[u] = v

visited = [0] * 101

def bfs(start):
    q = deque([start])

    while q:
        now = q.popleft()
        for i in range(1, 7):
            nx = now + i

            if nx > 100:
                continue

            if nx in ladder:
                nx = ladder[nx]
            if nx in snake:
                nx = snake[nx]
            
            if visited[nx] == 0:
                visited[nx] = visited[now] + 1
                q.append(nx)

bfs(1)
print(visited[100])