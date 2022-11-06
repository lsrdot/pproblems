# -*- coding: utf-8 -*-


def main():
    n = int(input())
    print(n)
    print(f'{int(n / 100)} nota(s) de R$ 100,00')
    aux = (n % 100)
    print(f'{int(aux / 50)} nota(s) de R$ 50,00')
    aux = (aux % 50)
    print(f'{int(aux / 20)} nota(s) de R$ 20,00')
    aux = (aux % 20)
    print(f'{int(aux / 10)} nota(s) de R$ 10,00')
    aux = (aux % 10)
    print(f'{int(aux / 5)} nota(s) de R$ 5,00')
    aux = (aux % 5)
    print(f'{int(aux / 2)} nota(s) de R$ 2,00')
    aux = (aux % 2)
    print(f'{int(aux / 1)} nota(s) de R$ 1,00')

    # Sol. not working. TODO Try to fix it
    # n = int(input())
    # hundbill = 0
    # fiftybill = 0
    # twentbill = 0
    # tenbill = 0
    # fivebill = 0
    # twobill = 0
    # onebill = 0
    # while n:
    #     if n - 100 >= 0:
    #         n -= 100
    #         hundbill += 1
    #     elif n - 50 >= 0:
    #         n -= 50
    #         fiftybill += 1
    #     elif n - 20 >= 0:
    #         n -= 20
    #         twentbill += 1
    #     elif n - 10 >= 0:
    #         n -= 10
    #         tenbill += 1
    #     elif n - 5 >= 0:
    #         n -= 5
    #         fivebill += 1
    #     elif n - 2 >= 0:
    #         n -= 2
    #         twobill += 1
    #     elif n - 1 >= 0:
    #         n -= 1
    #         onebill += 1
    #     else:
    #         break
    #
    # print(f'{hundbill} nota(s) de R$ 100,00')
    # print(f'{fiftybill} nota(s) de R$ 50,00')
    # print(f'{twentbill} nota(s) de R$ 20,00')
    # print(f'{tenbill} nota(s) de R$ 10,00')
    # print(f'{fivebill} nota(s) de R$ 5,00')
    # print(f'{twobill} nota(s) de R$ 2,00')
    # print(f'{onebill} nota(s) de R$ 1,00')

    # Sol. not working. TODO Try to fix it 2
    # n = int(input())
    # print(f'{n // 100} nota(s) de R$ 100,00')
    # aux = n % 100
    # print(f'{aux // 50} nota(s) de R$ 50,00')
    # aux %= 50
    # print(f'{aux // 20} nota(s) de R$ 20,00')
    # aux %= 20
    # print(f'{aux // 10} nota(s) de R$ 10,00')
    # aux %= 10
    # print(f'{aux // 5} nota(s) de R$ 5,00')
    # aux %= 5
    # print(f'{aux // 2} nota(s) de R$ 2,00')
    # aux %= 2
    # print(f'{aux // 1} nota(s) de R$ 1,00')


if __name__ == "__main__":
    main()
