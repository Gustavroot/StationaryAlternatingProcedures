# GMRES imports
#from scipy.sparse import csc_matrix
from scipy.sparse.linalg import gmres

# Hybrid GMRES imports
from hybridgmres import HybridGMRES

class LocalSolvers:

    def __init__(self, params):

        #self.A = params['matrix']
        #self.b = params['rhs']
        #self.x0 = params['initGuess']

        self.solverName = params['method']

        if self.solverName=='hybridGMRES':
            self.solverHandler = HybridGMRES()
            # TODO
            #self.solverHandler.hybridSetup()


    def solve(self, block_A, block_b, block_x0, block_tol):

        if self.solverName=='GMRES':
            x, exitCode = gmres(block_A, block_b, x0=block_x0, tol=block_tol)
            if exitCode!=0:
                raise Exception("Local solver failed to solve by using GMRES.")
            else:
                return x
        elif self.solverName=='hybridGMRES':
            self.solverHandler.solve()
