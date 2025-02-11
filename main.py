import numpy as np

from sed.string_edit_distance import StringEditDistance


def main():
    string1 = 'ABABBB'
    string2 = 'BABAAA'

    n, m = len(string1), len(string2)

    sed = StringEditDistance(string1, string2)

    D = sed.init_cost_matrix()
    P = sed.init_pointer_matrix()

    sed.calc_sed(D, P)

    print('Cost Matrix D: ')
    print(D)
    print('\nPointer Matrix P: ')
    for row in P:
        print(" ".join(row))


if __name__ == '__main__':
    main()