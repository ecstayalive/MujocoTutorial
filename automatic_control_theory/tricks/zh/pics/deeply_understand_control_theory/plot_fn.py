import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)


def u(x: np.ndarray) -> np.ndarray:
    return np.int32(x >= 0)


def v(x: np.ndarray) -> np.ndarray:
    return np.maximum(0, x)


def a(x: np.ndarray) -> np.ndarray:
    x = np.maximum(0, x)
    return 0.5 * np.power(x, 2)


def sin(x: np.ndarray) -> np.ndarray:
    return np.sin(x)


plt.plot(x, u(x)
         - 2 * u(x - 1)
         + 2 * u(x - 2)
         - 2 * u(x - 3)
        #  + 2 * u(x - 4)
         )
plt.show()
