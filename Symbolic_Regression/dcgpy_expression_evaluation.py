import dcgpy
import pygmo as pg
# Sympy is nice to have for basic symbolic manipulation.
from sympy import init_printing
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
# Fundamental for plotting.
from matplotlib import pyplot as plt

###http://darioizzo.github.io/dcgp/notebooks/symbolic_regression_2.html

#X, Y = dcgpy.generate_ratpol2d()
x = np.linspace(1,3,50)
X = np.array([(item,)for item in x])
#X = np.array([[item,item] for item in x])
Y = np.array([(item**5 - np.pi*item**3,) + item for item in x])


ss = dcgpy.kernel_set_double(["sum", "mul","diff"])

udp = dcgpy.symbolic_regression(
    points = X, labels = Y, kernels=ss(),
    rows = 1,
    cols = 100,
    n_eph = 3,
    levels_back = 80)
prob = pg.problem(udp)

uda  = dcgpy.es4cgp(gen = 100000, max_mut = 4)
algo = pg.algorithm(uda)
algo.set_verbosity(0)

pop = pg.population(prob, 4)
pop = algo.evolve(pop)
x = pop.champion_x
a = parse_expr(udp.prettier(x))[0]
print("Before",a)