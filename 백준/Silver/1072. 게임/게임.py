import sys

input = sys.stdin.readline

x, y = map(int, input().split())
z = (100 * y) // x

start = 0
end = x
result = 0

if  z >= 99:
    print(-1)

else:
    while start <= end:
        mid = (start + end) // 2

        if ((100 * (y + mid)) // (x + mid)) > z:
            result = mid
            end = mid - 1

        else:
            start = mid + 1

    print(result)