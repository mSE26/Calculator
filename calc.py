def welcome():
    print('''
Добро пожаловать в калькулятор
''')
welcome()

def calc():
    operation = input('''
Введите математическую операцию, которую вы хотите выполнить:
+ 
- 
* 
/ 
''')

    num1 = int(input('Первая цифра: '))
    num2 = int(input('Вторая цифра: '))

    if operation == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    elif operation == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    elif operation == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    elif operation == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)

    else:
        print('Вы не ввели правильный оператор, запустите программу еще раз.')
    
    again()

def again():
    calc_again = input('''
Хотите еще раз посчитать?
Пожалуйста, введите Y для ДА или N для НЕТ.
''')

    if calc_again.upper() == 'Y':
        calc()
    elif calc_again.upper() == 'N':
        print('До скорого.')
    else:
        again()

calc()