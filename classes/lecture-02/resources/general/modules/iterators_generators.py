from tqdm import tqdm


# Iterator - объект, поддерживающий функцию next() для взятия следующего.
# Generator - iterator, элементы которого можно пройти только однажды.


# Пример работы генератора
def generator_example():
    generator_list = [item for item in range(33, 45)]
    print(f'Generated list: {generator_list}')
    # print(f'Generated list: {generator_list}')

    generator = (i for i in range(1, 4))
    print(f'first time we have: {sum(generator)}')
    print(f'second time there is an empty sum: {sum(generator)}', end='\n\n')

    generator = (item ** 2 for item in range(1, 5))
    print('first time we can iterate this one: ')
    for item in generator:
        print(item, end='\t')
    print('\nbut no any more times((')
    for item in generator:
        print(item, end='\t')


# Польза generator - не храним все это дело в памяти.
def generator_profit_example():
    long_arr_generator = (item for item in range(10 ** 9))
    for _ in tqdm(long_arr_generator):
        pass
    print('It was too long, but it works!')


# Кастомный генератор range
def custom_range(start, finish, step):
    if step == 0:
        return

    less = lambda x, y: x < y
    greater = lambda x, y: x > y
    relation = less if step > 0 else greater

    while relation(start, finish):
        yield start
        start += step


# Тестим кастомный генератор range
def test_custom_range():
    print(custom_range(0, 0, 0))

    cr = custom_range(3, 11, 2)
    print(next(cr))
    print(next(cr))


# Итерируемый объект - объект элементы которого можно обойти и его можно преобразовать к итератору.
def iterator_object():
    iter_object = [10, 20, 40, 80]
    list_iterator = iter(iter_object)
    print(f'first value by iter: {next(list_iterator)}')
    print(f'second value by iter: {next(list_iterator)}')
