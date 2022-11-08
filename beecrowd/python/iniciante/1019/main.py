# -*- coding: utf-8 -*-


def main():
    n = int(input())
    horas = n // 3600
    minutos = ((n % 3600) // 60)
    segundos = n % 60
    print(f'{horas}:{minutos}:{segundos}')


if __name__ == '__main__':
    main()
