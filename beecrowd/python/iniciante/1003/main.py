# -*- coding: utf-8 -*-


def main():
    a, b = input(), input()
    if valid_int_sum(a, b):
        a, b = int(a), int(b)
        soma = a + b
        print(f'SOMA = {soma}')


def valid_int_sum(x, y):
    try:
        int(x)
        int(y)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
