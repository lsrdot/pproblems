# -*- coding: utf-8 -*-


def main():
    code1, n1, value1 = input().split(' ')
    code2, n2, value2 = input().split(' ')
    code1, n1, value1 = int(code1), int(n1), float(value1)
    code2, n2, value2 = int(code2), int(n2), float(value2)
    total = (n1 * value1) + (n2 * value2)
    print(f'VALOR A PAGAR: R$ {total:.2f}')


if __name__ == "__main__":
    main()
