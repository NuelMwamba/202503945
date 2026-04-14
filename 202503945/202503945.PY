def factorial(n):
    if n < 0:
        return "factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
#Function to return Fibonacci Sequence
def fibonacci(n):
    if n <= 0:
        return "Enter a positve number"
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence 
#main program
num = int(input("Enter a positive integer: "))
print("\nFactorial of", num, "is:", factorial(num))
print("Fibonacci sequence up to", num, "term is:", fibonacci(num))    