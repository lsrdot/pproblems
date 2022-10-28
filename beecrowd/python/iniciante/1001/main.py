

# -*- coding: utf-8 -*-


def main():
    a, b, x = input(), input(), 0
    if a.lstrip('-').isdigit() and b.lstrip('-').isdigit():
        a = int(a)
        b = int(b)
    x = a + b
    print(f'X = {x}')


if __name__ == "__main__":
    main()
