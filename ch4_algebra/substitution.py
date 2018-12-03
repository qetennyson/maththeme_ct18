from sympy import symbols

x, y = symbols('x,y')

# first we declare a new expression
expr = x*x + x*y + x*y + y*y

# then we pass in the substitute values as a dictionary object.  Here 1 is the value of x, and 2 the value of y.
res = expr.subs({x:1, y:2,})
print(res)

# what if we knew x = 1-y?
res = expr.subs({x: 1-y})
print(res)