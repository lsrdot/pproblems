# -*- coding: utf-8 -*-
# area = π . raio2
PI = 3.14159


def main():
    radius = input()
    if isfloat(radius):
        area = PI * float(radius) ** 2
        print(f'A={area:.4f}')


def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
