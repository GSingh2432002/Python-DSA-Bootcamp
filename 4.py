# Factorial of a number
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
if __name__ == '__main__':
    number = 5
    print(fact(number))