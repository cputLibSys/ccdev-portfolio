
import linear_algebra
import stats


m=linear_algebra.Matrix([[2, 6, 7, 0], [4, 9, 0, 1], [2, 1, 7, 2]])
v=linear_algebra.Vector(3, 0, 4)
v2=linear_algebra.Vector(2, 1,1)
for mode in stats.STAT_OPS.mode([2, 1, 5, 7, 5, 7, 0, 1]):
    print(mode.number, mode.counter)
#[pyo3(get, set)]