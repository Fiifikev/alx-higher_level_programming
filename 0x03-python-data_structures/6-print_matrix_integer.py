#!/usr/python3

def print_matrix_integer(matrix=[[]]):
        for eachrow in matrix:
            for eachcol in eachrow:
                print("{:d}".format(eachcol),
                    end=" " if eachcol != eachrow[-1] else "")
            print()
