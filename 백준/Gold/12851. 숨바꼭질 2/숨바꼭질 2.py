import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0] * 100001

def bfs(start):
    cnt = 0
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()

        if now == k:
            cnt += 1
        
        for v in (now-1, now+1, 2*now):
            if 0<=v<100001 and (visited[v] == 0 or visited[v] == visited[now] + 1):
                visited[v] = visited[now] + 1
                q.append(v)
    return cnt

cnt = bfs(n)

print(visited[k] - 1)
print(cnt)