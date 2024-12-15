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

cdef extern from "Stats.h" namespace "stats":
    cdef struct MODE:
        double number
        int count

    cdef cppclass Regress:
        Regress() except +
        Regress(vector[double] v_arr, int size) except +
        vector[double] main_arr
        int size
        void sample()
        double mean()
        MODE mode()
        double min()
        double max()
        double SD()
        double Var()
