
#-------------------------------------------------------------------------------
class character :

    speed = 10
    lives = 5
    jumpHeight = 2
    attack = 10

    def __init__(self):
        print("Character constructor")

    def walk(self):
        print("Walking")
        print ("His speed is:", self.speed)

    def jump(self):
        print("jumping")
#-------------------------------------------------------------------------------
class mario (character):

    coins = 15
    item = None

    def __init__(self):
        super().__init__()
        self.jumpHeight = 5
        self.attack = 13
        self.jumpHeight = 10
        self.attack = 17

    def walk(self):
        super().walk()
        self.speed = 9
        print("Mario started walking differntly. his speed is:", self.speed)

    def jump(self):
        print("Landing")

    def running(self):
        self.speed = 20
        print("Mario starts running. its speed is now", self.speed)

    def jump(self):
        print ("Jumping sideways")
#-------------------------------------------------------------------------------
characterA= character()
marioX= mario()

print("Character:")
characterA.jump()

print("Mario:")
marioX.walk()
marioX.jump()
