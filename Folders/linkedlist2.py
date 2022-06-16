#linear search for duplicate value: 
list2=[]
flag=False 
def search(key,list1):
    for i in range(len(list1)):
        if key==list1[i]:
            flag=True 
            list2.append(i) 
            
    if flag==True:
        for j in list2:
          print("Element is found at position:") 
          print(j)
          
    else:
        print("Element not found") 
        
list1=[1,2,34,1,42,8] 
key=int(input("enter the value of key"))
search(key,list1)