from . import schema


class Users:
    def __init__(self) -> None:
        self.user = {}

    def set(self, users: schema.Users):
        self.user[users.username] = users.dict()

    def get(self):
        return self.user


users = Users()
