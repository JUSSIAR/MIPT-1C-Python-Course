import pytest

from models.user import User


class TestUser:
    def setup(self):
        self.user = User('user_name')

    def test_edit_name(self):
        self.user.edit_name('other_name')
        assert self.user.name == 'other_name'

    @pytest.mark.parametrize('inc_count', [0, 1, 2, 5])
    def test_increment_rate(self, inc_count):
        for i in range(inc_count):
            self.user.increment_rate()
        assert self.user.rate == inc_count

    def test_ban_user(self):
        self.user.ban_user()
        assert self.user.is_banned

    def test_unban_user(self):
        self.user.ban_user()
        self.user.unban_user()
        assert not self.user.is_banned
