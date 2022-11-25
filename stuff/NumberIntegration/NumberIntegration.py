from stuff.BaseFunctionHandler import BaseFunctionHandler
from sympy import Symbol, integrate
from sympy.core import add


class NumberIntegration(BaseFunctionHandler):

    _exact_integral_of_the_function = 0
    _calculated_integral_of_the_function = 0
    _value_of_method = 0
    _absolute_error_value = 0
    _relative_error_value = 0
    _remainder_term_value = 0

    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        x = Symbol('x')
        super().__init__(n, begin_interval, end_interval, function)
        self._exact_integral_of_the_function = integrate(self._function, x)
        self._calculated_integral_of_the_function = self._exact_integral_of_the_function.subs(x, self._interval[
            1]) - self._exact_integral_of_the_function.subs(x, self._interval[0])
        self._execute_method()
        self._calculate_absolute_error()
        self._calculate_relative_error()
        self._calculate_remainder_term()

    def _execute_method(self):
        pass

    def get_calculated_exact_integral(self):
        return self._calculated_integral_of_the_function

    def change_values(self, n: int, begin_interval: float, end_interval: float, function: add):
        x = Symbol('x')
        super().__init__(n, begin_interval, end_interval, function)
        self._exact_integral_of_the_function = integrate(self._function, x)
        self._calculated_integral_of_the_function = self._exact_integral_of_the_function.subs(x, self._interval[
            1]) - self._exact_integral_of_the_function.subs(x, self._interval[0])
        self._execute_method()
        self._calculate_absolute_error()
        self._calculate_relative_error()
        self._calculate_remainder_term()

    def get_exact_integral(self):
        return self._exact_integral_of_the_function

    def get_value_of_method(self):
        return self._value_of_method

    def get_absolute_error(self):
        return self._absolute_error_value

    def get_relative_error(self):
        return self._relative_error_value

    def get_remainder_term(self):
        return self._remainder_term_value

    def _calculate_absolute_error(self):
        x = Symbol('x')
        self._absolute_error_value = abs(self._calculated_integral_of_the_function - self._value_of_method)

    def _calculate_relative_error(self):
        x = Symbol('x')
        self._relative_error_value = (self._absolute_error_value / (abs(self._calculated_integral_of_the_function)))

    def _calculate_remainder_term(self):
        x = Symbol('x')

        self._remainder_term_value = self._calculated_integral_of_the_function - self._value_of_method


class LeftBoxMethod(NumberIntegration):

    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        super().__init__(n, begin_interval, end_interval, function)

    def _execute_method(self):
        sum_of_boxes = 0
        for index in range(0, len(self._nodes) - 1):
            sum_of_boxes = sum_of_boxes + self._values_of_function[index] * self._step
        self._value_of_method = sum_of_boxes


class RightBoxMethod(NumberIntegration):

    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        super().__init__(n, begin_interval, end_interval, function)

    def _execute_method(self):
        sum_of_boxes = 0
        for index in range(1, len(self._nodes)):
            sum_of_boxes = sum_of_boxes + self._values_of_function[index] * self._step
        self._value_of_method = sum_of_boxes


class MidBoxMethod(NumberIntegration):

    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        super().__init__(n, begin_interval, end_interval, function)

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




