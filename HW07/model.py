db_list = []

def read_db(path: str) -> list:
    # global db_list
    db_list = []
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)
    return db_list

def save_data(db: list, path='database.txt'):
    with open(path, 'w', encoding='UTF-8') as file:
        for record in db:
            file.write(';'.join(list(record.values())) + '\n')
