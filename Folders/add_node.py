# Inserting a element from beginning



class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self):
         self.head=None
    def print_LL(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
              n=self.head
              while n is not None:
                 print(n.data)
    def add_node(self,data):
        n1=Node(data)
        n1.ref=self.head
        n1=self.head
        
ll1=Linkedlist()        
ll1.add_node(10)
ll1.add_node(20)
ll1.print_LL()
    