from sympy import symbols
from sympy import factor, expand

x,y = symbols('x,y')
expr = x**2 - y**2

# the factor function allows us to convert an expanded version of an expression to its factored version.
print(factor(expr))

# and vice versa with the expand function
factors = (factor(expr))
print(expand(factors))

# Here's a crazy one.
expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors2 = factor(expr)
print(factors2)
print(expand(factors2))