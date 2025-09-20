n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))
op = input("Enter your operator:+,-,*,/,//,% - ")

if op == '+':
    result = n1 + n2
    print(result)
elif op == '-':
    result = n1 - n2
    print(result)

elif op == '*':
    result = n1 * n2
    print(result)

elif op == '/':
    result = n1 / n2
    print(result)

elif op == '//':
    result = n1 - n2
    print(result)

elif op == '%':
    result = n1 % n2
    print(result)
else:
    print("Invalid operator")