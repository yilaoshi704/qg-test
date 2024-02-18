import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 汉化字体
matplotlib.rc("font", family='DengXian')


def transform(cls):
    if cls == 'setosa':
        return 0
    elif cls == 'versicolor':
        return 1
    elif cls == 'virginica':
        return 2
    else:
        return -1


def load_data():
    # 读取进来会成为一个元组，无法切片，很奇怪，所以进行曲线救国
    datas = np.genfromtxt("iris.csv", delimiter=',', dtype=None, encoding=None, skip_header=1)
    data = []
    for i in datas:
        data.append(i.tolist())
    data = np.array(data)
    # print(data)
    features = []
    labels = []
    for i in data:
        features.append(i[0:4])
        labels.append(transform(i[4]))
    features = np.array(features)
    labels = np.array(labels)
    # print(features)
    # print(labels)
    # 随机打乱数据集
    np.random.seed(42)
    indices = np.random.permutation(len(features))
    features = features[indices]
    labels = labels[indices]

    # 划分训练集（80%）和测试集（20%）
    train_size = int(0.8 * len(features))
    features_train, features_test = features[:train_size], features[train_size:]
    labels_train, labels_test = labels[:train_size], labels[train_size:]
    return features_train, features_test, labels_train, labels_test


# 主程序
features_train, features_test, labels_train, labels_test = load_data()
print(features_test)
