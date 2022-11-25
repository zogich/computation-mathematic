from stuff.BaseFunctionHandler import BaseFunctionHandler
from sympy import Symbol, integrate
from sympy.core import add


class NumberIntegration(BaseFunctionHandler):

    __exact_integral_of_the_function = 0

    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        x = Symbol('x')
        super().__init__(n, begin_interval, end_interval, function)
        self.__exact_integral_of_the_function = integrate(self._function, x)

    def get_exact_integral(self):
        return self.__exact_integral_of_the_function

    def left_box_method(self):
        x = Symbol('x')
        sum_of_boxes = 0
        for index in range(0, len(self._nodes)-1):
            sum_of_boxes = sum_of_boxes + self._values_of_function[index] * self._step
        return sum_of_boxes

    #DRY F__kED
    def right_box_method(self):
        x = Symbol('x')
        sum_of_boxes = 0
        for index in range(1, len(self._nodes)):
            sum_of_boxes = sum_of_boxes + self._values_of_function[index] * self._step
        return sum_of_boxes

    def mid_box_method(self):
        x = Symbol('x')
        sum_of_boxes = 0
        for index in range(0, len(self._nodes)-1):
            middle_value_function = self._function.subs(x, ((self._nodes[index+1]+self._nodes[index]) / 2))
            sum_of_boxes = sum_of_boxes + middle_value_function * self._step

        return sum_of_boxes

    def trapezoidal_method(self):
        x = Symbol('x')
        sum_of_trapezoids = 0
        for index in range(0, len(self._nodes)-1):
            sum_of_trapezoids = sum_of_trapezoids + \
                                ((self._values_of_function[index]+self._values_of_function[index+1]) / 2)* self._step

        return sum_of_trapezoids
