from stuff.NumberIntegration.NumberIntegration import LeftBoxMethod, RightBoxMethod, MidBoxMethod, TrapezoidalMethod, \
    SimpsonFormula
from sympy import Symbol, ln


def execute_third_lab():
    x = Symbol('x')
    t = TrapezoidalMethod(10, 0.4, 0.9, x ** 2 + ln(x))

    

