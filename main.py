# Телефонний довідник, з яким працюємо
USERS = {}
# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func (*args, **kwargs)
            return result
        except KeyError:
            return print ("Немає контакта з таким ім'ям")
        except ValueError:
            pass
        except IndexError:
            pass
    return inner   

# Запускаємо каррування - набір функцій з діями та словничок
# Функція рядка з привітанням - після вводу 'hello'
def def_hello():
    return print ('Hello, how can I help you?')

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

# Функція виходу з прощальним рядком - після вводу 'bye', 'exit', 'close'
def def_exit():
    print ('Good bye!')
    return None

COMMANDS = {'hello': ['-', 'почати роботу', def_hello],
            'add': ['<контакт> <номер телефону>', 
                    'додати новий контакт у довідник', def_add],
            'change': ['<контакт> <номер телефону>', 
                       'змінити номер телефону контакта', def_change],
            'phone': ['<контакт>', 
                      'показати телефон контакта із довідника', def_phone],
            'show': ['-', 'показати список усіх контактів з телефонами',
                     def_show],
            'bye': ['-', 'закінчити роботу', def_exit], 
            'close': ['-', 'закінчити роботу', def_exit], 
            'exit': ['-', 'закінчити роботу', def_exit]}

def main():
    print ('')
    print ('Привіт. Я консольний бот-телефонний довідник.')
    print ("У поточній версії я вмію зберігати ім'я користувача та один номер телефону.")
    print ('Команди, що я розумію сьогодні:')
    print ('|{:-^10}|{:-^26}|{:-^44}|'.format ('-', '-', '-'))
    print ('|{:^10}|{:^26}|{:^44}|'.format ('Команда', 'Параметри', 'Опис'))
    print ('|{:-^10}|{:-^26}|{:-^44}|'.format ('-', '-', '-'))
    for command, value in COMMANDS.items():
        print ('|{:<10}|{:^26}|{:<44}|'.format (command, value[0], value[1]))
    print ('|{:-^10}|{:-^26}|{:-^44}|'.format ('-', '-', '-'))
    print ('')
    print ('Параметри треба вводити без углових дужок одним словом через пробіл після')
    print ('команди або іншого параметра.')
    print ('')

    command_from_user = input ('Введіть команду: ').strip().lower().split()
    print (command_from_user)

if __name__ == "__main__":
    main()