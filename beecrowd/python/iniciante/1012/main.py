# -*- coding: utf-8 -*-

PI = 3.14159


def main():
    a, b, c = input().split(' ')
    a, b, c = float(a), float(b), float(c)
    triangulor = (a * c) / 2
    circ = PI * c ** 2
    trap = ((a + b) * c) / 2
    quadr = b ** 2
    retan = a * b
    print(f'TRIANGULO: {triangulor:.3f}')
    print(f'CIRCULO: {circ:.3f}')
    print(f'TRAPEZIO: {trap:.3f}')
    print(f'QUADRADO: {quadr:.3f}')
    print(f'RETANGULO: {retan:.3f}')


if __name__ == "__main__":
    main()
