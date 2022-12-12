from stuff.SplineInterpolation import SplineInterpolation
from sympy.core import add
import matplotlib.pyplot as plt


def execute_fourth_lab(begin_interval: float, end_interval: float, function: add):

    rawdata = []
    collabel = ('n', '△fn', 'δfn')
    absolute_error_values = []
    n_values = []

    s = SplineInterpolation(5, begin_interval, end_interval, function)
    rawdata.append([5, s.get_absolute_error(), s.get_relative_error()])
    absolute_error_values.append(s.get_absolute_error())
    n_values.append(5)

    for n in range(10, 101, 10):
        s = SplineInterpolation(n, begin_interval, end_interval, function)
        rawdata.append([n, s.get_absolute_error(), s.get_relative_error()])
        absolute_error_values.append(s.get_absolute_error())
        n_values.append(n)

    fig, ax = plt.subplots(2, 1, figsize=(10, 10))

    ax[0].plot(n_values, absolute_error_values, color='red')

    ax[1].axis('tight')
    ax[1].axis('off')
    ax[1].table(cellText=rawdata, colLabels=collabel, loc='center')
    plt.savefig('fourth_lab_output')
    plt.show()
