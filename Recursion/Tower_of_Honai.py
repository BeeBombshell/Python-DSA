#Program to Implement Tower of Honai Puzzel
def TowerofHonai(n, src, dest ,hel):
    if(n==0):
        return
    TowerofHonai(n-1,src,hel,dest)
    print("move from",src,"to",dest)
    TowerofHonai(n-1,hel,dest,src)
    
# n - Number of disks in Source Tower
n = int(input("Enter number of Disks: "))
# A - Source , B - Destination , C - Helper
TowerofHonai(n,'A','C','B')
