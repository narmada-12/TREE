#linear search 
def search(list,key):
    for i in range(len(list)):
        if key==list[i]:
            print("Data is found at position",i) 
            break 
        
    else:
        print("Data is not found") 
        
list=[1,2,3,6,9]
print(list) 
search(list,int(input("enter the value of key ")))