A, B=map(int, input().split())
C=""
D=""
E=[]
for a in reversed(str(A)):
    C+=a
    E+=[int(C)]
for b in reversed(str(B)):
    D+=b
    E+=[int(D)]
print(max(E))