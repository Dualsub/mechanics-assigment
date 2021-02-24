from sympy import *
import numpy as np

# För att printa det korrekta LaTex-uttrycket.
def printLatex(expr):
    print(r"\\"+"\n", latex(expr).replace("ξ", r"\xi").replace("ω", r"\omega_0"))

# Symbolisk beräkning av differential ekvationen.
def calc_diff():
    
    # A1
    
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

    # Tangentvektorn fås genom att derivera r med avseende på ξ(t).
    T = np.array([
        x.diff(xi_t), 
        y.diff(xi_t), 
        z.diff(xi_t)
    ])

    # A2

    # Enhetsvektorn längsmed 
    e_s = T / sqrt(np.sum(T**2))

    VL = np.dot(m*a, e_s)

    F = np.array([0,0,-m*g])

    HL = np.dot(F, e_s).simplify()

    diffEq = Eq(VL, HL)

    # Returnerar symboler så att användaren av funktionen kan utföra substitutioner.
    return diffEq.simplify(), xi_t, f_xi, t, omega, m, g

if(__name__ == "__main__"):
    init_printing(use_unicode=True)
    _ = calc_diff()