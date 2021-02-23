import numpy as np
from scipy.integrate import odeint
from equation_calc import calc_diff, printLatex
from sympy import *
import math

def compute(T : tuple = (0, 10.0), substep : float = 0.1, xi_0 : float = 10.0, xi_vel_0 : float = 0.0, m_0 : float = 1.0, omega_0 : float = math.pi, computePos : bool = False):
    diff_eq, xi, f, t, omega, m, g  = calc_diff()
    
    f_xi_0 = 0.2*xi**2 + 2
    diff_eq_0 = diff_eq.subs([(g, 9.82), (omega, omega_0), (m, m_0), (f, f_xi_0)]).simplify()
    d2xi_dt2 = solve(diff_eq_0, xi.diff(t,t))[0]

    # print(xi_expr)
    T_vals = np.linspace(T[0], T[1], int((T[1]-T[0]) / substep))
    
    def model(Y, t_in):
        X1 = Y[1]
        X2 = d2xi_dt2.subs([(xi.diff(t), Y[1]), (xi, Y[0])]).evalf()
        return [X1, X2]

    SOL = odeint(model, [xi_0, xi_vel_0], T_vals)
    SOL_xi = list([SOL[i][0] for i in range(len(SOL))])

    if(computePos):
        positions = list([(SOL_xi[i] * math.cos(omega_0*T_vals[i]), SOL_xi[i] * math.sin(omega_0*T_vals[i]), f_xi_0.subs(xi, SOL_xi[i])) for i in range(len(SOL_xi))])
        return T_vals, positions
    else:
        return T_vals, SOL_xi


if(__name__ == "__main__"):
    compute(T=(0, 10.0))