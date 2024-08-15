import math
import matplotlib.pyplot as plt
import pltpublish as pub


def plotting() -> None:
    X = [x / 100 * math.pi for x in range(100)]
    Y1 = [math.sin(x) for x in X]
    plt.plot(X, Y1, label=r"$\sin(x)$")
    Y2 = [math.cos(x) for x in X]
    plt.plot(X, Y2, label=r"$\cos(x)$")
    Y3 = [0.25 * math.sin(x) + 0.5 * math.cos(4 * x) for x in X]
    plt.plot(X, Y3, label=r"$\frac{1}{4}\sin(x)+\frac{1}{2}\cos(4x)$")
    Y4 = [0.5 * math.sin(2 * x) ** 2 + 1 / 3 * math.cos(4 * x) for x in X]
    plt.plot(X, Y4, label=r"$\frac{1}{2}\sin(2x)^2+\frac{1}{3}\cos(4x)$")
    plt.xlabel("Angle in radians")
    plt.ylabel("Something interesting")
    plt.legend()


def classic() -> None:
    plt.figure()
    plotting()
    plt.savefig("classic.png")


def pltpublish() -> None:
    pub.setup()
    plt.figure()
    plotting()
    pub.save_fig("pltpublish.png")


def set_size() -> None:
    pub.setup()
    plt.figure()
    pub.set_size_pixels(800, 600)
    plotting()
    pub.save_fig("pltpublish_800x600.png", scale=2)


def colors() -> None:
    pub.setup()
    plt.figure()
    pub.shift_color_cycle()
    plotting()
    pub.save_fig("pltpublish_colors.png")


if __name__ == "__main__":
    # in that order
    classic()
    pltpublish()
    set_size()
    colors()
