
import view
import model


def input_handler(inp: int):
    match inp:
        case 1:
            # показать справочник
            view.show_all(model.db_list)
        case 2:
            # открыть файл базы
            model.read_db('database.txt')
            view.db_success(model.db_list)
        case 3:
            # показать справочник
            pass
        case 4:
            # Новый контакт
            # TODO get и set для базы
            model.db_list.append(view.create_contact())
        case 5:
            # показать справочник
            pass
        case 6:
            # показать справочник
            pass
        case 7:
            # Выход
            # TODO проверка на сохранение изменений
            view.exit_program()

def start_program():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)




