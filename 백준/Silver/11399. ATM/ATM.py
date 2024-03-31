n = int(input())

p = list(map(int, input().split()))

p.sort()

time = 0
time_list = []

for i in p:
    time += i
    time_list.append(time)

print(sum(time_list))