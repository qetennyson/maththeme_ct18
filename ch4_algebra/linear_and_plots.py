from sympy import solve, symbols, plot, Symbol

# Let's solve a linear equation
x = Symbol('x')
y = Symbol('y')
linear1 = 2*x+3*y-6
linear2 = 3*x+2*y-12

# Holy moly.
soln = solve((linear1, linear2), dict=True)
for k,v in soln[0].items():
    print(f'{k}:',f'{v}')

# GRAPHS
plot(2*x+3)
