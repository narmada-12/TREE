factorial=1
def fact(n):
    if n<0:
        print("factorial not exist")
        
    elif n==0:
        print("factorial of number is 1")
    
    else: 
        n>0
        for i in range(1,n+1):
            factorial1=i*factorial
        print("factorial number is",factorial1)
        
fact(5)