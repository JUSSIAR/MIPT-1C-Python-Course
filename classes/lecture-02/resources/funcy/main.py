# https://pypi.org/project/funcy/
from funcy import (
    ilen,
    lfilter
)


def try_ilen():
    gen = (i for i in range(5))
    print(ilen(gen))


def try_lfilter():
    gen = (i for i in range(5))
    print(lfilter(lambda x: x & 1, gen))


if __name__ == '__main__':
    try_ilen()
    try_lfilter()
