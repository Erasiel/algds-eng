import math
from typing import Callable
from matplotlib import pyplot as plt

Function = Callable[[float], float]


def f01(n: float) -> float:
    return (5 * (n ** 3) +
            7 * (n ** 2) +
            8 * (n ** 6) +
            6 * n * math.log(n, 2) +
            2 * n +
            6 * (n ** 4))


def f02(n: float) -> float:
    return (7.3 * math.log(n, 2) +
            0.5 * math.sqrt(n) +
            1.2 * math.log(math.log(n, 2), 2) +
            11)


def f03(n: float) -> float:
    return (10 * (n ** 3) +
            5 * n +
            8 * n * math.log(n, 2) +
            3 * (n ** 7) +
            (1.3 ** n))


def visualize(f: Function,
              g: Function,
              c: float,
              n0: float,
              n_points: int = 1000,
              start: float = 1 + 1e-7,
              step: float = 1
) -> None:
    f_values = [f(start + i * step) for i in range(n_points)]
    g_values = [c * g(start + i * step) for i in range(n_points)]

    plt.plot(f_values, label="$f(n)$")
    plt.plot(g_values, label="$cg(n)$")
    plt.axvline(n0 // step, color="black", label="$n_0$")
    plt.xticks([n0 // step], ["$n_0$"])
    plt.xlabel("$n$")
    plt.ylabel("Function value")
    plt.legend()
    plt.show()

# TODO: visualize f(n) = O(g(n)) relations
