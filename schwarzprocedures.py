from localsolvers import LocalSolvers
import numpy as np

class SchwarzProcedures:

    # The solution vector
    x = []

    methodsAvailable = ['multiplicativeSchwarz', 'additiveSchwarz']

    def __init__(self, params):

        print("Initializing Schwarz solver.")

        # The matrix to be solved
        self.A = params['matrix']

        self.vecsLength = self.A.shape[0]

        # Accurary of the solve
        self.globalTol = params['globalTolerance']
        self.localTol = params['localTolerance']

        # The solve must stop at some point
        if 'maxNrIters' in params:
            self.maxNrIters = params['maxNrIters']
        else:
            self.maxNrIters = 1000000

        paramsLocalSolver = dict()
        paramsLocalSolver['method'] = 'GMRES'
        self.localSolver = LocalSolvers(paramsLocalSolver)



    def setInitGuess(self, typeInitGuess):

        print("Setting initial guess for Schwarz solver.")

        if typeInitGuess=='random':
            self.x = np.random.uniform( self.vecsLength )
        elif typeInitGuess=='ones':
            self.x = np.ones( self.vecsLength )
        elif typeInitGuess=='zeroes':
            self.x = np.zeros( self.vecsLength )
        else:
            raise Exception("Unknown type of initialization for initial guess.")


    def solve(self, method, b):

        print("\nSolving...")

        if method not in self.methodsAvailable:
            raise Exception("The requested Schwarz Procedure is not available.")

        if method=='multiplicativeSchwarz':
            self.multiplicativeSchwarz( b )
        elif method=='additiveSchwarz':
            self.additiveSchwarz( b )

        print("...done.")


    def multiplicativeSchwarz(self, b):
        # TODO
        for i in range(self.maxNrIters):

            # within here, call: x(sliced) = self.localSolver.solve( A(sliced), b(sliced), x(sliced) )

            pass


    def additiveSchwarz(self, b):
        # TODO
        for i in range(self.maxNrIters):
            pass
