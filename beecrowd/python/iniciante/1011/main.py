# -*- coding: utf-8 -*-

PI = 3.14159


def main():
    radius = float(input())
    volume = (4.0/3) * PI * (radius ** 3)
    print(f'VOLUME = {volume:.3f}')


if __name__ == "__main__":
    main()
