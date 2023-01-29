# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def encode_word(word: str) -> str:
    lcounter = 1
    current_letter = word[0]
    encoded_word = ''
    for i in range(1, len(word)):
        letter = word[i]
        if letter == current_letter:
            lcounter += 1
        else:
            encoded_word += str(lcounter) + current_letter
            lcounter = 1
            current_letter = letter
    encoded_word += str(lcounter) + current_letter
    return encoded_word


def decode_word(word: str) -> str:
    decoded_word = ''
    for i in range(0, len(word), 2):
        decoded_word += int(word[i]) * word[i + 1]
    return decoded_word


def get_data_from_file(filename="initial_data.txt") -> list:
    data_list = []
    with open(filename, 'r') as f:
        for line in f:
            data_list.append(line.split())
    return data_list


def save_data(data_list: list, filename="encoded_data.txt"):
    with open(filename, 'w') as f:
        for lines in data_list:
            f.write(" ".join(lines) + '\n')


def encode_data(initial_data: list) -> list:
    return [list(map(encode_word, lines)) for lines in initial_data]


def decode_data(encoded_data: list) -> list:
    return [list(map(decode_word, lines)) for lines in encoded_data]


data_list = get_data_from_file()
encoded_data_list = encode_data(data_list)
print(data_list)
print(encoded_data_list)
save_data(encoded_data_list)

decoded_data_list = decode_data(encoded_data_list)
print(decoded_data_list)
save_data(decoded_data_list, "decoded_data.txt")
