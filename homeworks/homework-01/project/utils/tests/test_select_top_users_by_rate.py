from models.user import User
from utils.select_top_users_by_rate import select_top_users_by_rate


def test_select_top_users_by_rate():
    users = [
        User('a'),
        User('b'),
        User('c'),
        User('d'),
        User('e'),
    ]
    users[0].rate = 10
    users[1].rate = 6
    users[2].rate = 22
    users[3].rate = 17
    users[4].rate = 15
    top_size = 3

    received = select_top_users_by_rate(users, top_size)

    assert len(received) == top_size
    assert sorted([
        received[0].rate,
        received[1].rate,
        received[2].rate,
    ]) == [15, 17, 22]