# -*- coding: utf-8 -*-

# Don't know why isn't working:
# PESOS = (2, 3, 5)
#
#
# def main():
#     a, b, c = input(), input(), input()
#     if isfloat(a, b, c):
#         if (float(a) and float(b) and float(c) <= 10.0) and (float(a) and float(b) and float(c) >= 0):
#             a, b, c = float(a) * PESOS[0], float(b) * PESOS[1], float(c) * PESOS[2]
#             media = (a + b + c) / (PESOS[0] + PESOS[1] + PESOS[2])
#             print(f'MEDIA = {media:.1f}')
#
#
# def isfloat(*n):
#     try:
#         for x in n:
#             float(x)
#         return True
#     except ValueError:
#         return False
#
#
# if __name__ == "__main__":
#     main()


a = float(input())
b = float(input())
c = float(input())
pesos = 10

media = (a / pesos * 2) + (b / pesos * 3) + (c / pesos * 5)

print(f'MEDIA = {media:.1f}')
