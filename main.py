from laboratory_tasks.first_lab import execute_first_lab
from laboratory_tasks.second_lab_part_two import execute_second_lab_part_two
from laboratory_tasks.third_lab import execute_third_lab
from laboratory_tasks.second_lab import execute_second_lab
from laboratory_tasks.fourth_lab import execute_fourth_lab
from sympy import Symbol, ln, log, sin, cos, pi
import math

x = Symbol('x')

execute_fourth_lab(0.4, 0.9, x**2+ln(x))
