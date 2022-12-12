from sympy import log
from sympy.core import add
from sympy import Symbol, expand


class BaseFunctionHandler:
    _interval = []
    _n = 0
    _nodes = []
    _values_of_function = []
    _step = 0
    _function = 0

    def __init__(self, n: int, begin_interval: float, end_interval: float, function: add):
        if not isinstance(n, int) or not isinstance(begin_interval, float) or not isinstance(end_interval, float):
            raise TypeError

        x = Symbol('x')
        self._values_of_function = []
        self._interval = []
        self._n = 0
        self._nodes = []
        self._function = 0
        self._n = n

        self._function = function

        self._interval.append(begin_interval)
        self._interval.append(end_interval)

        self._step = (end_interval - begin_interval) / n
        self._nodes.append(self._interval[0])
        for i in range(1, n - 1):
            self._nodes.append(self._nodes[i - 1] + self._step)
        self._nodes.append(end_interval)

        for value in self._nodes:
            self._values_of_function.append(expand(self._function.subs(x, value)))
