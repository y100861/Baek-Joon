import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

# dx = [-1, 1, 0, 0, 1, 1, -1, -1]
# dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y):

    if not (0<=x<h and 0<=y<w):
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x+1, y-1)
        dfs(x+1, y+1)
        dfs(x-1, y-1)
        dfs(x-1, y+1)
        return True
    return False


while True:
    result = 0

    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = [] * w

    for i in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                result += 1

    print(result)