
class User:
    user_count = 0

    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress
        User.user_count += 1

    def __del__(self):
        User.user_count -= 1


# user1 = User("ivan", 20, "addr1")
# user2 = User("huan", 30, "addr2")
# user3 = User("juan", 40, "addr3")

# print(User.user_count)
# # 3

# del user3
# print(User.user_count)
# # 3

user1 = User("ivan", 20, "addr1")
user2 = User("huan", 30, "addr2")
user3 = User("juan", 40, "addr3")


users = [user1, user2, user3]
print(len(users))
# 3

users.remove(user3)
print(len(users))
# 2


class User1:
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress

class User2:
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress

# ...

user1 = User1(...)
user2 = User2(...)

# ...
