from queue import Empty


stack=[]
def push():
    stack.append(30)
    stack.append(40)

def pop():
    if stack==Empty:
        print("stack is empty")
    else:
        print("stack is not empty")
        
        stack.pop(40)
        stack.pop(30)