import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))
visited = [0] * n

def bfs(start):
    q = deque([start])
    visited[start] = 0

    while q:
        now = q.popleft() # 1

        if now == n - 1:
            return visited[n-1]

        for v in range(1, array[now] + 1):

            if now + v >= n:
                continue

            if visited[now + v] == 0:
                visited[now + v] = visited[now] + 1
                q.append(now + v)
    
    return -1

print(bfs(0))