from sympy import pprint
from sympy import symbols, expand, solve

# pprint is handy for making expressions look nice in the console or wherever they are output.
x = symbols('x')
expr = 1 + 2*x + 2*x**2

# pprint will change the order of the terms automatically to reflect the highest power first.
pprint(expr)