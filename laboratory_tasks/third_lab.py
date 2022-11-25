from stuff.NumberIntegration import NumberIntegration
from sympy import Symbol, ln


def execute_third_lab():
    x = Symbol('x')
    a = NumberIntegration(2, 0.4, 0.9, x**2+ln(x))
