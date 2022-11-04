# -*- coding: utf-8 -*-


def main():
    name = input()
    prebonus = float(input())
    sales = float(input())
    posbonus = prebonus + (sales * .15)
    print(f'TOTAL = R$ {posbonus:.2f}')


if __name__ == "__main__":
    main()
