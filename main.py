
# Декоратор для обробки помилок
def input_error():
    def inner():
        pass
    return inner   

# Запускаємо каррування - набір функцій з діями та словничок
# Функція обробки додавання нового користувача - після вводу 'add'
def def_add():
    return None

# Функція зміни телефону - після вводу 'change'
def def_change():
    return None

# Функція показу номеру телефону - після вводу 'phone'
def def_phone():
    return None

# Функція виводу всього довідника - після вводу 'show'
def def_show():
    return None

COMMANDS = {'hello': ['-', 'почати роботу'],
            'add': ['<користувач> <номер телефону>', 
                    'додати новий контакт у довідник', def_add],
            'change': ['<користувач> <номер телефону>', 
                       'змінити номер телефону користувача', def_change],
            'phone': ['<користувач>', 
                      'показати номер телефону користувача із довідника', def_phone],
            'show': ['-', 'вивести на екран список усіх контактів з телефонами',
                     def_show],
            'bye': ['-', 'закінчити роботу'], 
            'close': ['-', 'закінчити роботу'], 
            'exit': ['-', 'закінчити роботу']}

def main():
    print ('')
    print ('Привіт. Я консольний бот-телефонний довідник.')
    print ("У поточній версії я вмію зберігати ім'я користувача та один номер телефону.")
    print ('Команди, що я розумію сьогодні:')
    print ('|{:-^10}|{:-^30}|{:-^52}|'.format ('-', '-', '-'))
    print ('|{:^10}|{:^30}|{:^52}|'.format ('Команда', 'Параметри', 'Опис'))
    print ('|{:-^10}|{:-^30}|{:-^52}|'.format ('-', '-', '-'))
    for command, value in COMMANDS.items():
        print ('|{:<10}|{:^30}|{:<52}|'.format (command, value[0], value[1]))
    print ('|{:-^10}|{:-^30}|{:-^52}|'.format ('-', '-', '-'))
    print ('')
    print ('Параметри треба вводити без углових дужок одним словом через пробіл після')
    print ('команди або іншого параметра.')
    print ('')

    command_from_user = input ('Введіть команду: ')
    print (command_from_user)

if __name__ == "__main__":
    main()