'''
Author: Sepehr Tayari
        elt15sta

Information theory EITFN45 
Hand in 1
'''

import numpy as np
class InfoTheory:
    def entropy(self,P):
        # Input P:
        # Matrix (2-dim array): Each row is a probability
        # distribution, calculate its entropy,
        # Row vector (1Xm matrix): The row is a probability
        # distribution, calculate its entropy,
        # Column vector (nX1 matrix): Derive the binary entropy
        # function for each entry,
        # Single value (1X1 matrix): Derive the binary entropy
        # function
        # Output:
        # array with entropies
        rows = P.shape[0]
        columns = P.shape[1]
        #print('Rows are {} and columns are {}'.format(rows, columns))
        #print("This is P {}".format(P))
        H = []
        if columns == 1:
        # Column vector (or single value), derive the binary entropy
            for p in P:
                if p == 0 or p == 1:
                    H.append(0)
                else:
                    p = p[0]
                    value = - (np.log2(p)*p) - (np.log2(1-p)*(1-p)) # Calculating the binary entropy
                    H.append(value)
        elif columns > 1:
        # Row vector, or matrix, calculate its entropy
            for row in P:
                value = 0
                for p in row:
                    if p == 0:
                        value += 0
                    else: 
                        value += -p*np.log2(p)
                H.append(value)
        return H

    def mutual_information(self,P):
        '''Calculates the mutual information
        Input: P, matrix
        Output: I 
        I = H(x)+H(y)-H(x,y)'''
        # Derive the mutual information I(X;Y)
        # Input P: P(X,Y)
        # Output: I(X;Y)

        P_x = np.array([np.sum(P, axis=1)]) # Sum of each row
        P_y = np.array([np.sum(P, axis=0)]) # Sum of each columna

        val_x=self.entropy(P_x)
        val_y=self.entropy(P_y)
        #val_joint = self._joint_entropy(P)
        val_joint_test = np.sum(self.entropy(P)) # Insåg att jag kan slippa använda _joint_entropy genom att göra såhär
        #print("Val x {}, val y {}, val join {}".format(val_x, val_y, val_joint))
        I = val_x[0] +val_y[0] - val_joint_test
        return [I]

    def _joint_entropy(self, P):
        # Joint entropy
        H = []
        for row in P:
            value = 0
            for p in row:
                if p == 0 or p == 1:
                    value += 0
                else: 
                    value += -p*np.log2(p)
            H.append(value)
        return np.sum(H)

def run_test_case(): 
    ''' Running all test cases from the task'''

    # init
    IT = InfoTheory()
    # 1st test
    P1 = np.transpose(np.array([np.arange(0.0,1.1,0.25)]))# row vector
    H1 = IT.entropy(P1)
    print('H1 =',H1)
    # 2nd test
    P2 = np.array([[0.3, 0.1, 0.3, 0.3],
    [0.4, 0.3, 0.2, 0.1],
    [0.8, 0.0, 0.2, 0.0]])
    H2 = IT.entropy(P2)
    print('H2 =',H2)
    # 3rd test
    P3 = np.array([[0, 3/4],[1/8, 1/8]])
    I3 = IT.mutual_information(P3)
    print('I3 =',I3)
    # 4th test
    P4 = np.array([[1/12, 1/6, 1/3],
    [1/4, 0, 1/6]])
    I4 = IT.mutual_information(P4)
    print('I4 =',I4)
    
if __name__=='__main__':
    run_test_case()
