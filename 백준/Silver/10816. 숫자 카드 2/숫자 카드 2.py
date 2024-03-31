import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
card_list = list(map(int, input().split()))
card_list.sort()

m = int(input())
num_list = list(map(int, input().split()))

for num in num_list:
    left_index = bisect_left(card_list, num)
    right_index = bisect_right(card_list, num)

    print(right_index-left_index, end=" ")