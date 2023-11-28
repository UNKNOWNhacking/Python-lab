a = 18.0
try:
    b = int(input('Enter a number: '))
    ans = a / b
    print(f'Answer is: {ans}')
except (ZeroDivisionError, ValueError):
    print('Please enter number greater than zero')
