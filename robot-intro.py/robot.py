class robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)
        print("My color is " + self.color)
        print("My weight is " + str(self.weight))
robot1 = robot("Tom", "red", 30)
robot2 = robot("Jerry", "blue", 40)
robot1.introduce_self()
robot2.introduce_self()