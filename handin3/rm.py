import numpy as np
import math

class RM:
    
    def __init__(self, r, m):
        self.r = r
        self.m = m
        self.G = np.zeros(pow(2,m))
        
    def rm(self):
        
        return self.G

    def _rm(self):
        
        return


if __name__ == '__main__':
    reed_muller = RM(1,3)
    print(reed_muller.rm())

