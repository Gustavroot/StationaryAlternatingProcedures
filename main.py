from schwarzprocedures import SchwarzProcedures
from lattice import Lattice
import numpy as np

print("\n")

# Creation of the lattice and associated matrix
paramsLattice = dict()
paramsLattice['Lx'] = 16
paramsLattice['Ly'] = 16
latt = Lattice(paramsLattice)
latt.setValuesSites('random')
latt.buildMatrix()
A = latt.getMatrix()

# Creation of the solver
paramsSolver = dict()
paramsSolver['matrix'] = A
paramsSolver['globalTolerance'] = 10e-6
paramsSolver['localTolerance'] = 10e-2
solver = SchwarzProcedures(paramsSolver)
solver.setInitGuess('random')

# Perform solve
b = np.random.uniform( A.shape[0] )
solver.solve('multiplicativeSchwarz', b)
