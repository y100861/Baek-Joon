import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

t = int(input())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    if not (0<=x<n and 0<=y<m):
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for r in range(t):
    result = 0

    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

    print(result)