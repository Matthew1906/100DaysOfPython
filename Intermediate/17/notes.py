# 1. Creating classes

# must have content, if we want it empty, we can add pass
class User:
    # __init__ => constructor of class
    # when constructing, must contain the attributes
    def __init__(self, userId, name, age):
        # initialize attributes
        # special built in function
        self.id = userId
        self.username = name
        self.age = age
        self.lives = 3 #we can also initialize starting value
        self.following = 0
        self.follower = 0
    def lose_a_life(self):
        self.lives-=1
    def follow(self, user):
        self.following+=1
        user.follower+=1

user_1 = User('ABC001', 'Matthew',18)
user_2 = User("ABC002", "Tony", 18)
print(user_1.lives)
user_1.lose_a_life()
print(user_1.lives)
user_1.follow(user_2)

#  we can also do sth like this
# user_1.lives = 3
# print(user_1.lives)