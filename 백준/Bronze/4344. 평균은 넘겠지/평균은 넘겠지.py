import sys
C=int(sys.stdin.readline())
for i in range(C):
    N=list(map(int, sys.stdin.readline().split()))
    avg=sum(N[1:])/N[0]
    A=[n for n in N[1:] if n>avg]
    print("{:.3f}%".format(len(A)/N[0]*100))