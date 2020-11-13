# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:03:06 2020

@author: 91824
"""

from pyomo.environ import *

def machines_order(m,i,k):
    if k == m.machines[-1]:
        return Constraint.Skip
    else:
        return m.S[i,m.machines.next(k)] >= m.S[i,k] + m.T[i,k]
    
def prec_1(m,i,j,k):
    if m.jobs.ord(i) >= m.jobs.ord(j):
        return Constraint.Skip
    else:
        return m.S[j,k] >= m.S[i,k]+m.T[i,k]+m.c[i,j,k]-m.M*(1-m.p[i,j])
    
def prec_2(m,i,j,k):
    if m.jobs.ord(i) >= m.jobs.ord(j):
        return Constraint.Skip
    else:
        return m.S[i,k] >= m.S[j,k]+m.T[j,k]+m.c[j,i,k]-m.M*(m.p[i,j])
    
def Q(m,i):
    k = m.machines[-1]
    return m.Q >= m.S[i,k]+m.T[i,k] 