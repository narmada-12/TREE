class BST:
  def __init__(self,key):
      self.key=key
      self.lchild=None
      self.rchild=None
      
def insert(self,data):
    if self.key==data:
        return
    if self.key is None:
        self.key=data
        return 
    if self.key>data:
        if self.lchild is None:
            self.lchild= BST(data)
        else:
             self.lchild.insert(data)
    else:
        if self.rchild is None:
            self.rchild=BST(data)
            
        else:
             self.rchild.insert(data)
    root=BST(10)
    list=[5,6,9,8,20,10]
    for i in list:
        root.insert(i)
            
     
        
      