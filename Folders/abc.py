def comparison(arr2):
    a=0
    b=0
    c=[]
    
    for i in range(len(arr2)):
        for j in range(len(arr2)):
          if arr2[i][j]>arr2[i+1][j]:   
              a+=1
          elif arr2[i][j]<arr2[i+1][j]:
                                       b+=1
          else:
               return None
  
    
    c.append(a)
    c.append(b)
    print(c)
comparison([[5,6,7],[3,6,10]])