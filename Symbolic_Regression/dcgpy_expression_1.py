from dcgpy import *
from dcgpy import expression_double
from dcgpy import kernel_set_double
from dcgpy import expression_gdual_double
from dcgpy import kernel_set_gdual_double

#inputs, outputs, rows, cols, levels_back, arity = 2, kernels, n_eph = 0, seed = randint)
#n_eph: Number of ephemeral constants. Their values and their symbols can be set via dedicated methods.
dcgp = expression_double(1,1,1,10,11,2,kernel_set_double(["sum","diff","mul","div"])(), 0, 32)

#print(dcgp)

'''
Results:
d-CGP Expression:
        Number of inputs:               1
        Number of outputs:              1
        Number of rows:                 1
        Number of columns:              10
        Number of levels-back allowed:  11
        Basis function arity:           [2, 2, 2, 2, 2, ... ]
        Start of the gene expressing the node:          [0, 0, 3, 6, 9, ... ]

        Resulting lower bounds: [0, 0, 0, 0, 0, ... ]
        Resulting upper bounds: [3, 0, 0, 3, 1, ... ]

        Current expression (encoded):   [3, 0, 0, 1, 1, ... ]
        Active nodes:                   [0, 1, 2, 3, 4, ... ]
        Active genes:                   [0, 1, 2, 3, 4, ... ]

        Function set:                   [sum, diff, mul, div]
        Number of ephemeral constants:                  0
        Ephemeral constants names:                      []
        Ephemeral constants values:                     []

'''


#print(dcgp(["x"]))
#['((((x/x)-x)+((((x/x)-x)/((x/x)-x))*(x/x)))*x)']

dcgp = expression_gdual_double(1,1,1,10,11,2,kernel_set_gdual_double(["sum","diff","mul","div"])(), 0, 32)
#print(dcgp)

'''
d-CGP Expression:
        Number of inputs:               1
        Number of outputs:              1
        Number of rows:                 1
        Number of columns:              10
        Number of levels-back allowed:  11
        Basis function arity:           [2, 2, 2, 2, 2, ... ]
        Start of the gene expressing the node:          [0, 0, 3, 6, 9, ... ]

        Resulting lower bounds: [0, 0, 0, 0, 0, ... ]
        Resulting upper bounds: [3, 0, 0, 3, 1, ... ]

        Current expression (encoded):   [3, 0, 0, 1, 1, ... ]
        Active nodes:                   [0, 1, 2, 3, 4, ... ]
        Active genes:                   [0, 1, 2, 3, 4, ... ]

        Function set:                   [sum, diff, mul, div]
        Number of ephemeral constants:                  0
        Ephemeral constants names:                      []
        Ephemeral constants values:                     []

'''

#print(dcgp(["x"]))
#['((((x/x)-x)+((((x/x)-x)/((x/x)-x))*(x/x)))*x)']


print(dcgp.get_rows())