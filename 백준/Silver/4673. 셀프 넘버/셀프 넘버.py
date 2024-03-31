def quiz(n):
    input_1=[]
    input_2=[]
    input_3=[]
    for i in range(1, n+1):
        input_2+=[i]
        A=i%10
        B=i%100
        C=i%1000
        if 1000<=i<10000:
            new_n=i+i//1000+C//100+(C%100)//10+(C%100)%10
        if 100<=i<1000:
            new_n=i+i//100+B//10+B%10
        if 1<=i<100:
            new_n=i+i//10+A
        input_1+=[new_n]
    for k in set(input_2)-set(input_1):
        input_3+=[k]
        input_3.sort()
    for j in input_3:
        print(j)
quiz(10000)