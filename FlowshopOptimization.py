# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:55:06 2020

@author: Utkarsh
"""

from pyomo.environ import *
from constraints import *

m = AbstractModel()
m.jobs = Set(ordered=True)
m.machines = Set(ordered=True)
m.T = Param(m.jobs,m.machines)
m.c = Param(m.jobs,m.jobs,m.machines)
m.M = Param(within=PositiveReals)

m.S = Var(m.jobs,m.machines,within=NonNegativeReals)
m.p = Var(m.jobs,m.jobs,domain=Binary)
m.Q = Var(within=NonNegativeReals)

m.obj = Objective(expr=m.Q,sense=minimize)

m1 = m.create_instance("data.dat")
m1.machines_order_cons = Constraint(m1.jobs,m1.machines,rule=machines_order)
m1.prec_1_cons = Constraint(m1.jobs,m1.jobs,m1.machines,rule=prec_1)
m1.prec_2_cons = Constraint(m1.jobs,m1.jobs,m1.machines,rule=prec_2)
m1.Q_cons = Constraint(m1.jobs,rule=Q)

opt = SolverFactory('cbc')
result = opt.solve(m1,tee=False)

print("Solver termination condition:",result.solver.termination_condition)
print("Solver status:",result.solver.status)

print("\nResult:")
print("  Optimal Makespan =",m1.obj())










