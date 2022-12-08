from stuff.LIP import LIP
import matplotlib.pyplot as plt
import numpy as np
import math
from sympy import ln, Symbol


def execute_first_lab():
    x = Symbol('x')
    clust_data = np.random.random((10, 3))

    n_values = []
    absolute_error_values = []
    relative_error_values = []
    remainder_estimate_values = []

    main_polynom = LIP(3, 0.4, 0.9, ln(x) + x**2)

    n_values.append(3)
    absolute_error_values.append(main_polynom.calculate_absolute_error())
    relative_error_values.append(main_polynom.calculate_relative_error())
    remainder_estimate_values.append(main_polynom.compute_the_remainder_estimate())

    main_polynom = LIP(5, 0.4, 0.9, ln(x) + x**2)
    n_values.append(5)
    absolute_error_values.append(main_polynom.calculate_absolute_error())
    relative_error_values.append(main_polynom.calculate_relative_error())
    remainder_estimate_values.append(main_polynom.compute_the_remainder_estimate())

    for value in range(10, 101, 10):
        main_polynom = LIP(value, 0.4, 0.9, ln(x) + x**2)
        n_values.append(value)
        absolute_error_values.append(main_polynom.calculate_absolute_error())
        relative_error_values.append(main_polynom.calculate_relative_error())
        remainder_estimate_values.append(main_polynom.compute_the_remainder_estimate())

    fig, ax = plt.subplots(3, 1, figsize=(10, 10))

    ax[2].axis('tight')
    ax[2].axis('off')

    collabel = ("n", "∆fn", "δfn", 'rn')
    colldata = []
    for num in range(len(n_values)):
        colldata.append([n_values[num],
                         absolute_error_values[num],
                         relative_error_values[num],
                         remainder_estimate_values[num]])

    ax[2].table(cellText=colldata, colLabels=collabel, loc='center')

    absolute_error_line = ax[0].plot(n_values, absolute_error_values, color='red')
    remainder_estimate_line = ax[0].plot(n_values, remainder_estimate_values, color='blue')

    log_absolute_error_line = ax[1].plot(n_values, list(map(lambda x: math.log(x, 10), absolute_error_values)), color='red')
    log_remainder_estimate_line = ax[1].plot(n_values, list(map(lambda x: math.log(x, 10), remainder_estimate_values)), color='blue')

    plt.savefig('table_and_plots.png')
    plt.show()