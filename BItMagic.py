def evenOdd(n):
    if n&1==1:
        print('odd')
    else:
        print("even")

def multiply2(x,y):
    return x<<y

def divide(x,y):
    return x>>y


#evenOdd(4)
#evenOdd(11)
print("ENter 2 numbers seperated by space")
x,y=map(int,input().split())
print(multiply2(x,y))
print(divide(x,y))




