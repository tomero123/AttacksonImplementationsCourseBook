import numpy as np

# performs the AES AddRoundKey transformation
#
# DESCRIPTION:
#
# aes_add_round_key(key, data)

# xors each line of the byte matrix 'data' with
# the byte vector 'key'. So, each byte  of the first column of the matrix
# 'data' is xored with the first byte of the vector 'key'. Each byte of the
# second column of 'data' is xored with the second byte of 'key' and so on.
# The number of bytes per line in the matrix 'data' and
# the number of bytes of 'key' need to be the same for this operation.
#
# PARAMETERS:
#
# - key:
#   A vector of bytes that represents the key input of this operation.
# - data:
#   A matrix of bytes. Each line of this matrix represents one data input
#   to the add_roundkey operations as specified in FIPS 197. So, the number
#   of bytes per line can either be 16 (AES-128), 24 (AES-192) or 32 (AES-256).
#
# RETURNVALUES:
#
# - result:
# A matrix of the size of data. Each line of this matrix contains
# the result of the XOR operation of the key and the corresponding
# line of the data input.
#
# EXAMPLE:
#
# aes_add_round_key( [123,200], [100,23; 156,21] )

# AUTHORS: Stefan Mangard, Mario Kirschbaum
#
# CREATION_DATE: 31 July 2001
# LAST_REVISION: 27 October 2008


def aes_add_round_key(key, data):
	key_len = np.shape(key)[1]

	result = np.uint8(np.zeros(np.size(data)))
	key = np.asmatrix(key)
	# do add_roundkey column by colomn
	for i in range(key_len):
		# print(key[0, i], data[0, i])
		result[i] = np.bitwise_xor(key[0, i], data[0, i])
	return np.asmatrix(result)
