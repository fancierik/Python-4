import numpy as np
import matplotlib.pyplot as plt

def data():
    VY = [-1.86,-1.95,-2.12,-2.06,-2.15,-2.00,-2.12,-2.31,-2.29,-2.57,-2.56,-2.86,-2.85,-3.03,-3.25,-3.08,-3.29,-3.67,-3.70,-3.85]
    VX = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]
    return VX, VY

def approximation(X, Y, m):
    A = np.array([[np.sum([np.power(X[t], j) for t in range(0, len(X))])
                   for j in range(i, i+m+1)] for i in range(0, m+1)])
    B = np.array([np.sum([np.power(X[j], i)*Y[j] for j in range(0, len(X))])
                  for i in range(0, m+1)])
    p = np.linalg.solve(A, B)
    pred = np.array([predict(X[j], p) for j in range(len(X))])
    return p, pred

def predict(x, p):
    return np.sum([p[i]*np.power(x, i) for i in range(len(p))])

def error(t, s):
    return np.sqrt(np.sum(np.power((t-s),2))/len(t))

def stdev():
    err = []
    for i in range(20):
        p, pred = approximation(VX, VY, i+1)
        err.append(error(pred, VY))
    return err

def chart1():
    VX, VY = data()
    x = np.arange(0, 2, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, '*r')
    p1, pred1 = approximation(VX, VY, 1)
    p2, pred2 = approximation(VX, VY, 2)
    p3, pred3 = approximation(VX, VY, 3)
    plt.plot(x, np.array([predict(x[i], p1) for i in range(len(x))]), '-b', label='m = 1')
    plt.plot(x, np.array([predict(x[i], p2) for i in range(len(x))]), '-g', label='m = 2')
    plt.plot(x, np.array([predict(x[i], p3) for i in range(len(x))]), '--y', label='m = 3')
    plt.legend()
    plt.grid()
    plt.show()

def chart2():
    VX, VY = data()
    x = np.arange(0, 2, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, '*r')
    p4, pred4 = approximation(VX, VY, 4)
    p5, pred5 = approximation(VX, VY, 5)
    p6, pred6 = approximation(VX, VY, 6)
    plt.plot(x, np.array([predict(x[i], p4) for i in range(len(x))]), '-b', label='m = 4')
    plt.plot(x, np.array([predict(x[i], p5) for i in range(len(x))]), '-g', label='m = 5')
    plt.plot(x, np.array([predict(x[i], p6) for i in range(len(x))]), '--y', label='m = 6')
    plt.legend()
    plt.grid()
    plt.show()

def chart3():
    VX, VY = data()
    x = np.arange(0, 2, 0.01)
    fig, lin = plt.subplots()
    lin.plot(VX, VY, '*r')
    p7, pred7 = approximation(VX, VY, 7)
    p8, pred8 = approximation(VX, VY, 8)
    plt.plot(x, np.array([predict(x[i], p7) for i in range(len(x))]), '-b', label='m = 7')
    plt.plot(x, np.array([predict(x[i], p8) for i in range(len(x))]), '--g', label='m = 8')
    plt.legend()
    plt.grid()
    plt.show()

VX, VY = data()
errors = stdev()
for i, error_value in enumerate(errors, start=0):
    print(f"RMSE (m={i}): {error_value:.10f}")


chart1()
chart2()
chart3()
