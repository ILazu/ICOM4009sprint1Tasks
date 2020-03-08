import math

class cartesianPlane:
    def __init__(self,x, y):
        self.setX(x)
        self.setY(y)
    xCoordinate= 0.00
    yCoordinate=0.00
    def setX(self, xValue):
        if xValue < 20:
            self.__x = xValue
        else:
            self.__x = 20

    def setY(self, yValue):
        if yValue < 20:
            self.__y = yValue
        else:
            self.__y = 20
            
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def convertToCartesian(self, r, theta):
        rad = math.radians(theta)
        self.setX(r*math.cos(rad))
        self.setY(r*math.sin(rad))
