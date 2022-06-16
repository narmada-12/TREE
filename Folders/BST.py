from curses import keyname
from winreg import KEY_CREATE_SUB_KEY


class BST:
 def__init__(self,key):
     self.key=key
     self.lchild=None
     self.rchild=None
     
root=BST(10)
root.lchild=BST(5)
root.rchild=BST(30)
print(root.key)
print(root.lchild)
print(root.rchild)