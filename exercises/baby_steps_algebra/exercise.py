# From: http://deeplearning.net/software/theano/tutorial/adding.html#exercise

import theano

# declare variable
a = theano.tensor.vector()

# build symbolic expression
out = a + a ** 10

# compile function
f = theano.function([a], out)

# prints `array([0, 2, 1026])`
print("f([0, 1, 2]) = " + str(f([0, 1, 2])))

# Modify and execute this code to compute this expression: a ** 2 + b ** 2 + 2 * a * b.

