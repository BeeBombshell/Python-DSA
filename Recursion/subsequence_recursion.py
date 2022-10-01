def get_all_subsequence(n,output,i):       
    if (i==len(n)):
        if (len(output)!=0):
            print(output)
    else:
        # exclude first character
        get_all_subsequence(n,output,i+1)
 
        # include first character
        output+=n[i]
        get_all_subsequence(n,output,i+1)
    return
 
n = input()
get_all_subsequence(n,"",0)
print(n[0])