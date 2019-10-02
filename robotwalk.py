class Robot:        # example of a class declaration in Python

    def _init_(self):
        self.x
        self.y
        self.heading  # 0, 90, 180 or 270 only
        self.name = "Richard"

    def goHome (self ):
        self.x = 0
        self.y = 0

    def  goForward (self, d):
        if self.heading < 0:
            self.heading += 360
        if self.heading == 0:
            self.x = self.x + d
        if self.heading == 90:
            self.y = self.y + d
        if self.heading == 180:
            self.x = self.x - d
        if self.heading == 270:
            self.y = self.y - d

    def displayPosition(self):
        print (' x= ', self.x, '  y = ', self.y)

robotArmy = []
for i in range(10):
    robotArmy.append(Robot())

robotArmy[0].name = "Richard"

for i in range(10):
    robotArmy[i].heading = 0
    robotArmy[i].goHome()
    robotArmy[i].goForward(100)

for i in range(10):
    robotArmy[i].displayPosition()

for i in range(5):
    robotArmy[i].heading = robotArmy[i].heading - 90
    robotArmy[i].goForward(50)

for i in range(10):
    robotArmy[i].displayPosition()

for i in range(10):
    robotArmy[i].heading = robotArmy[i].heading -270
    robotArmy[i].goForward(200)

for i in range(10):
    robotArmy[i].displayPosition()

## x=  100   y =  0
## x=  100   y =  0
## x=  100   y =  0
## x=  100   y =  0
## x=  100   y =  0
## x=  100   y =  0
## x=  100   y =  0
## x=  100   y =  0
## x=  100   y =  0
## x=  100   y =  0
## x=  100   y =  -50
## x=  100   y =  -50
## x=  100   y =  -50
## x=  100   y =  -50
## x=  100   y =  -50
## x=  100   y =  0
## x=  100   y =  0
## x=  100   y =  0
## x=  100   y =  0
## x=  100   y =  0
## x=  300   y =  -50
## x=  300   y =  -50
## x=  300   y =  -50
## x=  300   y =  -50
## x=  300   y =  -50
## x=  100   y =  200
## x=  100   y =  200
## x=  100   y =  200
## x=  100   y =  200
## x=  100   y =  200
