# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


def get_fibonacci_list(n, nega = False):
    res_list = []
    for i in range(n+1):
        if i == 0:
            res_list.append(0);
        elif i == 1:
            res_list.append(1)
        elif not nega:
            res_list.append(res_list[i - 2] + res_list[i - 1])
        else:
            res_list.append(res_list[i - 2] - res_list[i - 1])


    return res_list

n = 8

f_list = get_fibonacci_list(n)
fn_list = get_fibonacci_list(n, True)

fn_list.reverse()

print(fn_list + f_list[1:])