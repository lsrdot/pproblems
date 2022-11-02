# -*- coding: utf-8 -*-


PESO = (3.5, 7.5)


def main():
    a, b = input(), input()
    if isfloat(a, b):
        a, b = float(a), float(b)
        media = (a * PESO[0] + b * PESO[1]) / (PESO[0] + PESO[1])
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
