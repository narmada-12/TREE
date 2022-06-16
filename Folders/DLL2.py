class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None 
        self.next=None 
        
class DLL:
    
   def __init__(self):
        self.head=None 
    
   def insert_beginning(self,data):
       n=Node(data) 
       temp=self.head 
       temp.prev=n 
       n.next=temp 
       self.head=n
   
        
   def display(self):
       
     if self.head is None:
        print("EMPTY DLL") 
            
     else:
        n=self.head 
        while n is not None:
            print(n.data,"-->",end=" ") 
            n=n.next

L=DLL()      
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2 
L.insert_beginning(5)
L.display()
                 
        