import numpy as np

class Lattice:

    # this is a 2D system ! With 1 degree of freedom per site

    A = []

    def __init__(self, params):

        print("Setting up lattice.")

        self.Lx = params['Lx']
        self.Ly = params['Ly']

        self.nrSites = self.Lx*self.Ly

        self.A = np.empty([ self.nrSites, self.nrSites ])


    def setValuesSites(self, typeInitVals):
        #self.dataSites = np.copy(vals)

        print("Initializing values of lattice sites.")

        if typeInitVals=='random':
            self.dataSites = np.random.uniform( self.nrSites )
        elif typeInitVals=='ones':
            self.dataSites = np.ones( self.nrSites )
        elif typeInitVals=='zeroes':
            self.dataSites = np.zeros( self.nrSites )
        else:
            raise Exception("Unknown type of initialization for site values.")


    def buildMatrix(self):

        print("Building matrix from lattice.")

        # TODO
        pass



    def getMatrix(self):
        return self.A
