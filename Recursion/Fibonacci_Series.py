def fib(n):
     if n == 0:
          return 0
     elif n == 1:
          return 1
     else:
          return fib(n-1) + fib(n-2)
num = int(input("Enter no. of terms of fibonacci series: "))
print("Fibonacci series of",num,"terms :-")
for i in range(1,num+1):
     print(fib(i),end = ' ')
