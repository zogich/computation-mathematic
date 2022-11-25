from stuff.NumberIntegration import NumberIntegration
from sympy import Symbol, ln


def execute_third_lab():
    x = Symbol('x')
    a = NumberIntegration(1000, 0.4, 0.9, x**2+ln(x))
    print('EXACT INTEGRAL:', a.get_exact_integral().subs(x, 0.9)-a.get_exact_integral().subs(x, 0.4))
    print('LEFT BOX METHOD', a.left_box_method())
    print('RIGHT BOX METHOD', a.right_box_method())
    print('MIDDLE BOX METHOD', a.mid_box_method())
    print('TRAPEZOIDAL METHOD', a.trapezoidal_method())