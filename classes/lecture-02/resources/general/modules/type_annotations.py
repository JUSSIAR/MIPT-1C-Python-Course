# Здесь рассмотрел только эти типы, но есть еще интересные, в т.ч., например, Iterable
from typing import (
    Any,
    Union,
    Callable,
    TypeVar,
    NewType,
    Optional,
    Type, Dict,
)


def typing_examples() -> Dict[str, Callable]:
    # Нужно для подчеркивания, что вернуться может что угодно
    def return_any(flag: bool = True) -> Any:
        return 1.23 if flag else 'string'

    # Нужно для подчеркивания, что вернуться может что угодно из перечисленного
    def return_int_or_bool(flag: bool = True) -> Union[int, bool]:
        return 111 if flag else False

    # Нужно, чтобы обозначить вызываемость возвращаемого объекта
    def return_callable() -> Callable:
        def callback():
            print('I`m callback')

        return callback

    # Нужно для подчеркивания вариативности
    T = TypeVar('T')

    def return_generic_pow2(a: T) -> T:
        return a ** 2

    # Для объявления своего типа
    UID = NewType('UID', int)

    def check_uid(uid: UID) -> bool:
        return uid > 0

    # Нужно, чтобы понимать, что вероятно ничего не вернется(None)
    def return_optional(flag: bool = True) -> Optional[str]:
        if flag:
            return 'string'

    return {
        'return_any': return_any,
        'return_int_or_bool': return_int_or_bool,
        'return_callable': return_callable,
        'return_generic_pow2': return_generic_pow2,
        'check_uid': check_uid,
        'return_optional': return_optional,
    }
