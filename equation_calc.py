from sympy import *
import numpy as np

# För att printa det korrekta LaTex-uttrycket.
def printLatex(expr):
    print("Latex Expression:\n\n", latex(expr).replace("ξ", r"\xi").replace("ω", r"\omega_0"))

# Symbolisk beräkning av differential ekvationen.
def calc_diff():
    # Definerar variabler och funktioner
    t, omega, m, g = symbols("t, ω, m, g")
    xi, f = symbols("ξ, f", cls=Function)
    xi_t = xi(t)
    f_xi = f(xi_t)

    # Lägeverktorn defineras
    x = xi_t * cos(omega*t)
    y = xi_t * sin(omega*t)
    z = f_xi

    r = np.array([x,y,z])

    # Tangentvektorn fås genom att derivera r med avseende på ξ(t).
    tangent = np.array([
        x.diff(xi_t), 
        y.diff(xi_t), 
        z.diff(xi_t)
        ])

    # Enhetsvektorn längsmed 
    e_r = tangent / sqrt(np.sum(tangent**2))

    # Hastighet utvinns genom derivering av lägevektorn. 
    v = np.array([
        diff(x, t).simplify(),
        diff(y, t).simplify(),
        diff(z, t).simplify()
    ])

    # Accelerationen utvinns genom dervering av lägevektorn 2 ggr.
    a = np.array([
        diff(x, t, t).simplify(),
        diff(y, t, t).simplify(),
        diff(z, t, t).simplify()
    ])

    mae_r = np.dot(m*a, e_r)

    F = np.array([0,0,-m*g])

    Fe_r = np.dot(F, e_r).simplify()

    diffEq = Eq(Fe_r, mae_r)

    # Returnerar symboler så att användaren av funktionen kan utföra substitutioner.
    return diffEq.simplify(), xi_t, f_xi, t, omega, m, g

if(__name__ == "__main__"):
    init_printing(use_unicode=True)
    _ = calc_diff()