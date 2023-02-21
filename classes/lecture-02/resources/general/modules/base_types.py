import sys


def numeric_types():
    b: bool = False
    i: int = 1
    f: float = 2.0
    c: complex = complex(3)

    print(f'{type(b)} - numeric subtype for True/False values')
    print(f'{type(i)} - integer type with unlimited bounds')
    print(f'{type(f)} - type with floating point; info: {sys.float_info}')
    print(f'{type(c)} - type for complex numerating')


def immutable_string():
    print('string is immutable')


def simple_collections():
    list_object = [1, 2, 3]
    print(f'list = {list_object}')

    tuple_object = (1, 2, 3)
    print(f'tuple = {tuple_object}')

    set_object = {1, 2, 3}
    print(f'set = {set_object}')

    dict_object = {'a': 1, 'b': 2, 'c': 3, (9, 5): 3, 5: 4, list_object: 5}
    print(f'dict = {dict_object}')
