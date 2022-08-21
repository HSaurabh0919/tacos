# Some necessary imports.

import dcgpy
import pygmo as pg
import numpy as np
# Sympy is nice to have for basic symbolic manipulation.
from sympy import init_printing
from sympy.parsing.sympy_parser import *
init_printing()
# Fundamental for plotting.
from matplotlib import pyplot as plt


# Here we define our problem and solution strategy. In this case a simple Evolutionary Strategy acting on
# a CGP with no added constants.
X, Y = dcgpy.generate_chwirut2()
ss = dcgpy.kernel_set_double(["sum", "diff", "mul", "pdiv"])
udp = dcgpy.symbolic_regression(points = X, labels = Y, kernels=ss())
uda  = dcgpy.es4cgp(gen = 10000, max_mut = 2)

# We then construct our archipelago of *n*=64 islands containin 4 indivisuals each.
prob = pg.problem(udp)
algo = pg.algorithm(uda)
archi = pg.archipelago(algo = algo, prob = prob, pop_size = 4, n=64)

# Here is where the evolution starts
archi.evolve()


# We can inspect at any time the status of any island of the archipelago
#print(archi[23])


# Note how in the log above the island is *busy* indicating that the evolution is running. Note also that the
# island is, in this case, of type *thread island* indicating that its evolution is running on a separate thread
# We can also stop the interactive session and wait for the evolution to finish
#archi.wait_check()
archi.wait_check()
print('reached here')
# Let us inspect the results
fs = archi.get_champions_f()
xs = archi.get_champions_x()

# plt.plot(fs, '.')
# plt.xlabel('thread (island id)')
# _ = plt.ylabel('loss')
# plt.show()

b_idx = np.argmin(fs)
best_x = archi.get_champions_x()[b_idx]
print(parse_expr(udp.prettier(best_x)))

# And lets see what our model actually predicts on the inputs
Y_pred = udp.predict(X, best_x)

# Lets comapre to the data
_ = plt.plot(X, Y_pred, 'r.')
_ = plt.plot(X, Y, '.', alpha=0.2)
_ = plt.title('54 measurments')
_ = plt.xlabel('metal distance')
_ = plt.ylabel('ultrasonic response')
plt.show()
