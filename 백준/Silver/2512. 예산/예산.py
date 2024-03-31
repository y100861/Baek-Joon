import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
m = int(input())

result = 0

start = 0
end = max(array)

if sum(array) <= m:
    result = end

else:
    while start <= end:
        total = 0
        mid = (start + end) // 2

        for x in array:
            if mid >= x:
                total += x
            else:
                total += mid

        if total <= m: 
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
print(result)