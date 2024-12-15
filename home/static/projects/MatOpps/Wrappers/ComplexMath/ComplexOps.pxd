from libc.string import *

cdef extern from "<vector>" namespace "std":
    cdef cppclass vector[T]:
        cppclass iterator:
            T operator*()
            iterator operator++()
            bint operator==(iterator)
            bint operator!=(iterator)
        vector()
        void push_back(T&)
        T& operator[](int)
        T& at(int)
        iterator begin()
        iterator end()

cdef extern from "Complex.h" namespace "ComplexOps":
    cdef struct ComplexN:
        double real_part;
        double imag_part;
        double modulus();
        double argument();
    
    cdef cppclass ComplexMath:
        int setComplexN(vector[double] cn)
        ComplexN SUM(vector[int] range, int r)
        ComplexN PRODUCT(int i, int j)
        ComplexN DIV(int i, int j)
        ComplexN RecursiveProd(vector[int] range)
        ComplexN POW(int i, int n)