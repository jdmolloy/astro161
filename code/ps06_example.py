#! /usr/bin/env python
import numpy as np, pylab

def scale_factor(t):
    a = np.ones_like(t) # Do your calculation here
    return a

def n_neutrino(T, n1eV=5e13):
    n = np.ones_like(T) * n1eV # Do your real calculation here
    return m

def sigma_neutrino(T, s1MeV=1e-43):
    sigma = np.ones_like(T) * s1MeV # Do your real calculation here
    return sigma

def time_to_temp(t):
    T = np.ones_like(t) # Do your real calculation here
    return T

def calc_collision_rate(t, n1eV=5e13, s1MeV=1e-43):
    rate = np.ones_like(t) # Do your real calculation here
    return rate

def calc_n_over_p(t, n1eV=5e13, s1MeV=1e-43):
    n_over_p = np.ones_like(t) # Do your real calculation here
    return n_over_p

def calc_D_over_n(t, eta=5e-10, dE=2.2):
    D_over_n = np.ones_like(t) # Do your calculation here
    return D_over_n

t = np.logspace(.001, 300, num=1000)
pylab.plot(t, calc_D_over_n(t))
pylab.show()

