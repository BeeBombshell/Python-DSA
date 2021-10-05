def fact(n = 5):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)
num = input("Enter a number to get its factorial: ")
if num == 'None' or num == '' or num == ' ':
    print("Factorial of default value is: ",fact())
else:
    print("Factorial of number is: ",fact(int(num)))
