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
        self.__x = xValue

    def setY(self, yValue):
        self.__y = yValue
      
    def setZ(self, zValue):
        self.__z = zValue
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getZ(self):
        return self.__z
