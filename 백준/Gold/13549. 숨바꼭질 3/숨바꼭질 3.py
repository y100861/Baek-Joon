import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
MAXRANGE = 100001
visited = [-1 for _ in range(MAXRANGE)]
def bfs(cur):
    q = deque([])
    q.append(cur)
    visited[cur] = 0
    if cur==K:
        return 0
    while q:
        n = q.popleft()
        if n==K:
            return visited[n]
        for next_n in (2*n, n-1, n+1):
            if 0 <= next_n < MAXRANGE and visited[next_n]==-1 and next_n == 2*n:
                q.append(next_n)
                visited[next_n] = visited[n]
            elif 0 <= next_n < MAXRANGE and visited[next_n]==-1 and next_n != 2*n:
                q.append(next_n)
                visited[next_n] = visited[n] +1

print(bfs(N))