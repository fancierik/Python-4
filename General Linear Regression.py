import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def data():
    VY =  [-1.86,-1.95,-2.12,-2.06,-2.15,-2.00,-2.12,-2.31,-2.29,-2.57,-2.56,-2.86,-2.85,-3.03,-3.25,-3.08,-3.29,-3.67,-3.70,-3.85]
    VX = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]
    return VY, VX

def f(x, a = 1, b = 2, c = 1):
    return  a / x + b * x * x + c * np.e ** x

def chart():
    VY, VX = data()
    x = np.arange(0, 2, 0.01)
    fig, lin = plt.subplots()
    popt, pcov = curve_fit(f, VX, VY)
    lin.plot(VX, VY, '*r')
    plt.plot(x, np.array([f(i, popt[0], popt[1], popt[2]) for i in x]), '-b')
    lin.set_title('Линейная регрессия общего вида')
    plt.grid()
    plt.show()

chart()