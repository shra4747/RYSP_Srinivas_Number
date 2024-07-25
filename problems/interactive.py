import ipywidgets as widgets
from IPython.display import display

def interactive_plot(a=1.0):
    x = np.linspace(0, 10, 1000)
    y = np.sin(a * x)
    plt.plot(x, y)
    plt.show()

widgets.interact(interactive_plot, a=(0.1, 10.0, 0.1))
