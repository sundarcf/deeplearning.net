# From: http://deeplearning.net/software/theano/tutorial/adding.html#exercise

# Compute expression: a ** 2 + b ** 2 + 2 * a * b.


import theano

# declare variable
a = theano.tensor.dscalar(name = 'a')
b = theano.tensor.dscalar(name = 'b')

# build symbolic expression
out = a ** 2 + b ** 2 + 2 * a * b

# compile function
f = theano.function([a, b], out)

# Apply f
print("f([2, 5]) = " + str(f(2, 5)))


