import numpy as np

# function [result] = aes_shift_rows(input_data, encrypt)

#  performs the AES ShiftRows Transformation
# 
#  DESCRIPTION:
# 
#  aes_shift_row(input_data,encrypt)
#  
#  performs a shiftrow operation on each line of the matrix 'input_data'.
#  If encrypt=0, the inverse operation is performed - else the normal shiftrow operation.
# 
#  PARAMETERS:
# 
#  - input_data:
#    A matrix of bytes with an arbitrary number of lines. Each line consists of 16 bytes that
#    represent a 128-bit state.
#  - encrypt:
#    if encrypt=0, the inverse operation is performed - else the normal shiftrow operation.
# 
#  RETURNVALUES:
# 
#  - result:
#    A matrix of bytes with the same size as 'input_data'. Each line of the return value is the result of the
#    shiftrow operation applied to the corresponding line of the 'input_data' matrix.
# 
#  EXAMPLE:
# 
#  ShiftRows([1, 2,3 ,4, 5, 6 ,7 ,8, 1, 2,3 ,4, 5, 6 ,7 ,8] , 1)

#  AUTHORS: Stefan Mangard, Mario Kirschbaum
# 
#  CREATION_DATE: 31 July 2001
#  LAST_REVISION: 27 October 2008


def aes_shift_rows(input_data, encrypt):
	
	result = np.copy(input_data)

	#  first 4 bytes stay where they are
	#  third 4 bytes
	result[:,  2] = input_data[:, 10]
	result[:,  6] = input_data[:, 14]
	result[:, 10] = input_data[:,  2]
	result[:, 14] = input_data[:,  6]

	if encrypt == 0:
	
		#  second 4 bytes
		result[:, 1] = input_data[:, 13]
		result[:, 5] = input_data[:, 1]
		result[:, 9] = input_data[:, 5]
		result[:, 13] = input_data[:, 9]
	
		#  fourth 4 bytes
		result[:,  3] = input_data[:,  7]
		result[:,  7] = input_data[:, 11]
		result[:, 11] = input_data[:, 15]
		result[:, 15] = input_data[:,  3]
	
	else:
	
		#  second 4 bytes
		result[:, 1] = input_data[:, 5]
		result[:, 5] = input_data[:, 9]
		result[:, 9] = input_data[:, 13]
		result[:, 13] = input_data[:, 1]

		#  fourth 4 bytes
		result[:, 3] = input_data[:, 15]
		result[:, 7] = input_data[:, 3]
		result[:, 11] = input_data[:, 7]
		result[:, 15] = input_data[:, 11]

	return result
