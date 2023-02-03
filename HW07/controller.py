import view
import model


def input_handler(inp: int):
    match inp:
        case 1:
            # показать справочник
            if view.db_success(model.db_list):
                view.show_all(model.db_list)
                view.press_enter_key()
        case 2:
            # открыть файл базы
            model.db_list = model.read_db('database.txt')
            view.db_success(model.db_list, False)
        case 3:
            # сохранить файл
            if view.db_success(model.db_list):
                model.save_data(model.db_list)
        case 4:
            # Новый контакт
            if view.db_success(model.db_list):
                model.db_list.append(view.change_contact_form())
        case 5:
            # Изменить контакт
            if view.db_success(model.db_list):
                edit_contact(model.db_list)
        case 6:
            # Удалить контакт
            if view.db_success(model.db_list):
                delete_contact(model.db_list)
        case 7:
            # Поиск контакта
            view.show_filtered(model.db_list, view.search_request())
            view.press_enter_key()
        case 8:
            # Выход
            temp_db_list = model.read_db('database.txt')
            if model.db_list != temp_db_list:
                print('\tНесохранённые изменения!')
                to_save = input('Введите 1 для сохранения и 0 для отмены: ')
                if to_save:
                    model.save_data(model.db_list)

            view.exit_program()


def start_program():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)


def get_contact(db: list, contact_id: int) -> dict:
    return db[contact_id]

def set_contact(db: list, contact_id: int, contact_data: dict):
    db[contact_id] = contact_data


def edit_contact(db: list):
    contact_id = view.get_contact_id() - 1
    try:
        contact_data = get_contact(db, contact_id)
    except IndexError:
        view.print_error_message(2)
        contact_data = dict()
    if contact_data:
        contact_data = view.change_contact_form(contact_data, False)
        set_contact(db, contact_id, contact_data)

def delete_contact(db: list):
    contact_id = view.get_contact_id() - 1
    try:
        del db[contact_id]
    except IndexError:
        view.print_error_message(2)
