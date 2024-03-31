C = int(input())

for _ in range(C):
    A = list(input())
    score = 0
    sum = 0
    for a in A:
        if a == "O":
            sum += 1
        elif a == "X":
            sum = 0
        score += sum
    print(score)