from sympy import sympify, symbols, solve

# what if we're interested in user input?
expr = input('Enter a mathematical expression: ')
expr = sympify(expr)
print("Expression input solution:")

print(solve(expr))

# is that a WILD quadratic equation
x = symbols('x')
quad_expr = x**2+5*x+4

print("Quadratic solution: ")
print(solve(quad_expr))
