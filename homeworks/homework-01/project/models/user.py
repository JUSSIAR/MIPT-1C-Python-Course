import uuid


class User:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name):
        pass

    def increment_rate(self):
        pass

    def ban_user(self):
        pass

    def unban_user(self):
        pass

    def __repr__(self):
        pass
