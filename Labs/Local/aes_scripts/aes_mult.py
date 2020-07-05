import numpy as np
from aes_scripts.aes_xtimes import aes_xtimes
# function [result] = aes_mult(input_data, constant)

#  helper function for the AES Mixcolums transformation
# 
#  DESCRIPTION:
# 
#  aes_mult(input_data, constant)
#  
#  multiplies each byte of the matrix 'input_data' with the
#  value 'constant'. This multiplication is performed in GF(2^8) modulo the irreducible
#  polynomial used for the AES.
# 
#  PARAMETERS:
# 
#  - data: A matrix of bytes
#  - constant: A scalar value
# 
#  RETURNVALUES:
# 
#  - result:
#  A matrix of the size of 'input_data', where each byte is the product of 'constant' and
#  the corresponding byte of 'input_data'.
# 
#  EXAMPLE:
# 
#  aes_mult([1, 2,3 ,4; 5, 6 ,7 ,8], 3)

#  AUTHORS: Stefan Mangard, Mario Kirschbaum
# 
#  CREATION_DATE: 31 July 2001
#  LAST_REVISION: 27 October 2008


def aes_mult(input_data, constant):
	result = 0

	mult_val = np.copy(input_data)

	#  maximum constant is 15
	for i in range(4):

		if (constant >> i) & 1:
			result = np.bitwise_xor(result, mult_val)

		mult_val = aes_xtimes(mult_val)
	return result
