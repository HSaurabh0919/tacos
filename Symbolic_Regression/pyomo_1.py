# Some necessary imports.

import pygmo as pg
import numpy as np
import time


class sphere_function:
    def __init__(self, dim):
        self.dim = dim

    def fitness(self, x):
        return [sum(x*x)]

    def get_bounds(self):
        return ([-1] * self.dim, [1] * self.dim)

    def get_name(self):
        return "Sphere Function"

    def get_extra_info(self):
        return "\tDimensions: " + str(self.dim)

# prob = pg.problem(sphere_function(3))
# algo = pg.algorithm(pg.bee_colony(gen = 20, limit = 20))
# pop = pg.population(prob,10)
# pop = algo.evolve(pop)
# print(pop.champion_f) 

class py_rosenbrock:
    def __init__(self,dim):
        self.dim = dim
    def fitness(self,x):
        retval = np.zeros((1,))
        for i in range(len(x) - 1):
            retval[0] += 100.*(x[i + 1]-x[i]**2)**2+(1.-x[i])**2
        return retval
    def get_bounds(self):
        return (np.full((self.dim,),-5.),np.full((self.dim,),10.))

prob_python = pg.problem(py_rosenbrock(2000))
prob_cpp = pg.problem(pg.rosenbrock(2000))
dummy_x = np.full((2000,), 1.)
# import time
# start_time = time.time(); [prob_python.fitness(dummy_x) for i in range(1000)];

# print(time.time() - start_time) 

# start_time = time.time(); [prob_cpp.fitness(dummy_x) for i in range(1000)]; 
# print(time.time() - start_time) 

from numba import jit
class jit_rosenbrock:
    def __init__(self,dim):
        self.dim = dim
    @jit
    def fitness(self,x):
        retval = np.zeros((1,))
        for i in range(len(x) - 1):
            retval[0] += 100.*(x[i + 1]-x[i]**2)**2+(1.-x[i])**2
        return retval
    def get_bounds(self):
        return (np.full((self.dim,),-5.),np.full((self.dim,),10.))
prob_jit = pg.problem(jit_rosenbrock(2000))
start_time = time.time(); [prob_jit.fitness(dummy_x) for i in range(1000)]; print(time.time() - start_time) 