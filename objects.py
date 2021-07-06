

class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduceSelf(self):
        print("My name is", self.name)


robot1 = Robot("Max", "red", 23)

robot1.introduceSelf()
