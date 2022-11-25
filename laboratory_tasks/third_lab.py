from stuff.NumberIntegration.NumberIntegration import LeftBoxMethod, RightBoxMethod, MidBoxMethod, TrapezoidalMethod, \
    SimpsonFormula
from sympy import Symbol
import matplotlib.pyplot as plt


def execute_third_lab(function):

    x = Symbol('x')
    t = TrapezoidalMethod(2, 0.4, 0.9, function)

    colldata1 = []
    colldata2 = []
    collabel1 = ("n", "I*", "I", "∆I", "δI", 'Rn')
    collabel2 = ("Метод", "I*", "I", "∆I", "δI", 'Rn')

    colldata1.append([2, t.get_calculated_exact_integral(), t.get_value_of_method(), t.get_absolute_error(), t.get_relative_error(),
                      t.get_remainder_term()])

    count = 4
    while count < 2**16:
        t.change_values(count, 0.4, 0.9, function)
        colldata1.append([count, t.get_calculated_exact_integral(), t.get_value_of_method(), t.get_absolute_error(),
                          t.get_relative_error(), t.get_remainder_term()
                          ])
        count = count * 2

    l = LeftBoxMethod(10000, 0.4, 0.9, function)
    colldata2.append([
        'Л. прямоугольников', l.get_calculated_exact_integral(), l.get_value_of_method(), l.get_absolute_error(),
        l.get_relative_error(), l.get_remainder_term()
    ])

    r = RightBoxMethod(10000, 0.4, 0.9, function)
    colldata2.append([
        'П. прямоугольников', r.get_calculated_exact_integral(), r.get_value_of_method(), r.get_absolute_error(),
        r.get_relative_error(), r.get_remainder_term()
    ])

    m = MidBoxMethod(10000, 0.4, 0.9, function)
    colldata2.append([
        'Ц. прямоугольников', m.get_calculated_exact_integral(), m.get_value_of_method(), m.get_absolute_error(),
        m.get_relative_error(), m.get_remainder_term()
    ])

    t.change_values(10000, 0.4, 0.9, function)
    colldata2.append([
        'Трапеций', t.get_calculated_exact_integral(), t.get_value_of_method(), t.get_absolute_error(),
        t.get_relative_error(), t.get_remainder_term()
    ])

    s = SimpsonFormula(10000, 0.4, 0.9, function)
    colldata2.append([
        'Симпсона', s.get_calculated_exact_integral(), s.get_value_of_method(), s.get_absolute_error(),
        s.get_relative_error(), s.get_remainder_term()
    ])

    fig, ax = plt.subplots(2, 1, figsize=(12, 12))

    [a.axis('off') for a in ax]

    the_table1 = ax[0].table(cellText=colldata1, colLabels=collabel1, loc='center')
    the_table2 = ax[1].table(cellText=colldata2, colLabels=collabel2, loc='center')

    [table.auto_set_font_size(False) for table in [the_table1, the_table2]]
    [table.set_fontsize(10) for table in [the_table1, the_table2]]
    [table.auto_set_column_width(col=[0, 1, 2, 3, 4, 5]) for table in [the_table1, the_table2]]

    plt.savefig('third_lab_output.png')
    plt.show()

