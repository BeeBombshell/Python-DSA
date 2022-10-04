'''A recursive Python program to check whether a string is palindrome or not'''

def isPalindrome(s, i):
    if(i > len(s)/2):  #base case
       return True
    ans = False
    if((s[i] is s[len(s) - i - 1]) and isPalindrome(s, i + 1)): #recursive step
      ans = True
    return ans
 
str = "racecar"
if (isPalindrome(str, 0)):
    print("Yes")
else:
    print("No")
    
