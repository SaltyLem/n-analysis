import os

import numpy as np
import pandas as pd


def main():
    dirname = os.path.dirname(__file__)
    table1 = pd.read_csv(f"{dirname}/winequality-red.csv", encoding="UTF-8", sep=";")
    result = []
    for i in table1:
        rs = [
            table1[i].mean(),
            table1[i].max(),
            table1[i].min(),
            table1[i].var(ddof=0),
            np.sqrt(table1[i].var(ddof=0)),
        ]
        result.append(rs)
        print(i)
        print(f"平均: {rs[0]}")
        print(f"最大値: {rs[1]}")
        print(f"最小値: {rs[2]}")
        print(f"分散: {rs[3]}")
        print(f"標準偏差: {rs[4]}")

    df = pd.DataFrame(
        result, index=table1.columns, columns=["平均", "最大値", "最小値", "分散", "標準偏差"]
    )
    df.to_csv(f"{dirname}/result.csv", encoding="UTF-8")
