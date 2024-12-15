# distutils: language = c++
# distutils: sources = Stats.cpp

from Regress cimport Regress
from cpython cimport array

#ctypedef MODE mode

cdef class PyRegress:
    cdef Regress *_Regress 
    def __cinit__(self, nums):
        cdef vector[double] _nums = nums
        self._Regress = new Regress(_nums, len(nums))

    def sample(self):
        cdef vector[double] v = self._Regress.main_arr
        return v

    def mean(self):
        return self._Regress.mean()

    def mode(self):
        cdef MODE m
        m=self._Regress.mode()
        return [m.number, m.count]

    def min(self):
        return self._Regress.min()

    def max(self):
        return self._Regress.max()

    def SD(self):
        return self._Regress.SD()

    def Var(self):
        return self._Regress.Var()

