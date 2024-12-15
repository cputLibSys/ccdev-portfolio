import linear_algebra

class BasicOps:
    
    def popMatrix(self, dim, empty_set="None"):        
        tnM=[]
        if empty_set=='empty_set':
            for i in range(0, dim[0]):
                tnM.append([])

        else: 
            for i in range(0, dim[0]):
                tnM.append([])
                for j in range(0, dim[1]):
                    tnM[i].append(0)
            
        return tnM

    def matAddSub(self, operand,A, B):

        if A[-1]==B[-1]:
            
            tA=linear_algebra.Matrix(A[:-1])
            tB=linear_algebra.Matrix(B[:-1])
            dim=A[-1]

            return linear_algebra.mat_ops.add(tA, tB).elements

        else:
            return "Error"


    def transpose(self, mat):
        trans_M=self.popMatrix([ len(mat[0]), len(mat)], 'empty_set')
        for el in mat:
            for i in range(0, len(mat[0])):
                trans_M[i].append(el[i])  

        return linear_algebra.mat_ops.transpose(mat).elements

    def matProd(self, A, B):

        nM=[] #matrix product

        if A[-1][1]==B[-1][0]: #dimensions check
            tA, tB=A[:-1],B[:-1] #temporary matrices
            dim=[A[-1][0], B[-1][1]] #dimensions of new matrix

            nM=linear_algebra.mat_ops.multiply(tA, tB).elements
        else:
            print('\nCannot multiply matrices. Make sure the col-number of matrix A and row-number of matrix B are the same')

        return nM
