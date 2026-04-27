import numpy as np


def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / h


def back_difference(f, x, h=1e-5):
    return (f(x) - f(x - h))


def second_difference(f, x, h=1e-5):
    return (f(x + h) - 2*f(x) + f(x - h)) / h**2


