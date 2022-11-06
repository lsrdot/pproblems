import math

# -*- coding: utf-8 -*-


def main():
    x1, y1 = input().split(' ')
    x2, y2 = input().split(' ')
    x1, y1 = float(x1), float(y1)
    x2, y2 = float(x2), float(y2)
    d = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    print(f'{d:.4f}')


if __name__ == "__main__":
    main()
