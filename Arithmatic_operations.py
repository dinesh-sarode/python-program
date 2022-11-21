number_1 = input(int('Enter First Number:'))
operation = input('Enter Operation:')
number_2 = input(int('Enter First Number:'))

if operation == '+':
    print('Your Result:', number_1+number_2)

elif operation == '-':
    print('Your Result:', number_1-number_2)

elif operation == '*':
    print('Your Result:', number_1*number_2)

elif operation == '/':
    print('Your Result:', number_1/number_2)

else:
    print('Operation Unknown. Please try with vaild operator.')    


