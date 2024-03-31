B=[]
for i in range(10):
  A=int(input())
  B.append(A)
C={}
for i in B:
  if i%42 in C:
    C[i%42]+=1
  else:
    C[i%42]=1
print(len(C))