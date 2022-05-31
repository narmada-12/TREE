

from tempfile import tempdir


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None 
        
    def insert_node(self,data):
        nb=Node(data)
        nb.next=self.head 
        self.head=nb
        
        
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head 
        while temp.next is not None:
            temp=temp.next
        temp.next=ne 
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next 
            
        np.data=data
        np.next=temp.next
        temp.next=np
               
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
LL1=LL()
n=Node(10)
LL1.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
LL1.insert_node(20)
LL1.insert_node(40)
LL1.insert_end(50)
LL1.insert_end(60)
LL1.insert_position(4,60)
LL1.display()
