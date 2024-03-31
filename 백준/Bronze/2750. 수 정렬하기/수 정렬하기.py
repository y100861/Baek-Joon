n = int(input())

num_list = []

for _ in range(n):
    num_list.append(int(input()))

num_list.sort()

for n in num_list:
    print(n)