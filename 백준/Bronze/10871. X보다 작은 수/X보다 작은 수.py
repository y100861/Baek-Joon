import sys
N, X=map(int, sys.stdin.readline().split())
A=map(int, input().split())
for i in list(A):
  if i<X:
    print(i)