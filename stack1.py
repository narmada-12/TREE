stack=[]
def push():
    element=input("ENTER THE ELEMENT IN THE STACK")
    stack.append(element)
    print(stack)
    
def pop_element():
        if not stack:
            print("Stack is empty")
        else:
            stack.pop()
            print(stack)
while True:
   choice=int(input("enter the input"))
   if choice==1:
     push()
   elif choice==2:
    pop_element()
   else:
    choice==3
    print("Enter a correct value")
