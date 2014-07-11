# From http://deeplearning.net/software/theano/tutorial/adding.html#adding-two-scalars

import theano.tensor as T
from theano import function

# Step 1:
# Define two symbols (Variables) representing the quantities that you want to add.
# 'x' and 'y' are instances of TensorVariable of theano Type dscalar in their type field.
# T.dscalar is the type we assign to "0-dimensional arrays (scalar) of doubles (d).
x = T.dscalar('x')
y = T.dscalar('y')

# Step 2:
# Combine 'x' and 'y' into their sum 'z'.
# 'z' is yet another variable which represents the addition of 'x' and 'y'.
z = x + y

# Step 3:
# Create a theano function taking 'x' and 'y' as inputs and giving 'z' as output.
# A theano function takes a list of input symbol variables as the first argument and
# an output symbol variable or list of output symbol variables as the second argument.
f = function([x, y], z)


# Apply theano function 'f' over various inputs and display output
print("f(2, 3) = " + str(f(2, 3)))
print("f(16.3, 12.1) = " + str(f(16.3, 12.1)))