import sys

input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
a_list.sort()

m = int(input())
b_list = list(map(int, input().split()))

def binary_search(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
    
    return None

for b in b_list:
    result = binary_search(a_list, b, 0, n-1)
    if result != None:
        print(1)
    else:
        print(0)