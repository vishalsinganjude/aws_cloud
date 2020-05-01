
def factorial(n):
    return 1 if(n == 0 or n == 1) else n * factorial(n-1)

num = int(input("Enter a Num : "))
print("Factorial of", num, "is", factorial(num))

# Recursiv and One line Solution (Using Ternary operator) and Iterative