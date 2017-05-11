#Calculates the factorial of x, so 5! = 1*2*3*4*5 = 120
def factorial(x):
    product = 1
    n = 1
    while n <= x:
        product = product*n
        n += 1
    return product
