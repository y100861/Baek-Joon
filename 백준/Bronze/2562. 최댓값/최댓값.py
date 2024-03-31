B=[]
while True:
    try:
        A=int(input())
        B.append(A)
    except:
        print(max(B))
        print(B.index(max(B))+1)
        break