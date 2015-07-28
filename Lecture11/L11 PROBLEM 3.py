##class Weird(object):
##    def __init__(self, x, y): 
##        self.y = y
##        self.x = x
##    def getX(self):
##        return x 
##    def getY(self):
##        return y
##
##class Wild(object):
##    def __init__(self, x, y): 
##        self.y = y
##        self.x = x
##    def getX(self):
##        return self.x 
##    def getY(self):
##        return self.y
##
##X = 7
##Y = 8
##
##w1 = Weird(X, Y)
##print w1.getX()


class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self,other):
        assert type(other) == type(self)
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getYeval()




##a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"  
##  
##b = eval(a)  
##  
##b  
##Out[3]: [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]  
##  
##type(b)  
##Out[4]: list  
##  
##a = "{1: 'a', 2: 'b'}"  
##  
##b = eval(a)  
##  
##b  
##Out[7]: {1: 'a', 2: 'b'}  
##  
##type(b)  
##Out[8]: dict  
##  
##a = "([1,2], [3,4], [5,6], [7,8], (9,0))"  
##  
##b = eval(a)  
##  
##b  
##Out[11]: ([1, 2], [3, 4], [5, 6], [7, 8], (9, 0))  










    
        
    
