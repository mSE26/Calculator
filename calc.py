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

else:
    print('Вы не ввели правильный оператор, запустите программу еще раз.')