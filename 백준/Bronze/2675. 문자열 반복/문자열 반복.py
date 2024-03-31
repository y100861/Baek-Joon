T=int(input())
for i in range(T):
    A, B=input().split()
    for k in B:
        print(int(A)*k, end="")
    print()