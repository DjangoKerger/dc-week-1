N = int(input("What is your number?"))
factorial = 1

if N == 0:
    print("the factorial of 0 is 1")
else: 
    for i in range(1,N+1):
        factorial = factorial*i
        print(factorial,i)

print(f"The factorial of {N} is: {factorial}")