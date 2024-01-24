import numpy as np

# m = np.loadtxt("C:\\Users\\张奕霖\\Desktop\\data.txt")
# print(m)
print(np.arange(1, 10, 2))  # 参数为：(起始点，终点，步长)；注意！ 不包括终点
a1 = np.array([[1],[1]])
a2 = np.eye(3)
print(a2)
a3 = np.linspace(3, 9, 3)
print(a3)
a4 = np.logspace(1, 10, 10, base=2)
print(a4)
a4 = np.vstack((a2, a3))
print(a4)
