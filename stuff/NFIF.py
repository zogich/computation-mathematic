from stuff.BaseFunctionHandler import BaseFunctionHandler
from sympy import Symbol, log, factorial, expand, diff


class NFIF(BaseFunctionHandler):
    __table_of_finite_differences = []
    __polynom = []
    __newton_formula = []
    __remainder_estimate = ''
    __max_value_of_remainder_estimate = 0
    __min_value_of_remainder_estimate = 0

    def get_polynom(self):
        return self.__polynom

    def get_n(self):
        return self._n

    def __init__(self, n: int, begin_interval: float, end_interval: float):
        super().__init__(n, begin_interval, end_interval)
        self.__calculate_table_of_finite_differences()
        self.__calculate_newton_formula()
        self.__calculate_polynom()
        self.__compute_the_remainder_estimate()

    def __calculate_table_of_finite_differences(self):

        one_order = []
        for j in range(self._n - 1):
            one_order.append(self._values_of_function[j + 1] - self._values_of_function[j])
        self.__table_of_finite_differences.append(one_order)

        for i in range(self._n - 2):
            one_order = []
            for j in range(len(self.__table_of_finite_differences[-1]) - 1):
                one_order.append(
                    self.__table_of_finite_differences[-1][j + 1] - self.__table_of_finite_differences[-1][j])
            self.__table_of_finite_differences.append(one_order)

    def get_table_of_finite_differences(self):
        return self.__table_of_finite_differences

    def __calculate_newton_formula(self):
        q = Symbol('q')
        current_q_expression = q
        factorial_value = 1
        self.__newton_formula = self._nodes[0] ** 2 + log(self._nodes[0])
        for one_order in self.__table_of_finite_differences:
            self.__newton_formula = self.__newton_formula + (current_q_expression * one_order[0]) / factorial(
                factorial_value)
            current_q_expression = current_q_expression * (q - factorial_value)
            factorial_value = factorial_value + 1

        self.__newton_formula = expand(self.__newton_formula)

    def __calculate_polynom(self):

        q = Symbol('q')
        x = Symbol('x')

        step = (self._interval[1] - self._interval[0]) / self._n
        self.__polynom = expand(self.__newton_formula.subs(q, ((x - self._interval[0]) / step)))

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

    def __compute_the_remainder_estimate(self):
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
        return self.__remainder_estimate

    def get_remainder_estimate(self):
        return self.__remainder_estimate

    def interpolate_at_point(self, point):
        x = Symbol('x')
        return self.__polynom.subs(x, point)
