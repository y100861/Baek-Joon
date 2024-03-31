S=input().upper()
A=["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
cnt=0
for s in S:
    for i, element in enumerate(A):
        if s in element:
            cnt+=i+3
print(cnt)