from math import *
def All_Divisors(n):
    l=[]
    for i in range(1,int(sqrt(n)+1)):
        if n%i==0:
            l.append(i)
            l.append(n//i)
    return sorted(l)

t=int(input())
while t:
    n=int(input())
    a=All_Divisors(n)
    print(*a)
    t-=1
