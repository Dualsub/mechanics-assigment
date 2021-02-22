from num_solution import compute
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    t, pos = compute(T=(0, 20.0), substep=0.08, xi_0=10)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, #projection='3d'#
    )
    # X = list([p[0] for p in pos])
    # Y = list([p[1] for p in pos])
    # Z = list([p[2] for p in pos])
    ax.plot(t, pos)
    plt.show()


if(__name__ == "__main__"):
    main()