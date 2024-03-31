import sys
from collections import deque

sys.setrecursionlimit(10000)

input = sys.stdin.readline

n, k = map(int, input().split())
max_num = 100001

visited = [0] * max_num 

def bfs(start):
    q = deque([start])

    while q:
        v = q.popleft()

        if v == k:
            break

        for i in (v-1, v+1, 2*v):
            if 0<=i<max_num and visited[i] == 0:
                visited[i] = visited[v] + 1
                q.append(i)


bfs(n)

print(visited[k])