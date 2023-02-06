def get_class() -> str:
    return input('Укажите номер класса: ').upper()


def get_subject() -> str:
    return input('Введите текущий предмет: ').lower()

def show_journal(db: dict, subject: str):
    print(f'Список учеников ({subject}):')
    print('-----------------------------------')
    for k, v in db.items():
        print('\t', k, '\t', ' '.join(v[subject]))

def get_student() -> str:
    return input('Введите имя ученка для отметки (или "exit" для выхода): ')

def get_mark(student_name: str) -> str:
    return input(f'Введите оценку для {student_name}: ')
