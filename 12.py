import numpy as np

# Інтеграл 1: f(x) = 1 / sqrt(3x - 1)
def f1(x):
    return 1 / np.sqrt(3 * x - 1)

# Інтеграл 2: f(x) = ln(x^2 + 1) / x
def f2(x):
    return np.log(x**2 + 1) / x

# Інтеграл 3: f(x) = 1 / sqrt(0.2x^2 + 1)
def f3(x):
    return 1 / np.sqrt(0.2 * x**2 + 1)

# Метод прямокутників
def rectangles(f, a, b, n, method='left'):
    h = (b - a) / n
    if method == 'left':
        x = np.linspace(a, b-h, n)
    elif method == 'middle':
        x = np.linspace(a + h/2, b - h/2, n)
    else:  # right
        x = np.linspace(a + h, b, n)
    return h * np.sum(f(x))

# Метод Сімпсона
def simpson(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    S = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])
    return h / 3 * S

# Метод трапецій
def trapezoidal(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))

# Обчислення інтегралів
I1_left = rectangles(f1, 1.4, 2.1, 10, 'left')
I1_middle = rectangles(f1, 1.4, 2.1, 10, 'middle')
I1_right = rectangles(f1, 1.4, 2.1, 10, 'right')

I2_simpson = simpson(f2, 0.8, 1.6, 8)
I3_trapezoidal = trapezoidal(f3, 1.3, 2.5, 20)

print(f"I1 (Left Rectangles): {I1_left:.4f}")
print(f"I1 (Middle Rectangles): {I1_middle:.4f}")
print(f"I1 (Right Rectangles): {I1_right:.4f}")
print(f"I2 (Simpson's Method): {I2_simpson:.4f}")
print(f"I3 (Trapezoidal Method): {I3_trapezoidal:.4f}")
