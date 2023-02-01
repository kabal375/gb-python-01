def main_menu() -> int:
    menu_list = ['Показать все контакты',
                 'Открыть файл',
                 'Сохранить файл',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Выход'
                 ]
    print('Главное меню:')
    for i in range(len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')
    user_input = int(input('Введите номер команды: '))

    return user_input


def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print('\t', user_id, end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()


def db_success(db: list) -> bool:
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False


def exit_program():
    print('Завершение программы')
    exit()

def create_contact():
    print('Создание нового контакта')
    new_contact = dict()
    new_contact['lastname'] = input('   Введите фамилию: ')
    new_contact['firstname'] = input('   Введите имя: ')
    new_contact['phone'] = input('   Введите телефон: ')
    new_contact['comment'] = input('   Введите комментарий: ')
    return new_contact
