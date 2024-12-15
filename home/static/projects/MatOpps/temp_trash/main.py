import matplotlib.pyplot as plt
import numpy as np
from Wrappers.linear_algebra.mat_maths import *

class matApp(BasicOps):

    A=None
    B=None

    def __init__(self):

        self.A=[[1,2 ,3], [4, 5, 7],[1, 1, 1],[2, 0, 5], [4,3]]#self.getInput()
        self.B=[[2, 43], [4, 5], [1, 0], [3, 2]]#self.getInput()

        print(self.A[:-1],' * ',self.B,' = ',self.matProd())


    def getInput(self):

        print('\n')

        dim=input('Enter matrix dimension: ')
        dim=dim.split(' ')
        dim=[int(i) for i in dim]

        matrix=[]
        
        for i in range(0,dim[0]):        
            
            row=input(f'Enter row {i+1}: ')
            row=row.strip()
            row=row.split(' ')
        

            row=[float(x) for x in row]

            if len(row)!=dim[1]:
                print('Matrix row dimensions out of bounds.\n')
                break

            matrix.append(row)

        matrix.append(dim)

        return matrix


app=matApp()





