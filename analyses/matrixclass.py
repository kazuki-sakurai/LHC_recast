from math import *

class matrix(list):

    def __init__(self,l):
        list.__init__(self,l)
        self.rows = len(self)
        self.columns = len(self[0])
        for row in self:
            if len(row)!=self.columns:
                print "This is not a matrix. Row "
                print row
                print "has different size than others"
                self = None
                return

    

    def __add__(self,m2):

        if m2.rows!=self.rows or self.columns != m2.columns:
            print "Impossible to add matrices"
            return None
        M = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(self[i][j]+m2[i][j])
            M.append(row)
        return matrix(M)
    
            
    def __sub__(self,m2):

        if m2.rows!=self.rows or self.columns != m2.columns:
            print "Impossible to add matrices"
            return None
        M = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(self[i][j]-m2[i][j])
            M.append(row)
        return matrix(M)
       

    def __mul__(self,n):
        M = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(self[i][j]*n)
            M.append(row)
        return matrix(M)
        

    __rmul__ = __mul__

    def __neg__(self):
        return self*(-1)

    def __div__(self,n):
        a = 1./n
        return self*a

    __rdiv__=__div__
    
