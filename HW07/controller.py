import view
import model


def input_handler(inp: int):
    match inp:
        case 1:
            # показать справочник
            view.show_all(model.db_list)
            view.press_enter_key()
        case 2:
            # открыть файл базы
            model.read_db('database.txt')
            view.db_success(model.db_list, False)
        case 3:
            # сохранить файл
            pass
        case 4:
            # Новый контакт
            model.db_list.append(view.change_contact_form())
        case 5:
            # Изменить контакт
            edit_contact(model.db_list)
        case 6:
            # Удалить контакт
            pass
        case 7:
            # Выход
            # TODO проверка на сохранение изменений
            view.exit_program()


def start_program():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)


def get_contact(db: list, id: int) -> dict:
    if view.db_success(db):
        return db[id]

def set_contact(db: list, id: int, contact_data: dict):
    db[id] = contact_data


def edit_contact(db: list):
    if view.db_success(db):
        contact_id = view.get_contact_id() - 1
        if contact_id > -1:
            try:
                contact_data =  db[contact_id]
            except IndexError:
                view.print_error_message(2)
                contact_data = dict()
        else:
            view.print_error_message(1)
            contact_data = dict()
        if contact_data:
            contact_data = view.change_contact_form(contact_data, False)
            set_contact(db, contact_id, contact_data)

