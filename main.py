# Телефонний довідник, з яким працюємо
USERS = {}
# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func (*args, **kwargs)
            return result
        except KeyError:
            print ('Невідома помилка KeyError. Спробуй іншу команду')
        except ValueError:
            print ('Невідома помилка ValueError. Спробуй іншу команду')
        except IndexError:
            print ('Недостатньо параметрів для запису/зміни/виводу контакта\n')
        except TypeError:
            print ('Невідома помилка TypeError. Спробуй іншу команду')
    return inner   

# Запускаємо каррування - набір функцій з діями та словничок
# Функція рядка з привітанням - після вводу 'hello'
def def_hello(*args):
    return print ('Hello, how can I help you?\n')

# Функція обробки додавання нового користувача - після вводу 'add'
@input_error
def def_add(list): # Список, що ввів юзер, окрім команди. Цікавить 1-й і 2-й ім'я + номер
    if list[0].title() in USERS.keys():
        return print ('Такий контакт існує. Спробуйте команду "change"\n')
    else:
        USERS.update ({list[0].title(): list[1]})
        return print ('Контакт успішно додано\n')

# Функція зміни телефону - після вводу 'change'
@input_error
def def_change(list): # Список, що ввів юзер. Цікавить 2-й і 3-й ім'я + номер
    if list[0].title() in USERS.keys():
        USERS [list[0].title()] = list[1]
        return print ('Контакт успішно обновлений\n')
    else:
        return print ('Такого контакту не існує. Спробуйте команду "add"\n')

# Функція показу номеру телефону - після вводу 'phone'
@input_error
def def_phone(list): # Список, що ввів юзер. Цікавить другий ел - ім'я
    return print (f'Номер телефону {list[0].title()}: \
{USERS.get(list[0].title(), "Наразі такого контакту не існує")}\n')

# Функція виводу всього довідника - після вводу 'show'
def def_show(*args):
    print ('|{:-^20}|{:-^26}|'.format ('-', '-'))
    print ('|{:^20}|{:^26}|'.format ("Ім'я", 'Номер телефону'))
    print ('|{:-^20}|{:-^26}|'.format ('-', '-'))
    for name, number in USERS.items():
        print ('|{:<20}|{:<26}|'.format (name, number))
    print ('|{:-^20}|{:-^26}|'.format ('-', '-'))
    print ('')
    return None

# Функція виходу з прощальним рядком - після вводу 'bye', 'exit', 'close'
def def_exit(*args):
    return print ('Good bye!\n')

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

@input_error
def get_handler(command):
    try:
        return COMMANDS[command][-1]
    except:
        return print ('Така команда наразі не підтримується. Спробуй іншу\n')

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
    print ('команди або іншого параметра.\n')

    while True:
        command_from_user = input ('Введіть команду: ').strip().lower().split()
        handler = get_handler(command_from_user[0])
        try:
            handler (command_from_user[1:])
        except TypeError:
            continue
#        print (USERS)
        if command_from_user[0] in ['exit', 'close', 'bye']:
            break

if __name__ == "__main__":
    main()