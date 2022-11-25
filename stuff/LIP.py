import math

import numpy as np
from sympy import Symbol, Float, expand, log, diff, factorial

from stuff.BaseFunctionHandler import BaseFunctionHandler


class LIP(BaseFunctionHandler):
    __polynom = 0
    __min_value_of_remainder_estimate = 0
    __max_value_of_remainder_estimate = 0
    __remainder_estimate = 0

    def __str__(self):
        return str(self.__polynom)

    def __init__(self, n: int, begin_interval: float, end_interval: float):
        super().__init__(n, begin_interval, end_interval)
        self.__calculate_polynom()
        print(self._n)

    def get_polynom(self):
        return self.__polynom

    def get_nodes(self):
        return self._nodes

    def __calculate_polynom(self):
        for i in range(self._n):
            ptr_term = Float(self._nodes[i] ** 2) + Float(math.log(self._nodes[i]))
            for j in range(self._n):
                x = Symbol('x')
                if j != i:
                    ptr_term *= (x - self._nodes[j]) / (self._nodes[i] - self._nodes[j])
                    ptr_term = expand(ptr_term)
            self.__polynom += ptr_term
            self.__polynom = expand(self.__polynom)
        self.__polynom = expand(self.__polynom)

    def calculate_absolute_error(self):
        x = Symbol('x')
        function_for_calculating = self.__polynom - x ** 2 - log(x)
        absolute_error = 0
        for value in self._nodes:
            ptr_value = abs(function_for_calculating.subs(x, value))
            if ptr_value > absolute_error:
                absolute_error = ptr_value
        return absolute_error

    def calculate_relative_error(self):
        x = Symbol('x')
        absolute_error = self.calculate_absolute_error()
        function = x ** 2 + log(x)
        norm_of_function = 0
        for value in self._nodes:
            ptr_value = abs(function.subs(x, value))
            if ptr_value > norm_of_function:
                norm_of_function = ptr_value
        relative_error = absolute_error / norm_of_function
        return relative_error

    def compute_the_remainder_estimate(self):
        x = Symbol('x')

        function_for_norm = (x ** 2 + log(x))
        differencial_of_function = diff(function_for_norm, x, self._n + 1)
        norm_of_function = 0

        for value in self._nodes:
            ptr_value = abs(differencial_of_function.subs(x, value))
            if ptr_value > norm_of_function:
                norm_of_function = ptr_value
        remainder_estimate = norm_of_function / np.math.factorial(self._n + 1)
        remainder_estimate = remainder_estimate * ((self._interval[1] - self._interval[0]) ** (self._n + 1))
        return remainder_estimate

    def compute_the_remainder_estimate_way_two(self):
        x = Symbol('x')
        function_for_norm = (x ** 2 + log(x))
        differencial_of_function = diff(function_for_norm, x, self._n + 1)
        self.__remainder_estimate = differencial_of_function / factorial(self._n + 1)
        for value in self._values_of_function:
            self.__remainder_estimate = self.__remainder_estimate * (x - value)
        self.__remainder_estimate = expand(self.__remainder_estimate)

        self.__min_value_of_remainder_estimate = self.__remainder_estimate.subs(x, self._values_of_function[0])
        self.__max_value_of_remainder_estimate = self.__remainder_estimate.subs(x, self._values_of_function[0])

        for value in self._values_of_function:
            sub_value = self.__remainder_estimate.subs(x, value)
            if sub_value > self.__max_value_of_remainder_estimate:
                self.__max_value_of_remainder_estimate = sub_value
            if sub_value < self.__min_value_of_remainder_estimate:
                self.__min_value_of_remainder_estimate = sub_value

    def get_max_remainder_estimate(self):
        return self.__max_value_of_remainder_estimate

    def get_min_remainder_estimate(self):
        return self.__min_value_of_remainder_estimate
