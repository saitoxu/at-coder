import numpy as np

ary = np.array([[1, 2, 3], [4, 5, 6]], np.int64)
print(ary.shape) # => (2, 3)

# searchsorted
# ref. https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html
print(np.searchsorted([1, 2, 3, 4, 5], 3)) # => 2
print(np.searchsorted([1, 2, 3, 4, 5], 3, side='right')) # => 2
print(np.searchsorted([1, 2, 3, 4, 5], [-10, 10, 2, 3])) # => [0, 5, 1, 2]
