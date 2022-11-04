# -*- coding: utf-8 -*-


def main():
    workern = int(input())
    nhours = int(input())
    salaryph = float(input())
    salary = nhours * salaryph
    print(f'NUMBER = {workern}\nSALARY = U$ {salary:.2f}')


if __name__ == "__main__":
    main()
