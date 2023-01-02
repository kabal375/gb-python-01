# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from polynomial import create_equation, save2file

def get_equation_from_file(filename: str) -> str:
    with open(filename, 'r') as f:
        eq_str = f.readline().strip()
    return eq_str

def get_factors_from_eq(eq_string: str) -> dict:
    factors_str = eq_string.replace(' ', '').replace('+', ' ').replace('-', ' -').replace('=0', '').lstrip()
    members_list = factors_str.split(' ')
    factors_dict = {}

    for member in members_list:

        if member.find('*x**') > -1:
            f, p = member.split('*x**')
        elif member.endswith('x'):
            f, p = member.split('*x')[0], '1'
        else:
            f, p = member, '0'
        # print (f, p)
        factors_dict[int(p)] = int(f)

    return factors_dict

def find_max_power(dict1: dict, dict2: dict) -> int:

    return max(max(dict2.keys()), max(dict1.keys()))

def sum_dicts (dict1: dict, dict2: dict) -> dict:
    sum_dict = {}
    for i in range(find_max_power(dict1, dict2), -1, -1):
        sum_dict[i] = dict1.get(i, 0) + dict2.get(i, 0)

    return sum_dict

eq_factors1 = get_factors_from_eq(get_equation_from_file('eq1.txt'))
eq_factors2 = get_factors_from_eq(get_equation_from_file('eq2.txt'))

print(eq_factors1)
print(eq_factors2)

sum_eq_factors = sum_dicts(eq_factors1, eq_factors2)

print(sum_eq_factors)

save2file('sum_eq.txt', create_equation(sum_eq_factors))