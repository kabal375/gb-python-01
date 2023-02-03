def main_menu() -> int:
    menu_list = ['Показать все контакты',
                 'Открыть файл',
                 'Сохранить файл',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Поиск контакта',
                 'Выход'
                 ]
    print('Главное меню:')
    for i in range(len(menu_list)):
        print(f'{i + 1}. {menu_list[i]}')
    user_input = int(input('Введите номер команды: '))

    return user_input


def show_all(db: list):
    print('Список контактов:')
    for i in range(len(db)):
        user_id = i + 1
        print('\t', user_id, end='. ')
        for v in db[i].values():
            print(f'{v}', end=' ')
        print()


def db_success(db: list, no_message=True) -> bool:
    if db:
        if not no_message:
            print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False


def exit_program():
    print('Завершение программы')
    exit()


def change_contact_form(contact_data=dict(), new=True) -> dict:
    if new:
        print('Создание нового контакта')
    else:
        print('Редактирование данных контакта')
    contact_data['lastname'] = input(f'\tВведите фамилию ({contact_data.get("lastname", "--")}): ')
    contact_data['firstname'] = input(f'\tВведите имя ({contact_data.get("firstname", "--")}): ')
    contact_data['phone'] = input(f'\tВведите телефон ({contact_data.get("phone", "--")}): ')
    contact_data['comment'] = input(f'\tВведите комментарий ({contact_data.get("comment", "--")}): ')
    return contact_data


def press_enter_key():
    print('Нажмите Enter для продолжения...')
    input()


def get_contact_id() -> int:
    try:
        contact_id = int(input('Введите номер контактка: '))
    except ValueError:
        print_error_message(1)

    return contact_id


def print_error_message(err_no: int):
    message: str
    match err_no:
        case 1:
            message = 'Введены некорректные данные'
        case 2:
            message = 'Контакт с таким номером не обнаружен'

    print(message)
    press_enter_key()


def search_request() -> str:
    return input('Введите строку для поиска: ').strip().lower()

def show_filtered(db: list, request: str):
    # print('Список контактов:')
    for i in range(len(db)):
        match_found = False
        user_id = i + 1
        record = db[i].values()
        # print(record)
        for element in record:
            if request in element.lower():
                match_found = True
                break
        if match_found:
            print('\t', user_id, end='. ')
            for v in record:
                print(f'{v}', end=' ')
            print()

