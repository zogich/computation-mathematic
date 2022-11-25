from stuff.BaseFunctionHandler import BaseFunctionHandler
from sympy import Symbol, integrate
from sympy.core import add


class NumberIntegration(BaseFunctionHandler):

    _exact_integral_of_the_function = 0
    _value_of_method = 0

    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        x = Symbol('x')
        super().__init__(n, begin_interval, end_interval, function)
        self.__exact_integral_of_the_function = integrate(self._function, x)

    def get_exact_integral(self):
        return self.__exact_integral_of_the_function


class LeftBoxMethod(NumberIntegration):

    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        super().__init__(n, begin_interval, end_interval, function)
        self._execute_method()

    def _execute_method(self):
        sum_of_boxes = 0
        for index in range(0, len(self._nodes) - 1):
            sum_of_boxes = sum_of_boxes + self._values_of_function[index] * self._step
        self._value_of_method = sum_of_boxes


class RightBoxMethod(NumberIntegration):

    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        super().__init__(n, begin_interval, end_interval, function)
        self._execute_method()

    def _execute_method(self):
        sum_of_boxes = 0
        for index in range(1, len(self._nodes)):
            sum_of_boxes = sum_of_boxes + self._values_of_function[index] * self._step
        self._value_of_method = sum_of_boxes


class MidBoxMethod(NumberIntegration):

    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        super().__init__(n, begin_interval, end_interval, function)
        self._execute_method()

    def _execute_method(self):
        x = Symbol('x')
        sum_of_boxes = 0
        for index in range(0, len(self._nodes) - 1):
            middle_value_function = self._function.subs(x, ((self._nodes[index + 1] + self._nodes[index]) / 2))
            sum_of_boxes = sum_of_boxes + middle_value_function * self._step

        self._value_of_method = sum_of_boxes


class TrapezoidalMethod(NumberIntegration):
    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        super().__init__(n, begin_interval, end_interval, function)
        self._execute_method()

    def _execute_method(self):
        sum_of_trapezoids = 0
        for index in range(0, len(self._nodes) - 1):
            sum_of_trapezoids = sum_of_trapezoids + \
                                ((self._values_of_function[index] + self._values_of_function[
                                    index + 1]) / 2) * self._step

        self._value_of_method = sum_of_trapezoids


class SimpsonFormula(NumberIntegration):
    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        super().__init__(n, begin_interval, end_interval, function)
        self._execute_method()

    def _execute_method(self):
        x = Symbol('x')
        parabols_sums = 0
        for index in range(0, len(self._nodes) - 1):
            middle_value_function = self._function.subs(x, ((self._nodes[index + 1] + self._nodes[index]) / 2))
            parabola = ((self._interval[1] - self._interval[0]) / 6) * (
                    self._values_of_function[index] + 4 * middle_value_function + self._values_of_function[index + 1]
            )
            parabols_sums = parabols_sums + parabola

        self._value_of_method = parabols_sums

