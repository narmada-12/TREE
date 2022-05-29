#Implementation of queue
queue=[]
def enqueue():
   e=input("enter the element")
   queue.append(e)
   
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        queue.pop[0]
        
def display():
    print(queue)
    
while True:
    print("select the operation 1.add 2.pop 3.display 4.quit")
    choice=int(input( ))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter the correct operation")
        
    
