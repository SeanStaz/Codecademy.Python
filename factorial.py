"Define a function factorial that takes an integer x as input."

"Calculate and return the factorial of that number."

def factorial(x):
    print "x:", x
    total = 1
    while x >= 1:
        total = total * x
        x = x-1
    print "Total:", total
    return total
