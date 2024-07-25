import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    r1 = np.linspace(x_min, x_max, width)
    r2 = np.linspace(y_min, y_max, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def plot_mandelbrot(width=800, height=800, x_min=-2.0, x_max=1.0, y_min=-1.5, y_max=1.5, max_iter=256):
    X, Y, Z = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
    plt.imshow(Z.T, cmap='viridis', extent=(x_min, x_max, y_min, y_max))
    plt.show()

plot_mandelbrot()
