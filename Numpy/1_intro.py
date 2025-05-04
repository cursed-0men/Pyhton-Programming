# NumPy
# NumPy is a Python library used for working with arrays.

'''
NumPy’s array class is called ndarray. It is 
also known by the alias array. Note that numpy.array 
is not the same as the Standard Python Library 
class array.array, which only handles one-dimensional 
arrays and offers less functionality.
'''

'''
The more important attributes of an ndarray 
object are:
'''
# 1. ndarray.ndim : the number of axes (dimensions) of the array.
# 2. ndarray.shape : For a matrix with n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore the number of axes, ndim.
# 3. ndarray.size : product of elements of shape i.e n*m.
# 4. ndarray.dtype : datatype of a array.
# 5. ndarray.itemsize : the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.
# 6. ndarray.data : the buffer containing the actual elements of the array. 

# array creation
import numpy as np
# np is alias
arr = np.array([4,5,6,7])
print(arr)
print(arr.dtype) # int64
print(arr.itemsize) # 8 bytes for each elements
print(arr.shape)
print(arr.size)
print(arr.ndim)# 1 dimensional array
print(type(arr))