journal_db = dict()
journal_path: str


def read_db(path: str) -> dict:
    global journal_db

    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            line = line.strip().split('#')
            marks = line[1].split('|')
            mark_dict = {}
            for item in marks:
                markset = item.split(':')
                mark_dict[markset[0]] = markset[1].split(',')
            journal_db[line[0]] = mark_dict
        # print(journal_db)


def save_db(path: str):
    global journal_db
    with open(path, 'w', encoding='UTF-8') as file:
        for k, v in journal_db.items():
            line = str(k) +'#'
            subline = []
            for s, m in v.items():
                subline.append(s + ':' + ','.join(m))
            line += '|'.join(subline)
            file.write(line + '\n')
