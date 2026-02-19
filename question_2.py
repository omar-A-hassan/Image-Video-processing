def fact(n):
    if n == 0 or n == 1:
       return 1
    else:
        return n * fact(n-1)
    

while True:
    
    try:

        num = int(input("Enter a positive integer: "))

        if num >= 0 :
            break
        else:
            print("Enter a number greater than zero")
    except ValueError:
        print("Enter a valid whole number")

print(f"Factorial of {num} is {fact(num)}")


