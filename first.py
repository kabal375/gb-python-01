
# print("Введите А")
a = int(input('a = '))
b = 1.23
s = 'hello world'

c = a ** 2 # возведение в степень

print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')


l = [1, 2, 3, 4]
print (not 2 in l)

my_liat = [(i, (lambda i: i**2)(i)) for i in range(1, 101) if i%2 == 0]

print(my_liat)