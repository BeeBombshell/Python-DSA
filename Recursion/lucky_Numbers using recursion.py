#User function Template for python3


class Solution:
    def lucky(self,n,i):
        if(n%i==0):
            return False
        elif(n<i):
            return True
        p=n-(n//i)
        return self.lucky(p,i+1)
    def isLucky(self, n): 
        #RETURN True OR False
        return self.lucky(n,2)
 
# Driver Code Starts
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends