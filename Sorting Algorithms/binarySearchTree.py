#---BST Alogrithm-----
def binarysearch(A,min,max,key):
    if max<min:
        return False
    else:
        mid=((min+max)//2)
        if A[mid]>key:
            return binarysearch(A,min,mid-1,key)
        elif A[mid]<key:
            return binarysearch(A,mid+1,max,key)
        else:
            return mid
    

#--main---
A=[]
print("Enter sorted array: ")

for i in range(0,5):
    x=int(input())
    A.append(x)

print(A)
k= binarysearch(A,0,len(A)-1,20)
print("Key is located in index: ",k)
