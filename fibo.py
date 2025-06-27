def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("Input cannot be a negative number.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == '__main__':
    print(fibonacci_recursive(4))
