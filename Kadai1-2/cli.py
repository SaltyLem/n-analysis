import itertools
import os

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

dirname = os.path.dirname(__file__)
path = f"{dirname}/output"


def main():
    table1 = pd.read_csv(f"{dirname}/winequality-red.csv", encoding="UTF-8", sep=";")
    if not os.path.exists(path):  # ディレクトリが存在しない場合、作成する。
        os.makedirs(path)

    pairs = itertools.combinations(table1.columns, 2)
    print("相関係数")
    print(table1.corr())
    for p in pairs:
        reg = linear_model.LinearRegression()
        xlabel = p[0]
        ylabel = p[1]
        x_values = table1[xlabel]
        y_values = table1[ylabel]
        x = table1.loc[:, [xlabel]].values
        y = y_values.values
        reg.fit(x, y)
        plt.figure()
        plt.scatter(x_values, y_values, s=5, color="c")
        plt.plot(x_values, reg.predict(x))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(f"{path}/{xlabel.replace(' ', '_')}-{ylabel.replace(' ', '_')}.png")
        plt.close()
        print(p)

    table1.corr().to_csv(f"{dirname}/corr.csv", encoding="UTF-8")
