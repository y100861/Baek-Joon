import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())

def bfs(start):
    q = deque()
    q.append((start, 1))

    while q:
        x, i = q.popleft()

        if x == b:
            return i

        for v in (2*x, int(str(x)+str(1))):
            if 1<=v<b+1:
                q.append((v, i+1))
    
    return -1

print(bfs(a))