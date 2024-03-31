S=input()
abc={}
for i in "abcdefghijklmnopqrstuvwxyz":
    abc[i]=-1
    for k in S:
        abc[k]=S.index(k)
    print(abc[i], end=" ")