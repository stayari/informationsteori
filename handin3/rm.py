import numpy as np
import math

class RM:
    
    #def __init__(self):
    #    self.r = r
    #    self.m = m


    def g(self, r, m):
        print("This is r{} and this is m{}".format(r,m))
        return self._g(r,m)

    def _g(self, r, m):
        print("recThis is r{} and this is m{}".format(r,m))
        if r == 0 :
            #return self._ones(pow(2,m))
            return self._ones(pow(2,m))
        elif r == m:
            #return  self._identity(pow(2,m))
            return self._identity(pow(2,m))
        else:
            #print("detta är m,",m)
            x11 = self._g(r,m-1)
            x12 = x11
            x21 = self._zeros(pow(2,m-1))
            x22 = self._g(r-1,m-1)
            #print(x11, x12, x21, x22)
            return x11, x12, x21, x22


            #return np.array([
            #    [self._g(r,m-1),        self._g(r,m-1)],
            #    [np.zeros(pow(2,m-1)), self._g(r-1,m-1)]
            #    ])

    
    def _identity(self, n):
        m=[[0 for x in range(n)] for y in range(n)]
        for i in range(0,n):
            m[i][i] = 1
        print(m, "identity")
        return m

    def _ones(self, m):
        arr = []
        for _ in range(m): 
            arr.append(1)
        print(arr, "ones")
        return arr
    
    def _zeros(self, m):
        arr = []
        for _ in range(m): 
            arr.append(0)
        return arr


if __name__ == '__main__':
    reed_muller = RM()
    x11, x12, x21, x22= reed_muller.g(1,3)
    print(x11)
    print(x12)
    print(x21)
    print(x22)
    #print(np.matrix())


