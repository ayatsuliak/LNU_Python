import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#task1
def laguerre_func(t, n, beta=2, sigma=4):
    if t < 0 or n < 0:
        print("Sorry, but t and n value has to be greater or equal than 0.")
        print('Your values: n = ', n, ';  t = ', t)
        return

    lag0 = np.sqrt(sigma) * (np.e ** ((-1) * ((beta * t) / 2)))
    lag1 = lag0 * (1 - (sigma * t))

    if n == 0:
        return lag0
    elif n == 1:
        return lag1
    elif n >= 2:
        for i in range(2, n + 1):
            lag2 = ((2 * n - 1 - sigma * t) / n) * lag1 - ((n - 1) / n) * lag0
            lag0 = lag1
            lag1 = lag2
        return lag2
#
# #print(laguerre_func(5,3))
# #task2
# def tabulate_laguerre(_T, n, beta = 2, sigma = 4):
#     t = np.linspace(0, _T, num=50)
#     lag = [laguerre_func(i, n, beta, sigma) for i in t]
#     data = {'T': t, 'L': [lag]}
#     return data
#
# data_table = {'Tabulation' : [round(i,1) for i in tabulate_laguerre(8,2)['T']],
#         'Lagguere results' : [round(i,5) for i in tabulate_laguerre(8,2)['L'][0]]}
# df = pd.DataFrame(data_table)
# #print(df)
#
# #task3
#
# def func3(eps, t, n, beta = 2, sigma = 4):
#     result = np.array([])
#     while True:
#         for i in range(n+1):
#             res = laguerre_func(t, i, beta, sigma)
#             if np.abs(res) < eps:
#                 result.append(res)
#                 t += 0.01
#             else:
#                 break
#                 return result
#
#
# def func3(eps, t, n, beta = 2, sigma = 4):
#     result = np.array([])
#
#     for i in range(n+1):
#         res = laguerre_func(t, i, beta, sigma)
#         while np.abs(res) < eps:
#             result.append(res)
#             t += 0.01
#
#     return result
#
#
#
# print(func3(0.0001, 0.1, 20))
#
#
#
# # print(func2(8, 20, 0.0001))
# #


def construct_a_graph(data):
    plt.plot(data['T'], data['L'][0], label='desired graph n=n')
    plt.grid(True)
    plt.title('LAGUERRE\'S FUNCTION')
    plt.xlabel('tabulation - axis')
    plt.ylabel('laguerre results(t) - axis')
    plt.legend()
    plt.show()
# #
# # construct_a_graph(tabulate_laguerre(8,2))
# #
# # def func(_T, n, eps, beta = 2, sigma = 4):
# #     t = np.linspace(0, _T, num=50)
# #     lag = [laguerre_func(i, n, beta, sigma) for i in t]
# #     data_table = {'Tabulation': [round(i, 1) for i in tabulate_laguerre(8, 2)['T']],
# #                   'Lagguere results': [round(i, 5) for i in tabulate_laguerre(8, 2)['L'][0]]}
# #     df = pd.DataFrame(data_table)
# #     print(abs(df["Lagguere results"]) < eps)
# #
# #
# #
#
#
#
# #task4
# def transformation_Laguerre(f, a, T, N, num_of_points, eps, alpha, sigma = 4, beta = 2):
#     points = np.linspace(a, T, num_of_points)
#     delta = (T - a) / (num_of_points - 1)
#
#     func0 = np.zeros(N+1)
#     func1 = np.array([np.sum(np.multiply([f(i) for i in points], [laguerre_func(k, p, beta, sigma) for k in points]) * np.e**(-alpha*points) * delta) for p in range(N+1)])
#
#     while (np.abs(func1 - func0) > eps).any():
#         func0 = func1
#         num_of_points *= 2
#         points = np.linspace(a, T, num_of_points)
#         delta = (T - a) / (num_of_points - 1)
#         func1 = np.array([np.sum(np.multiply([f(i) for i in points], [laguerre_func(k, p, beta, sigma) for k in points]) * np.e**(-alpha*points) * delta) for p in range(N+1)])
#     return func1
#
# #task5
# def f(t):
#     if t >= 0 and t <= 2 * np.pi:
#         return np.sin(t - 2 * np.pi) + 1
#     else:
#         return 0
#
# a=0
# T=5
# N=20
# alpha=3
# eps=0.01
# func = transformation_Laguerre(f, a, T, N, 50, eps, alpha)
# #print(func)
#
# #task6
# def func6(t, seq, beta = 2, sigma = 4):
#     lag = [laguerre_func(t, i, beta, sigma) for i in range(len(seq))]
#     h = np.sum(seq + lag)
#     return h
#
# h = np.array([0, 2, 6, 1])
# t = 5
# result = func6(t, h)

#task7
# a = 0
# T = 2*np.pi
# N_range = [10, 20, 30, 50, 75, 100]
# alpha = 3
# eps = 0.01
#
# num_of_points = 150
# delta = (T - a) / (num_of_points - 1)
# t_range = np.linspace(a, T, num_of_points)
#
# f_N = []
# for n in N_range:
#     f_N.append(func6(transformation_Laguerre(f, a, T, n, alpha, eps), t)for t in t_range)
#
# for i in range(len(N_range)):
#     plt.plot(t_range, f_N[i], f'f_{N_range[i]} (t)')
#
# plt.grid(True)
# plt.xlabel('t')
# plt.ylabel('f(t)')
# plt.legend()
# plt.show()

def method_of_rectangles(f, a, b, num_of_points):
    points = np.linspace(a, b, num_of_points)
    S = np.sum(f(points)) * (b - a)/(num_of_points - 1)
    return S

def integral(f, a, b, N, num_of_points, alpha, beta, sigma):
    points = np.linspace(a, b, num_of_points)
    delta = (b - a) / (num_of_points - 1)

    return np.array([np.sum(np.multiply([f(i) for i in points], [laguerre_func(k, p, beta, sigma) for k in points]) * np.e**(-alpha*points) * delta) for p in range(N+1)])

def transformation_Laguerre(f, a, T, N, num_of_points, eps, alpha, beta = 2, sigma = 4):
    func0 = np.zeros(N+1)
    func1 = integral(f, a, T, N, num_of_points, alpha, beta, sigma)

    while (np.abs(func1 - func0) > eps).any():
        func0 = func1
        num_of_points *= 2
        func1 = integral(f, a, T, N, num_of_points, alpha, beta, sigma)
    return func1

def f(t):
    if t >= 0 and t <= 2 * np.pi:
        return np.sin(t - 2 * np.pi) + 1
    else:
        return 0

a = 0
T = 1
N = 20
alpha = 2
eps = 0.001
func = transformation_Laguerre(f, a, T, N, 50, eps, alpha)
print(func)