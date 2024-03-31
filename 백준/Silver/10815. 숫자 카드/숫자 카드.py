import sys

input = sys.stdin.readline

n = int(input())
card_list = list(map(int, input().split()))
card_list.sort()

m = int(input())
num_list = list(map(int, input().split()))

def binary_search(array, target, start, end):
    
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return 1
        
        elif array[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
    
    return 0

for num in num_list:
    print(binary_search(card_list, num, 0, n-1), end=" ")