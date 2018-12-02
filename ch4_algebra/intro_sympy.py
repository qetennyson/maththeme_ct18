from sympy import symbols

# Create an algebraic symbol 'x' as a Symbol object.  Note that it is a string.
x = symbols('x')

# Notice that x is the variable given to represent a mathematical symbol of x.
# This can be confusing at first.  You could store symbol x in variable 'a', but that seems like a bad idea.
print(x + x + 1)

# We can create as many symbols as we like at one time.
x,y,z = symbols('x,y,z') # This is a bit weird how this is parsed.  Just remember symbols() expects only one string.

# SymPy simplifies simpler expressions.
print(x*y + x*y)
print(x*(x+x))

# But does not simplify more complex expressions.
p = (x+2)*(x+3)
print(p)

# the name attribute
print(x.name)