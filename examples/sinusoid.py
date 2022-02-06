import math
from tkinter.messagebox import NO
import matplotlib.pyplot as plt
import pltpublish as pub


def plotting() -> None:
    plt.figure()
    X = [x / 100 * math.pi for x in range(100)]
    Y1 = [math.sin(x) for x in X]
    plt.plot(X, Y1, label=r'$\sin(x)$')
    Y2 = [math.cos(x) for x in X]
    plt.plot(X, Y2, label=r'$\cos(x)$')
    Y3 = [.25 * math.sin(x) + .5 * math.cos(4*x) for x in X]
    plt.plot(X, Y3, label=r'$\frac{1}{4}\sin(x)+\frac{1}{2}\cos(4x)$')
    Y4 = [.5 * math.sin(2*x)**2 + 1/3 * math.cos(4*x) for x in X]
    plt.plot(X, Y4, label=r'$\frac{1}{2}\sin(2x)^2+\frac{1}{3}\cos(4x)$')
    plt.xlabel("Angle in radians")
    plt.ylabel("Something interesting")
    plt.legend()


def classic() -> None:
    plotting()
    plt.savefig("classic.png")

def pltpublish() -> None:
    pub.setup()
    plotting()
    pub.save_fig("pltpublish.png")

if __name__ == "__main__":
    # in that order
    classic()
    pltpublish()
