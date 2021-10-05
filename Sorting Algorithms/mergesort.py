def merge_sort(listt):
    '''
    list->list
    sort the inputed list in O(o*log n) time with O(n) space complexity
    '''
    mid=len(listt)//2
    if(len(listt)>1): #if less than or equal to one then it is already sorted so return the same list in that case
        left=listt[:mid]
        right=listt[mid:]
        merge_sort(left)
        merge_sort(right)

        i=j=k=0

        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                listt[k]=right[j]
                k+=1
                j+=1
            else:
                listt[k]=left[i]
                i+=1
                k+=1
        while(i<len(left)):
            listt[k]=left[i]
            i+=1
            k+=1
        while(j<len(right)):
            listt[k]=right[j]
            j+=1
            k+=1
        return listt

if __name__=='__main__':
    testlist=[0,3,6,4,2,10,7]
    print(merge_sort(testlist))




        