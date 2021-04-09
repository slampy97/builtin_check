import csv
import sys
import pandas


class MyClass:
    pass


users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]

with open("my_file.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)


def foo():
    a = 1
    b = MyClass()
    c = [1, 2, 3]
    d = pandas.read_csv("my_file.csv")
    print_vars()


def print_vars():
    for obj in sys._getframe(1).f_locals.items():
        print(f"{obj[0]}: {obj[1].__class__.__module__ == 'builtins'}")


if __name__ == '__main__':
    foo()
