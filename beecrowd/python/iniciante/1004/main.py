# -*- coding: utf-8 -*-


def main():
    x, y = input(), input()
    if can_multiply(x, y):
        x, y = int(x), int(y)
        prod = x * y
        print(f'PROD = {prod}')


def can_multiply(a, b):
    try:
        int(a)
        int(b)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
