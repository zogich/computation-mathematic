from stuff.LIP import LIP
from sympy import Symbol, log, factorial, expand, diff, ln


def execute_second_lab_part_two():
    x = Symbol('x')

    main_polynom = LIP(20, 0.4, 0.9, ln(x) + x**2 - 4)
    print(main_polynom)
    main_polynom.compute_the_remainder_estimate_way_two()
    main_polynom_differencial = diff(main_polynom.get_polynom(), x, 1)
    print(main_polynom_differencial)

    main_function_differencial = diff(log(x)+x**2-4, x, 1)

    main_function_differencial_in_point = main_function_differencial.subs(x, 0.72)
    main_polynom_differencial_in_point = main_polynom_differencial.subs(x, 0.72)

    print('Минимальное значение остаточного члена: ', main_polynom.get_min_remainder_estimate())
    print('Максимальное значение остаточного члена: ', main_polynom.get_max_remainder_estimate())

    print('Разность между дифференциалом полинома и функции в точке 0.72: ', main_function_differencial_in_point-main_polynom_differencial_in_point)