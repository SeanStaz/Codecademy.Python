"Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits."

"For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4."

"(Assume that the number you are given will always be positive.)"

def digit_sum(n):
    if n >= 0:
        sum = 0
        while n:
            sum += n % 10
            n /= 10
        else:
            print sum
            return sum
