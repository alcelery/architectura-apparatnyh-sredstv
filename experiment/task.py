from tabulate import tabulate

def example1(a, b, c):
    return (~ (a & b)) | (~ (a | c))

def example2(a, b, c):
    return (a & b) | (~b & c)

def example3(a, b, c):
    return (a & b) | (~ c)


def main():
    table_inf = [
        [0, 0, 0, example1(0, 0, 0), example2(0, 0, 0), example3(0, 0, 0)],
        [0, 0, 1, example1(0, 0, 1), example2(0, 0, 1), example3(0, 0, 1)],
        [0, 1, 0, example1(0, 1, 0), example2(0, 1, 0), example3(0, 1, 0)],
        [0, 1, 1, example1(0, 1, 1), example2(0, 1, 1), example3(0, 1, 1)],
        [1, 0, 0, example1(1, 0, 0), example2(1, 0, 0), example3(1, 0, 0)],
        [1, 0, 1, example1(1, 0, 1), example2(1, 0, 1), example3(1, 0, 1)],
        [1, 1, 0, example1(1, 1, 0), example2(1, 1, 0), example3(1, 1, 0)],
        [1, 1, 1, example1(1, 1, 1), example2(1, 1, 1), example3(1, 1, 1)],
    ]

    print(tabulate(table_inf, headers=["A", "B", "C", "Выражение 1", "Выражение 2", "Выражение 3"], tablefmt="grid"))

main()