class Dog:

    def __init__(self, name):
        self.name = name
        self.moving_distance = 0
        self.food_name = ""

    def eat(self, food_name):
        self.food_name = food_name

    def walk(self):
        self.moving_distance += 2

    def info(self):
        print("이름 : {0}\n먹은 것 : {1}\n이동거리 : {2}".format(
            self.name, self.food_name, self.moving_distance))


happy = Dog("Happy")
happy.eat("apple")
happy.walk()
happy.walk()
happy.info()
