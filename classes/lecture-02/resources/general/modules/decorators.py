SEPARATOR = '-' * 30


def decor_without_args(callback):
    def wrapper():
        print(SEPARATOR, 'decor_without_args', SEPARATOR, sep='\t')
        print(SEPARATOR, 'START', SEPARATOR, sep='\t')
        callback()
        print(SEPARATOR, 'FINISH', SEPARATOR, sep='\t')
    return wrapper


def level_param(param):
    def decor_with_args(callback):
        def wrapper(arg1, arg2):
            print(SEPARATOR, f'decor_with_args: {arg1}; {arg2}', SEPARATOR, sep='\t')
            print(SEPARATOR, 'START', SEPARATOR, sep='\t')
            callback(arg1, arg2 + param)
            print(SEPARATOR, 'FINISH', SEPARATOR, sep='\t')
        return wrapper
    return decor_with_args


@decor_without_args
def log_hello():
    print('Hello world!')


@decor_without_args
def log_hello1():
    print('Hello world111111')


@level_param(0)
def sum_of_two(arg1, arg2):
    print(f'{arg1} + {arg2} = {arg1 + arg2}')


def example():
    # log_hello()
    # log_hello1()
    # print()

    sum_of_two(3, 4)
    # print()
