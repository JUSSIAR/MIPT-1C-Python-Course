class AbstractUser:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'User:\tname:{self.name},\tage:{self.age}'


class SystemUser(AbstractUser):
    def __init__(self, name: str, age: int, access: bool):
        super().__init__(name, age)
        self.access = access

    def __buba(self):
        print('buba')

    def __str__(self):
        return f'System {super().__str__()} {"with" if self.access else "without"} access'


class UsersFactory:
    users_count = 0

    @staticmethod
    def create_user(name: str, age: int, **kwargs):
        UsersFactory.users_count += 1
        if 'access' in kwargs:
            return SystemUser(name, age, kwargs['access'])
        return AbstractUser(name, age)

    @staticmethod
    def log_users_count():
        print(f'Total users count is {UsersFactory.users_count}')


def example():
    user1 = UsersFactory.create_user('Igor', 45)
    user2 = UsersFactory.create_user('Oleg', 22, access=False)

    UsersFactory.log_users_count()
    user3 = UsersFactory.create_user('Ivan', 99, access=True)
    UsersFactory.log_users_count()

    # user3._SystemUser__buba()

    print(user1)
    print(user2)
    print(user3)
