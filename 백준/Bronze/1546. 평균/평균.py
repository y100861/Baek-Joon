N=int(input())
score=list(map(int, input().split()))
new_score=[]
for n in score:
  new_score.append(n/max(score)*100)
print(sum(new_score)/N)