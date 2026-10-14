def divisible(number, divisor):
    return number % divisor == 0

num = int(input("Enter a number: "))
div = int(input("Enter a divisor: "))

if  divisible(num, div):
    print(f"{num} is divisible by {div}.")
else:
    print(f"{num} is NOT divisible by {div}.")
