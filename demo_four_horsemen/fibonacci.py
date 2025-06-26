def fibonacci(i):
    if i <= 0:
        return 0
    elif i == 1:
        return 1
    else:
        a = b = 1
        for _ in range(i - 1):
            a, b= b, a + b
        return a
        
for x in range(10):
    print(f'NO.{x} fibonacci number is {fibonacci(x)}')