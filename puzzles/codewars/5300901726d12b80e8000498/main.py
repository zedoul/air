def _fizzbuzz(n):
    ret = n
    if n % 3 == 0:
        ret = "Fizz"
    if n % 5 == 0:
        ret = "Buzz"
    return ret

def fizzbuzz(n):
    # your code here
    return [_fizzbuzz(i) for i in range(1,n+1)]
