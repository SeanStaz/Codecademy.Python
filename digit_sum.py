def digit_sum(n):
    if n >= 0:
        sum = 0
        while n:
            sum += n % 10
            n /= 10
        else:
            print sum
            return sum
