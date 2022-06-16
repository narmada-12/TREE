def Binarysearch(list1,key):
    low=0 
    high=len(list1)-1 
    found=False
    while low<=high and not found :
        mid=(low+high)//2
        if key==list1[mid]: 
            found=True
            print("key is found at postion",mid) 
         
        elif key>list1[mid]: 
             low=mid+1 
            
        elif key<list1[mid]:
             high=mid-1 
            
        else:
          print("key is not found") 
        
list1=[1,2,34,46,92,21]
list1.sort() 
key=int(input("enter the value of key ")) 
Binarysearch(list1,key)
            
            
                
            