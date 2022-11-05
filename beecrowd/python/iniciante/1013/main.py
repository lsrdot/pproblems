# -*- coding: utf-8 -*-


def main():
    x, y, z = input().split(' ')
    x, y, z = int(x), int(y), int(z)
    print(f'{max(x, y, z)} eh o maior')


# Works 2, but lets just use the built-in py function:
# def get_max(*args):
#     aux = 0
#     for i in args:
#         if i > aux:
#             aux = i
#     return aux


if __name__ == "__main__":
    main()
