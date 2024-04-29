import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0] * 100001

def bfs(start):
    q = deque()
    q.append([start, 0, [start]])

    if n > k:
        return n-k, [int(x) for x in range(n, k-1, -1)]

    while q:
        now, c, road = q.popleft()

        if now == k:
            return c, road

        for v in (2*now, now+1, now-1):
            if 0<=v<100001 and visited[v] == 0:
                visited[v] = 1
                q.append([v, c + 1, road+[v]])


cnt = 0
cnt, result= bfs(n)
print(cnt)
for r in result:
    print(r, end=" ")