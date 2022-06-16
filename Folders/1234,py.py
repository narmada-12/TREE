class Solution:
    def __init__(self):
        pass
    def countKdivPairs(self, arr, n, k):
        count=0
        for i in range(len(arr)):
         if arr[i]+arr[i+1]/k==0:
             print(i)
s=Solution()
s.countKdivPairs([2, 2, 1, 7, 5, 3],6,4)
       