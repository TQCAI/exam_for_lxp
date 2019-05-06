from sklearn.datasets import make_classification
import pylab as plt
from random import randint
from math import sqrt
from collections import Counter
import numpy as np


def get_dist(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def solve(X, Y, X_q, k):
    ans_list = []
    for qpt in X_q:
        data = []
        for xpt, label in zip(X, Y):
            dist = get_dist(xpt, qpt)
            data.append({'label': label, 'dist': dist})
        data.sort(key=lambda x: x['dist'])
        data = data[:k]
        label_list = [item['label'] for item in data]
        cnt_dict = Counter(label_list)
        max_cnt, ans_label = max(zip(cnt_dict.values(), cnt_dict.keys()))
        ans_list.append(ans_label)
    return ans_list


def decay_precision(arr, precision='.2f'):
    def decay(x):
        s = f'{x:.2f}'
        return float(s)

    ans_list = []
    for x, y in arr:
        ans_list.append([decay(x), decay(y)])
    return np.array(ans_list)


def generate(n_samples, labels, q, k, index):
    X, Y = make_classification(n_samples=n_samples, n_features=2, n_redundant=0, n_clusters_per_class=1,
                               n_classes=labels)
    X=decay_precision(X)
    X_query, _ = make_classification(n_samples=q, n_features=2, n_redundant=0, n_clusters_per_class=1, n_classes=2)
    X_query=decay_precision(X_query)
    with open(f'knn_data/Test{index + 1:02}.in', 'w+') as f:
        print(n_samples, labels, k, file=f)
        for pt, label in zip(X, Y):
            print(f"{pt[0]:.2f} {pt[1]:.2f} {label}", file=f)
        print(q, file=f)
        for pt in X_query:
            print(f"{pt[0]:.2f} {pt[1]:.2f}", file=f)
    return X, Y, X_query


def writeout_ans_list(ans_list, index):
    with open(f'knn_data/Test{index + 1:02}.ans', 'w+') as f:
        print(*ans_list, file=f)


def generate_demo():
    n_samples = 5
    k = 2
    q = 3
    labels = 2
    X, Y, X_q = generate(n_samples, labels, q, k, 0)
    ans_list = solve(X, Y, X_q, k)
    writeout_ans_list(ans_list, 0)

if __name__ == '__main__':
    for i in range(1, 10):
        n_samples = randint(3, 100)
        k = randint(2, min(n_samples, 5))
        labels=randint(2,min(n_samples,4))
        q=randint(5,20)
        X, Y, X_q = generate(n_samples, labels, q, k, i)
        ans_list = solve(X, Y, X_q, k)
        writeout_ans_list(ans_list, i)
