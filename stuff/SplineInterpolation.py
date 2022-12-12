from stuff.BaseFunctionHandler import BaseFunctionHandler
from sympy.core import add
from scipy.interpolate import UnivariateSpline
from sympy import Symbol


class SplineInterpolation(BaseFunctionHandler):

    __full_spline = 0
    __absolute_error = 0
    __relative_error = 0

    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        super().__init__(n, begin_interval, end_interval, function)
        x = Symbol('x')
        spl = UnivariateSpline(self._nodes, self._values_of_function)
        self.__full_spline = spl.get_coeffs()[0] + x*spl.get_coeffs()[1] + (x**2)*spl.get_coeffs()[2] + (x**3)*spl.get_coeffs()[3]
        self.__calculate_absolute_error()
        self.__calculate_relative_error()

    def __calculate_absolute_error(self):
        x = Symbol('x')
        self.__absolute_error = 0
        for node in self._nodes:
            if abs(self.__full_spline.subs(x, node) - self._function.subs(x, node)) > self.__absolute_error:
                self.__absolute_error = abs(self.__full_spline.subs(x, node) - self._function.subs(x, node))

    def __calculate_relative_error(self):
        norm_of_function = 0
        for value in self._values_of_function:
            if abs(value) > norm_of_function:
                norm_of_function = abs(value)

        self.__relative_error = self.__absolute_error / norm_of_function

    def get_absolute_error(self):
        return self.__absolute_error

    def get_relative_error(self):
        return self.__relative_error

