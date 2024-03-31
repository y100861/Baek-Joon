A=int(input())
B=input()
C=list(map(int, B))
for i in reversed(C):
    print(A*i)
print(A*int(B))