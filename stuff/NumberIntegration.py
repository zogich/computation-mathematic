from stuff.BaseFunctionHandler import BaseFunctionHandler
from sympy import Symbol, integrate
from sympy.core import add


class NumberIntegration(BaseFunctionHandler):

    __function = Symbol('x')
    __exact_integral_of_the_function = 0

    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        super().__init__(n, begin_interval, end_interval)
        self.__function = function
        self.__exact_integral_of_the_function = integrate(self.__function)

    def left_box_method(self):
        x = Symbol('x')
        sum_of_boxes = 0
        for index in range(0, len(self._nodes)-1):
            sum_of_boxes = sum_of_boxes + self._values_of_function[index] * self._step
        integral_of_sum = integrate(sum_of_boxes)
        return integral_of_sum.subs(x, self._interval[1]) - integral_of_sum.subs(x, self._interval[0])