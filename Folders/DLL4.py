class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None 
        self.next=None 
        
class DLL:
    
   def __init__(self):
        self.head=None 
    
   def insert_beginning(self,data):
       n1=Node(data) 
       temp=self.head 
       temp.prev=n1 
       n1.next=temp 
       self.head=n1
   
   def inserting_end(self,data):
       n2=Node(data) 
       temp=self.head 
       while temp.next is not None:
           temp=temp.next
       
       temp.next=n2
       n2.prev=temp 
       
   def insert_pos(self,data,pos):
       n1=Node(data)
       temp=self.head
       for i in range(1,2):
           temp=temp.next 
       n1.prev=temp 
       n1.next=temp.next 
       temp.next.prev=n1 
       temp.next=n1
           
           
        
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
#L.inserting_end(5) 
L.insert_pos(40,3)
L.display()
                 
        