# distutils: language = c++
# distutils: sources = Complex.cpp

from ComplexOps cimport *
from libc.stdlib cimport malloc, free
import ctypes
import numpy as np
from cpython cimport array

ctypedef ComplexN ComplexNumber

cdef class ComplexOpsWrapper:
    cdef ComplexMath *CM;
    def __cinit__(self):
        self.CM=new ComplexMath()

    def setComplexN(self, cn):
        #cdef double *_cn=array.array('d',cn).data.as_doubles
        cdef vector[double] v
        v.push_back(cn[0])
        v.push_back(cn[1])
        #print(cn[0])
        return self.CM.setComplexN(v)
        
    

    def SUM(self, range, r):
        cdef ComplexNumber c_sn

        cn_s=self.CM.SUM(range, r)
        res=[cn_s.real_part, cn_s.imag_part, [cn_s.argument(), cn_s.modulus()]]
       
        return res

    def PRODUCT(self, int i, int j):
        cdef ComplexNumber cn_p

        cn_p=self.CM.PRODUCT(i, j)
        res=[cn_p.real_part, cn_p.imag_part, [cn_p.argument(), cn_p.modulus()]]

        return res

    def DIV(self, int i, int j):
        cdef ComplexNumber cn_q

        cn_q=self.CM.DIV(i, j)
        res=[cn_q.real_part, cn_q.imag_part]

        return res
        
    def RecursiveProd(self, range):
        cdef ComplexNumber rProd

        cProd=self.CM.RecursiveProd(range)
        res=[cProd.real_part, cProd.imag_part, [cProd.argument(), cProd.modulus()]]

        return res

    def POW(self, int i, int n):
        cdef ComplexNumber cn
        cn=self.CM.POW(i, n)
        res=[cn.real_part, cn.imag_part, [cn.argument(), cn.modulus()]]

        return res