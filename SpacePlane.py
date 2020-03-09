import math

class SpacePlane:
    def __init__(self,x, y, z):
        self.setX(x)
        self.setY(y)
        self.setZ(z)
        
    xCoordinate= 0.00
    yCoordinate=0.00
    zCoordinate=0.00
    
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
      
    def setZ(self, zValue):
        self.__z = zValue
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getZ(self):
        return self.__z
