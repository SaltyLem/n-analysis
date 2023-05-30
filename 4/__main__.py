import os

import pandas as pd
import scipy as sp


def newton_1(x: int):
    return x**2 + 2 * x


dirname = os.path.dirname(__file__)
print(sp.optimize.newton(newton_1, -1))
print(sp.optimize.newton(newton_1, 0))

random_table1 = pd.read_csv(f"{dirname}/random1.csv", encoding="UTF-8")
print(random_table1)

random_table2 = pd.read_csv(f"{dirname}/random2.csv", encoding="UTF-8")
print(random_table2)

random_table = pd.merge(random_table1, random_table2, on="id")
print(random_table)

random_table.to_csv(f"{dirname}/random_result.csv", encoding="UTF-8")
