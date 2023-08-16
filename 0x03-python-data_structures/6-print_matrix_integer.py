#!/usr/bin/python3



def print_matrix_integer(matrix=[[]]):
for m  in matrix:
	for i  in m:
		print("{5:3d".format(i), end ='')
	print()
	if not matrix:
		return 
