import json
import pandas as pd


# task_1
def f1(x):
    return x/(x+100)


def f2(x):
    return 1 / x


# task_2
def f3(x):
    return 20 * (f1(x) + f2(x)) / x


# task_3
dic = {x: [f1(x), f2(x), f3(x)] for x in range(5, 90, 1)}
print(dic)

# task_4
csv_columns = ['x', 'f1(x)', 'f2(x)', 'f3(x)']
pd.DataFrame(dic).T.reset_index().to_csv('csvfile.csv', header=csv_columns, index=False)

# task_5
df = pd.read_csv('csvfile.csv', delimiter=',')
list_of_rows = [list(row) for row in df.values]
print(list_of_rows)

# task_6
with open('data.json', 'w') as file:
    json.dump(list_of_rows, file, indent=4)
