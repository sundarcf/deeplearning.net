# From: http://deeplearning.net/software/theano/tutorial/adding.html#adding-two-matrices

# See adding_two_scalars.py

import numpy
import theano.tensor as T
from theano import function

# Instantiate x and y as TensorVariable of Type T.dmatrix (matrix of doubles)
x = T.dmatrix('x')
y = T.dmatrix('y')
z = x + y
f = function([x, y], z)


# Apply function over various inputs and display outputs

print("f([[1, 2], [3, 4]], [[10, 20], [30, 40]]) = ")
print(f([[1, 2], [3, 4]], [[10, 20], [30, 40]]))

print("f(numpy.array([[1, 2], [3, 4]]), numpy.array([[10, 20], [30, 40]])) = ")
print(f(numpy.array([[1, 2], [3, 4]]), numpy.array([[10, 20], [30, 40]])))