# Turning SAP into a stationary method when using GMRES-type local solvers

Immediate TODOs:

 -- set-up an appropriate Domain Decomposition of the chosen system

 -- implement the method multiplicativeSchwarz(...) of the class SchwarzProcedures. For this,
    when performing local solves, choose for now the <GMRES> when calling the method solve(...)
    of the LocalSolvers class

 -- implement Hybrid GMRES and use instead of GMRES for the block solves
