from stuff.LIP import LIP
from sympy import Symbol, log, diff
from sympy.core import add


def execute_second_lab_part_two(begin_interval: float, end_interval: float, function: add):
    x = Symbol('x')

    main_polynom = LIP(20, begin_interval, end_interval, function)
    main_polynom.compute_the_remainder_estimate_way_two()
    main_polynom_differencial = diff(main_polynom.get_polynom(), x, 1)

    main_function_differencial = diff(function, x, 1)

    main_function_differencial_in_point = main_function_differencial.subs(x, 0.56)
    main_polynom_differencial_in_point = main_polynom_differencial.subs(x, 0.56)

    print('Минимальное значение остаточного члена: ', main_polynom.get_min_remainder_estimate())
    print('Максимальное значение остаточного члена: ', main_polynom.get_max_remainder_estimate())

    print('Разность между дифференциалом полинома и функции в точке 0.49: ', main_function_differencial_in_point-main_polynom_differencial_in_point)