from stuff.NFIF import NFIF
from sympy.core import add
import matplotlib.pyplot as plt


def execute_second_lab(begin_interval: float, end_interval: float, function: add):
    n = 10
    rawdata = []
    colllabel = ['△'+str(i)+'y' for i in range(1, n)]
    for i in range(1, n):
        rawdata.append([])

    main_polynom = NFIF(n, begin_interval, end_interval, function)
    for order in main_polynom.get_table_of_finite_differences():
        i = 0
        while i < len(order):
            rawdata[i].append(order[i])
            i = i + 1
        while i < n-1:
            rawdata[i].append(' ')
            i = i + 1
    fig, ax = plt.subplots(1, 1, figsize=(20, 12))

    ax.axis('off')

    the_table = ax.table(cellText=rawdata, colLabels=colllabel, loc='center')

    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.auto_set_column_width(col=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    plt.savefig('second_lab_output.png')
    plt.show()


