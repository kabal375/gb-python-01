import view
import model
def start_program():
    class_no = view.get_class()
    # class_no = '7B'
    set_path(class_no)
    model.read_db(model.journal_path)
    subject = view.get_subject()
    # subject = 'математика'
    view.show_journal(model.journal_db, subject)
    # student = ''

    while True:
        student = view.get_student()
        if student.lower() == 'exit':
            break
        if student in model.journal_db.keys():
            mark = view.get_mark(student)
            if int(mark) in [1, 2, 3, 4, 5]:
                add_mark(model.journal_db, subject, student, mark)
            else:
                print('Некорректная отметка!')
        else:
            print('Такой ученик не найден!')
        view.show_journal(model.journal_db, subject)

    model.save_db(model.journal_path)


def set_path(class_no: str):
    model.journal_path = class_no + '.txt'

def add_mark(db: dict, subject: str, student_name: str, mark: str):
    # current_marks = dict()
    current_marks = db.get(student_name)
    current_marks_list = current_marks.get(subject)
    current_marks_list.append(mark)
    current_marks[subject] = current_marks_list
    db[student_name] = current_marks




