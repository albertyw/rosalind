# Calculate fibonacci numbers

def fibo(num):
    first = 0
    second = 1
    if num == 0:
        return first
    elif num == 1:
        return second
    for i in range(2, num+1):
        current = first + second
        first = second
        second = current
    return current

if __name__ == "__main__":
    import sys
    index = int(sys.argv[1])
    print fibo(index)
