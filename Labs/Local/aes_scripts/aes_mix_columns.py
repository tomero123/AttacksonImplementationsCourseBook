import numpy as np
import math
from aes_scripts.aes_mult import aes_mult

# function result = aes_mix_columns(input_data, encrypt)

# performs the AES MixColumns transformation
#
# DESCRIPTION:
#
# aes_mix_columns(input_data, encrypt)
#
# This function performs an AES MixColumns operation on each line of the
# byte matrix 'input_data'. 'input_data' is a matrix of bytes with an
# arbitrary number of lines that are four bytes wide (or a width that is a
# multiple of four bytes - in this case the MixColumns operation is
# performed on the bytes 1..4, 5..8, 8..12, ... ).
#
# PARAMETERS:
#
# - input_data:
#   A matrix of bytes with an arbitrary number of lines and a number of
#   columns that is a multiple of 4.
# - encrypt:
#   Paramter indicating whether an encryption or a decryption is performed
#   (1 = encryption, 0 = decryption). In case of a decrytion, an inverse
#   MixColumns operation is performed.
#
# RETURNVALUES:
#
# - result:
#   A matrix of bytes of the size of the 'data' matrix. Each line of this
#   matrix consists of the mixcolumn result of the corresponding line of
#   'input_data'.
#
# EXAMPLE:
#
# aes_mix_columns([1, 2, 3, 4; 5, 6, 7 ,8], 1)

# AUTHORS: Stefan Mangard, Mario Kirschbaum
#
# CREATION_DATE: 31 July 2001
# LAST_REVISION: 30 June 2009


def aes_mix_columns(input_data, encrypt):
	n = np.shape(input_data)[1]

	times = math.ceil(n / 4)

	data = np.double(input_data)

	result = np.copy(data)

	for i in range(0, times):

		if encrypt == 0:
			# inverse mixcolumn
			result[:, 1+4*i] = np.bitwise_xor(np.bitwise_xor(np.bitwise_xor(aes_mult(data[:, 1+4*i], 14), aes_mult(data[:, 2+4*i], 11)), aes_mult(data[:, 3+4*i], 13)), aes_mult(data[:, 4+4*i], 9))
			result[:, 2+4*i] = np.bitwise_xor(np.bitwise_xor(np.bitwise_xor(aes_mult(data[:, 1+4*i],  9), aes_mult(data[:, 2+4*i], 14)), aes_mult(data[:, 3+4*i], 11)), aes_mult(data[:, 4+4*i], 13))
			result[:, 3+4*i] = np.bitwise_xor(np.bitwise_xor(np.bitwise_xor(aes_mult(data[:, 1+4*i], 13), aes_mult(data[:, 2+4*i], 9)), aes_mult(data[:, 3+4*i], 14)), aes_mult(data[:, 4+4*i], 11))
			result[:, 4+4*i] = np.bitwise_xor(np.bitwise_xor(np.bitwise_xor(aes_mult(data[:, 1+4*i], 11), aes_mult(data[:, 2+4*i], 13)), aes_mult(data[:, 3+4*i], 9)), aes_mult(data[:, 4+4*i], 14))

		else:
			# mixcolumn
			result[:, 1+4*i] = np.bitwise_xor(np.bitwise_xor(np.bitwise_xor(aes_mult(data[:, 1+4*i], 2), aes_mult(data[:, 2+4*i], 3)), data[:, 3+4*i]), data[:, 4+4*i])
			result[:, 2+4*i] = np.bitwise_xor(np.bitwise_xor(np.bitwise_xor(data[:, 1+4*i], aes_mult(data[:, 2+4*i], 2)), aes_mult(data[:, 3+4*i], 3)), data[:, 4+4*i])
			result[:, 3+4*i] = np.bitwise_xor(np.bitwise_xor(np.bitwise_xor(data[:, 1+4*i], data[:, 2+4*i]), aes_mult(data[:, 3+4*i], 2)), aes_mult(data[:, 4+4*i], 3))
			result[:, 4+4*i] = np.bitwise_xor(np.bitwise_xor(np.bitwise_xor(aes_mult(data[:, 1+4*i], 3), data[:, 2+4*i]), data[:, 3+4*i]), aes_mult(data[:, 4+4*i], 2))

	result = np.uint8(result)
	return result
