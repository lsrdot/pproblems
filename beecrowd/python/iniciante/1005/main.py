# -*- coding: utf-8 -*-


PESOS = (3.5, 7.5)


def main():
    a, b = input(), input()
    if isfloat(a, b):
        a, b = float(a), float(b)
        media = (a * PESOS[0] + b * PESOS[1]) / (PESOS[0] + PESOS[1])
        print(f'MEDIA = {media:.5f}')


def isfloat(*n):
    try:
        for x in n:
            float(x)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
