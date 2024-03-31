import sys

n = int(sys.stdin.readline().rstrip())

num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline().rstrip()))

num_list = sorted(num_list)

for n in num_list:
    print(n)