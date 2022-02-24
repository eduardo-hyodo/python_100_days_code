class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = None
        print("new being create")

user_1 = User("108", "angela")

print(user_1.id)
print(user_1.username)
print(user_1.followers)
