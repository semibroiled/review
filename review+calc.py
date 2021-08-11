while True:
    x = input('first number: ')
    X = int(x)
    operation= input('Operation: ')
    y = input('second number: ')
    Y = int(y)
    print(operation)
    if operation == '+':
         print(X+Y)
    elif operation == '-':
         print(X-Y)
    elif operation == '*':
         print(X*Y)
    elif operation == '/' :
         print(X/Y)
    else:
        print('Idk man kinda sus')
