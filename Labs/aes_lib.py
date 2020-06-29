import numpy as np
import math

# function [result] = aes_xtimes(input_data)

#  helper function for the AES key expansion
# 
#  DESCRIPTION:
# 
#  aes_xtimes(input_data)
#  
#  multiplies each byte of 'input_data' with two the GF(2^8) as it is used
#  for the AES.
# 
#  PARAMETERS:
# 
#  - input_data:
#    A matrix of bytes
# 
#  RETURNVALUES:
# 
#  - result:
#    A matrix of bytes with the same size as input_data. Each byte in this matrix is the
#    result of the multiplication of the corresponding byte of 'input_data' with 2.
# 
#  EXAMPLE:
# 
#  aes_xtime([1, 2,3 ,4 5, 6 ,7 ,8])

#  AUTHORS: Stefan Mangard, Mario Kirschbaum
# 
#  CREATION_DATE: 31 July 2001
#  LAST_REVISION: 27 October 2008


def bitset(num, index, value):
	return num | ((1 << index) * value)


def bitget(num, index):
	return (num >> index) & 1


def aes_xtimes(input_data):

	result = 0

	result = bitset(result, 0, bitget(input_data, 7))
	result = bitset(result, 1, np.bitwise_xor(bitget(input_data, 0), bitget(input_data, 7)))
	result = bitset(result, 2, bitget(input_data, 1))
	result = bitset(result, 3, np.bitwise_xor(bitget(input_data, 2), bitget(input_data, 7)))
	result = bitset(result, 4, np.bitwise_xor(bitget(input_data, 3), bitget(input_data, 7)))
	result = bitset(result, 5, bitget(input_data, 4))
	result = bitset(result, 6, bitget(input_data, 5))
	result = bitset(result, 7, bitget(input_data, 6))

	return result

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

# function result = aes_sbox(input_data, encrypt)

#  performs the AES S-Box operation on each element of a byte matrix
# 
#  DESCRIPTION:
# 
#  aes_sbox(input_data,encrypt)
#  
#  performs an AES Sbox operation on each byte of the byte
#  matrix 'input_data'. If encrypt=0 an inverse Sbox operation is
#  performed. If encrypt=1 an Sbox operation is performed.
# 
#  PARAMETERS:
# 
#  - data   : A matrix of bytes that are SBOXed.
#  - encrypt: Paramter indicating whether an encryption or a decryption is performed
# 			    (1=encryption, 0=decryption) In the case of a decryption, the inverse ByteSub
#             operation is performed.
# 
#  RETURNVALUES:
# 
#  - result:
#    A matrix of the size of 'input_data'. Each byte of this matrix is the output of the
#    ByteSub operation calculated based on the corresponding input byte of the 'input_data' matrix.
# 
#  EXAMPLE:
# 
#  aes_sbox([1,2; 3,4],1)

#  AUTHORS: Stefan Mangard, Mario Kirschbaum, Thomas Plos
# 
#  CREATION_DATE: 31 July 2001
#  LAST_REVISION: 10 March 2009

#  the sbox and inverse sbox tables


def aes_sbox(input_data, encrypt):

	original_sbox = np.uint8([
		99,  124, 119, 123, 242, 107, 111, 197,
		48,    1, 103,  43, 254, 215, 171, 118,
		202, 130, 201, 125, 250,  89,  71, 240,
		173, 212, 162, 175, 156, 164, 114, 192,
		183, 253, 147,  38,  54,  63, 247, 204,
		52,  165, 229, 241, 113, 216,  49,  21,
		4,   199,  35, 195,  24, 150,   5, 154,
		7,    18, 128, 226, 235,  39, 178, 117,
		9,   131,  44,  26,  27, 110,  90, 160,
		82,   59, 214, 179,  41, 227,  47, 132,
		83,  209,   0, 237,  32, 252, 177,  91,
		106, 203, 190,  57,  74,  76,  88, 207,
		208, 239, 170, 251,  67,  77,  51, 133,
		69,  249,   2, 127,  80,  60, 159, 168,
		81,  163,  64, 143, 146, 157,  56, 245,
		188, 182, 218,  33,  16, 255, 243, 210,
		205,  12,  19, 236,  95, 151,  68,  23,
		196, 167, 126,  61, 100,  93,  25, 115,
		96,  129,  79, 220,  34,  42, 144, 136,
		70,  238, 184,  20, 222,  94,  11, 219,
		224,  50,  58,  10,  73,   6,  36,  92,
		194, 211, 172,  98, 145, 149, 228, 121,
		231, 200,  55, 109, 141, 213,  78, 169,
		108,  86, 244, 234, 101, 122, 174,   8,
		186, 120,  37,  46,  28, 166, 180, 198,
		232, 221, 116,  31,  75, 189, 139, 138,
		112,  62, 181, 102,  72,   3, 246,  14,
		97,   53,  87, 185, 134, 193,  29, 158,
		225, 248, 152,  17, 105, 217, 142, 148,
		155,  30, 135, 233, 206,  85,  40, 223,
		140, 161, 137,  13, 191, 230,  66, 104,
		65,  153,  45,  15, 176,  84, 187, 22])

	# original_sbox = original_sbox';

	inv_sbox = np.uint8([
		82,   9, 106, 213,  48,  54, 165,  56,
		191,  64, 163, 158, 129, 243, 215, 251,
		124, 227,  57, 130, 155,  47, 255, 135,
		52, 142,  67,  68, 196, 222, 233, 203,
		84, 123, 148,  50, 166, 194,  35,  61,
		238,  76, 149,  11,  66, 250, 195,  78,
		8,  46, 161, 102,  40, 217,  36, 178,
		118,  91, 162,  73, 109, 139, 209,  37,
		114, 248, 246, 100, 134, 104, 152,  22,
		212, 164,  92, 204,  93, 101, 182, 146,
		108, 112,  72,  80, 253, 237, 185, 218,
		94,  21,  70,  87, 167, 141, 157, 132,
		144, 216, 171,   0, 140, 188, 211,  10,
		247, 228,  88,   5, 184, 179,  69,   6,
		208,  44,  30, 143, 202,  63,  15,   2,
		193, 175, 189,   3,   1,  19, 138, 107,
		58, 145,  17,  65,  79, 103, 220, 234,
		151, 242, 207, 206, 240, 180, 230, 115,
		150, 172, 116,  34, 231, 173,  53, 133,
		226, 249,  55, 232,  28, 117, 223, 110,
		71, 241,  26, 113,  29,  41, 197, 137,
		111, 183,  98,  14, 170,  24, 190,  27,
		252,  86,  62,  75, 198, 210, 121,  32,
		154, 219, 192, 254, 120, 205,  90, 244,
		31, 221, 168,  51, 136,   7, 199,  49,
		177,  18,  16,  89,  39, 128, 236,  95,
		96,  81, 127, 169,  25, 181,  74,  13,
		45, 229, 122, 159, 147, 201, 156, 239,
		160, 224,  59,  77, 174,  42, 245, 176,
		200, 235, 187,  60, 131,  83, 153,  97,
		23,  43,   4, 126, 186, 119, 214,  38,
		225, 105,  20,  99,  85,  33,  12, 125])

	# inv_sbox = inv_sbox';

	if encrypt == 0:

		result = inv_sbox[np.array(input_data)]

	else:

		result = original_sbox[np.array(input_data)]

	# if np.shape(input_data)[0] == 1:
		# return result
		# result = np.transpose(result)
	return result

# function [result] = aes_round_key(key, round)

#  calculates the round key for a given round based on a 128-bit secret key
# 
#  DESCRIPTION:
# 
#  aes_round_key(key, round)
#  
#  calculates the round key of round 'round' based on the
#  secret key 'key'. The current implementation only works for keys with 128 bits.
# 
#  PARAMETERS:
# 
#  - key: A vector of 16 bytes representing the secret key.
#  - round: The number of the round key that is calculated
# 
#  RETURNVALUES:
# 
#  - result:
#    A vector of 16 bytes that represent the round key of round 'round'.
# 
#  EXAMPLE:
# 
#  aes_round_key([1, 2,3 ,4, 5, 6 ,7 ,8, 1, 2,3 ,4, 5, 6 ,7 ,8],1)

#  AUTHORS: Stefan Mangard, Mario Kirschbaum
# 
#  CREATION_DATE: 31 July 2001
#  LAST_REVISION: 27 October 2008


def aes_round_key(key, round):
	rcon = 1

	result = np.copy(key)
	next = np.copy(key)
	for i in range(round + 1):
		next[0, 0:4] = aes_sbox([result[0, 13], result[0, 14], result[0, 15], result[0, 12]], 1)
		next[0, 0:4] = np.bitwise_xor(next[0, 0:4], result[0, 0:4])
		next[0, 0] = np.bitwise_xor(next[0, 0], rcon)

		next[0, 4:8] = np.bitwise_xor(next[0, 0: 4], result[0, 4: 8])
		next[0, 8:12] = np.bitwise_xor(next[0, 4: 8], result[0, 8:12])
		next[0, 12:16] = np.bitwise_xor(next[0, 8:12], result[0, 12:16])

		result = np.copy(next)
		rcon = aes_xtimes(rcon)
	
	return result

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

# function result = aes_mix_columns_8bit(input_data, encrypt)

# performs the AES MixColumns transformation like a 8-bit uC would
# 
# DESCRIPTION:
# 
# aes_mix_columns_8bit(input_data, encrypt)
# 
# This function performs an AES MixColumns operation on each line of the
# byte matrix 'input_data'. 'input_data' is a matrix of bytes with an
# arbitrary number of lines that are four bytes wide (or a width that is a
# multiple of four bytes - in this case the MixColumns operation is
# performed on the bytes 1..4, 5..8, 8..12,  ).
# 
# PARAMETERS:
# 
# - input_data:
#   A matrix of bytes with an arbitrary number of lines and a number of
#   :s that is a multiple of 4.
# - encrypt:
#   Paramter indicating whether an encryption or a decryption is performed
#   (1 = encryption, 0 = decryption). In case of a decrytion, an inverse
#   Mix:s operation is performed.
# 
# RETURNVALUES:
# 
# - result:
#   A matrix of bytes of the size of the 'data' matrix. Each line of this
#   matrix consists of the MixColumns result of the corresponding line of
#   'input_data'.
# 
# EXAMPLE:
# 
# aes_mix_columns_8bit([1, 2, 3, 4 5, 6, 7 ,8], 1)

# AUTHORS: Stefan Mangard, Mario Kirschbaum, Yossi Oren
# 
# CREATION_DATE: 31 July 2001
# LAST_REVISION: 30 June 2009


def aes_mix_columns_8bit(input_data, encrypt):
	n = np.shape(input_data)[1]

	times = math.ceil(n / 4)

	data = np.asmatrix(input_data)

	result = np.copy(data)

	for i in range(times):

		if encrypt == 0:
			# inverse mixcolumns  - 8 bit implementation
			tmp = np.bitwise_xor(np.bitwise_xor(np.bitwise_xor( 
				data[:, 0+4*i], data[:, 1+4*i]),
				data[:, 2+4*i]), data[:, 3+4*i])         # Leak #0.1
			xtmp = aes_xtimes(tmp)                             # Leak #0.2
			h1 = np.bitwise_xor(np.bitwise_xor(
				xtmp, data[:, 0+4*i]), data[:, 2+4*i])   # Leak #0.3
			h1 = aes_xtimes(h1)                                # Leak #0.4
			h1 = aes_xtimes(h1)                                # Leak #0.5
			h1 = np.bitwise_xor(h1, tmp)                               # Leak #0.6
			h2 = np.bitwise_xor(np.bitwise_xor(
				xtmp, data[:, 1+4*i]), data[:, 3+4*i])   # Leak #0.7
			h2 = aes_xtimes(h2)                                # Leak #0.8
			h2 = aes_xtimes(h2)                                # Leak #0.9
			h2 = np.bitwise_xor(h2, tmp)                               # Leak #0.10

			tm = np.bitwise_xor(data[:, 0+4*i], data[:, 1+4*i])    # Leak #1.1
			tm = aes_xtimes(tm)                                  # Leak #1.2
			result[:, 0+4*i] = np.bitwise_xor(np.bitwise_xor(
				data[:, 0+4*i], tm), h1)                    # (output)

			tm = np.bitwise_xor(data[:, 1+4*i], data[:, 2+4*i])    # Leak #2.1
			tm = aes_xtimes(tm)                                  # Leak #2.2
			result[:, 1+4*i] = np.bitwise_xor(np.bitwise_xor(
				data[:, 1+4*i], tm), h2)

			tm = np.bitwise_xor(data[:, 2+4*i], data[:, 3+4*i])    # Leak #3.1
			tm = aes_xtimes(tm)                                  # Leak #3.2
			result[:, 2+4*i] = np.bitwise_xor(np.bitwise_xor(
				data[:, 2+4*i], tm), h1)                    # (output)

			tm = np.bitwise_xor(data[:, 3+4*i], data[:, 0+4*i])    # Leak #4.1
			tm = aes_xtimes(tm)                                  # Leak #4.2
			result[:, 3+4*i] = np.bitwise_xor(np.bitwise_xor(
				data[:, 3+4*i], tm), h2)                    # (output)
			# Total 18 extra leaks per column
		else:
			# mixcolumns  - 8 bit implementation
			tmp = np.bitwise_xor(np.bitwise_xor(np.bitwise_xor(
				data[:, 0+4*i], data[:, 1+4*i]),
				data[:, 2+4*i]), data[:, 3+4*i])         # Leak #0.1
			tm = np.bitwise_xor(data[:, 0+4*i], data[:, 1+4*i])    # Leak #1.1
			tm = aes_xtimes(tm)                                  # Leak #1.2
			result[:, 0+4*i] = np.bitwise_xor(np.bitwise_xor(
				data[:, 0+4*i], tm), tmp)                   # (output)

			tm = np.bitwise_xor(data[:, 1+4*i], data[:, 2+4*i])    # Leak #2.1
			tm = aes_xtimes(tm)                                  # Leak #2.2
			result[:, 1+4*i] = np.bitwise_xor(np.bitwise_xor(
				data[:, 1+4*i], tm), tmp)                   # (output)

			tm = np.bitwise_xor(data[:, 2+4*i], data[:, 3+4*i])    # Leak #3.1
			tm = aes_xtimes(tm)                                  # Leak #3.2
			result[:, 2+4*i] = np.bitwise_xor(np.bitwise_xor(
				data[:, 2+4*i], tm), tmp)                   # (output)

			tm = np.bitwise_xor(data[:, 3+4*i], data[:, 0+4*i])    # Leak #4.1
			tm = aes_xtimes(tm)                                  # Leak #4.2
			result[:, 3+4*i] = np.bitwise_xor(np.bitwise_xor(               # (output)
				data[:, 3+4*i], tm), tmp)
		# Total 9 extra leaks per column

	result = np.uint8(result)
	return result

# function [result leak]= aes_mix_columns_8bit_and_leak(input_data, encrypt)

#  performs the AES MixColumns transformation like a 8-bit uC would, leaking
#  the intermediate results for the purpose of SCA
# 
#  DESCRIPTION:
# 
#  aes_mix_columns_8bit(input_data, encrypt)
# 
#  This function performs an AES MixColumns operation on each line of the
#  byte matrix 'input_data'. 'input_data' is a matrix of bytes with an
#  arbitrary number of lines that are four bytes wide (or a width that is a
#  multiple of four bytes - in this case the MixColumns operation is
#  performed on the bytes 1..4, 5..8, 8..12,  ).
# 
#  PARAMETERS:
# 
#  - input_data:
#    A matrix of bytes with an arbitrary number of lines and a number of
#    columns that is a multiple of 4.
#  - encrypt:
#    Paramter indicating whether an encryption or a decryption is performed
#    (1 = encryption, 0 = decryption). In case of a decrytion, an inverse
#    Mix:s operation is performed.
# 
#  RETURNVALUES:
# 
#  - result:
#    A matrix of bytes of the size of the 'data' matrix. Each line of this
#    matrix consists of the MixColumns result of the corresponding line of
#    'input_data'.
#  - leak:
#    The leaked intermediate results of the MixColumns operation
#    Size is #lines x #cols x 9 for encryption, #lines x #cols x 18 for decryption
# 
#  EXAMPLE:
# 
#  aes_mix_columns_8bit([1, 2, 3, 4 5, 6, 7 ,8], 1)

#  AUTHORS: Stefan Mangard, Mario Kirschbaum, Yossi Oren
# 
#  CREATION_DATE: 31 July 2001
#  LAST_REVISION: 30 June 2009


def aes_mix_columns_8bit_and_leak(input_data, encrypt):

	n = np.shape(input_data)[1]

	times = math.ceil(n / 4)

	data = np.copy(input_data)

	result = np.copy(data)
	if encrypt == 0:  # decryption
		leak = np.zeros([times, np.shape(input_data)[0], 18])
	else:  # encryption
		leak = np.zeros([times, np.shape(input_data)[0], 9])

	for i in range(times):

		if encrypt == 0:
			#  inverse mixcolumns - 8 bit implementation
			tmp = np.bitwise_xor(np.bitwise_xor(np.bitwise_xor(
			data[:, 0 + 4 * i], data[:, 1 + 4 * i]),
			data[:, 2 + 4 * i]), data[:, 3 + 4 * i])  # Leak  # 0.1
			leak[i + 0, :, 0] = tmp

			xtmp = aes_xtimes(tmp)  # Leak  # 0.2
			leak[i + 0, :, 1] = xtmp

			h1 = np.bitwise_xor(np.bitwise_xor(
			xtmp, data[:, 0 + 4 * i]), data[:, 2 + 4 * i])  # Leak  # 0.3
			leak[i + 0, :, 2] = h1

			h1 = aes_xtimes(h1)  # Leak  # 0.4
			leak[i + 0, :, 3] = h1

			h1 = aes_xtimes(h1)  # Leak  # 0.5
			leak[i + 0, :, 4] = h1

			h1 = np.bitwise_xor(h1, tmp)  # Leak  # 0.6
			leak[i + 0, :, 5] = h1

			h2 = np.bitwise_xor(np.bitwise_xor(
			xtmp, data[:, 1 + 4 * i]), data[:, 3 + 4 * i])  # Leak  # 0.7
			leak[i + 0, :, 6] = h2

			h2 = aes_xtimes(h2)  # Leak  # 0.8
			leak[i + 0, :, 7] = h2

			h2 = aes_xtimes(h2)  # Leak  # 0.9
			leak[i + 0, :, 8] = h2

			h2 = np.bitwise_xor(h2, tmp)  # Leak  # 0.10
			leak[i + 0, :, 9] = h2

			tm = np.bitwise_xor(data[:, 0 + 4 * i], data[:, 1 + 4 * i])  # Leak  # 1.1
			leak[i + 0, :, 10] = tm

			tm = aes_xtimes(tm)  # Leak  # 1.2
			leak[i + 0, :, 11] = tm

			result[:, 0 + 4 * i] = np.bitwise_xor(np.bitwise_xor(
			data[:, 0 + 4 * i], tm), h1)  # (output)

			tm = np.bitwise_xor(data[:, 1 + 4 * i], data[:, 2 + 4 * i])  # Leak  # 2.1
			leak[i + 0, :, 12] = tm

			tm = aes_xtimes(tm)  # Leak  # 2.2
			leak[i + 0, :, 13] = tm

			result[:, 1 + 4 * i] = np.bitwise_xor(np.bitwise_xor(  # (output)
			data[:, 1 + 4 * i], tm), h2)

			tm = np.bitwise_xor(data[:, 2 + 4 * i], data[:, 3 + 4 * i])  # Leak  # 3.1
			leak[i + 0, :, 14] = tm

			tm = aes_xtimes(tm)  # Leak  # 3.2
			leak[i + 0, :, 15] = tm

			result[:, 2 + 4 * i] = np.bitwise_xor(np.bitwise_xor(
			data[:, 2 + 4 * i], tm), h1)  # (output)

			tm = np.bitwise_xor(data[:, 3 + 4 * i], data[:, 0 + 4 * i])  # Leak  # 4.1
			leak[i + 0, :, 16] = tm

			tm = aes_xtimes(tm)  # Leak  # 4.2
			leak[i + 0, :, 17] = tm

			result[:, 3 + 4 * i] = np.bitwise_xor(np.bitwise_xor(data[:, 3 + 4 * i], tm), h2)  # (output)
			#  Total 18 extra leaks per column
		else:
			#  mixcolumns - 8 bit implementation
			tmp = np.bitwise_xor(np.bitwise_xor(np.bitwise_xor(
			data[:, 0 + 4 * i], data[:, 1 + 4 * i]),
			data[:, 2 + 4 * i]), data[:, 3 + 4 * i])  # Leak  # 0.1
			leak[i + 0, :, 0] = tmp[0]

			tm = np.bitwise_xor(data[:, 0 + 4 * i], data[:, 1 + 4 * i])  # Leak  # 1.1
			leak[i + 0, :, 1] = tm

			tm = aes_xtimes(tm)  # Leak  # 1.2
			leak[i + 0, :, 2] = tm

			result[:, 0 + 4 * i] = np.bitwise_xor(np.bitwise_xor(
			data[:, 0 + 4 * i], tm), tmp)  # (output)

			tm = np.bitwise_xor(data[:, 1 + 4 * i], data[:, 2 + 4 * i])  # Leak  # 2.1
			leak[i + 0, :, 3] = tm

			tm = aes_xtimes(tm)  # Leak  # 2.2
			leak[i + 0, :, 4] = tm

			result[:, 1 + 4 * i] = np.bitwise_xor(np.bitwise_xor(
			data[:, 1 + 4 * i], tm), tmp)  # (output)

			tm = np.bitwise_xor(data[:, 2 + 4 * i], data[:, 3 + 4 * i])  # Leak  # 3.1
			leak[i + 0, :, 5] = tm

			tm = aes_xtimes(tm)  # Leak  # 3.2
			leak[i + 0, :, 6] = tm

			result[:, 2 + 4 * i] = np.bitwise_xor(np.bitwise_xor(
			data[:, 2 + 4 * i], tm), tmp)  # (output)

			tm = np.bitwise_xor(data[:, 3 + 4 * i], data[:, 0 + 4 * i])  # Leak  # 4.1
			leak[i + 0, :, 7] = tm

			tm = aes_xtimes(tm)  # Leak  # 4.2
			leak[i + 0, :, 8] = tm

			result[:, 3 + 4 * i] = np.bitwise_xor(np.bitwise_xor(data[:, 3 + 4 * i], tm), tmp)
	result = np.uint8(result)
	return result, leak

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

# function result = aes_crypt(input_data, secret_key, encrypt)

#  performs AES-128 encryptions or decryptions
# 
#  DESCRIPTION:
# 
#  [result] = aes_crypt(input_data, secret_key, encrypt)
# 
#  This function performs an AES-128 encryption or decryption of the input
#  data with the given secret key.
# 
#  PARAMETERS:
# 
#  - input_data:
#    A matrix of bytes, where each line consists of a 16 bytes (128 bit)
#    data input value of the AES-128 en/decryption.
#  - secret_key:
#    A vector of 16 bytes that represents the secret key.
#  - encrypt:
#    Paramter indicating whether an encryption or a decryption is performed
#    (1=encryption, 0=decryption).
# 
#  RETURNVALUES:
# 
#  - result:
#    A matrix of bytes of the same size as the byte matrix 'input_data'.
#    Each line of this matrix consists of 16 bytes that represent the
#    128-bit output of an AES-128 en/decryption of the corresponding line of
#    'input_data'.
# 
#  EXAMPLE:
# 
#  result = aes_crypt([1:16 17:32], 1:16, 1)

#  AUTHORS: Stefan Mangard, Mario Kirschbaum
# 
#  CREATION_DATE: 31 July 2001
#  LAST_REVISION: 28 October 2008


def aes_crypt(input_data, secret_key, encrypt):

	if encrypt == 0:

		for i in range(9, -1, -1):
			input_data = aes_add_round_key(aes_round_key(secret_key, i), input_data)

			if i != 9:
				input_data = aes_mix_columns(input_data, 0)

			input_data = aes_shift_rows(input_data, 0)

			input_data = np.uint8(aes_sbox(input_data, 0))

		input_data = aes_add_round_key(secret_key, input_data)

	else:

		input_data = aes_add_round_key(secret_key, input_data)

		for i in range(10):
			input_data = np.uint8(aes_sbox(input_data, 1))

			input_data = aes_shift_rows(input_data, 1)

			if i != 9:
				input_data = aes_mix_columns(input_data, 1)

			input_data = aes_add_round_key(aes_round_key(secret_key, i), input_data)

	result = input_data
	return result

# function result = aes_crypt_8bit(input_data, secret_key, encrypt)

#  performs AES-128 encryptions or decryptions(using 8-bit uC algorithm)
# 
#  DESCRIPTION:
# 
#  [result] = aes_crypt_8bit(input_data, secret_key, encrypt)
# 
#  This function performs an AES-128 encryption or decryption of the input
#  data with the given secret key.
# 
#  PARAMETERS:
# 
#  - input_data:
#    A matrix of bytes, where each line consists of a 16 bytes (128 bit)
#    data input value of the AES-128 en/decryption.
#  - secret_key:
#    A vector of 16 bytes that represents the secret key.
#  - encrypt:
#    Paramter indicating whether an encryption or a decryption is performed
#    (1=encryption, 0=decryption).
# 
#  RETURNVALUES:
# 
#  - result:
#    A matrix of bytes of the same size as the byte matrix 'input_data'.
#    Each line of this matrix consists of 16 bytes that represent the
#    128-bit output of an AES-128 en/decryption of the corresponding line of
#    'input_data'.
# 
#  EXAMPLE:
# 
#  result = aes_crypt([1:16: 17:32], 1:16, 1)


#  AUTHORS: Stefan Mangard, Mario Kirschbaum
# 
#  CREATION_DATE: 31 July 2001
#  LAST_REVISION: 28 October 2008


def aes_crypt_8bit(input_data, secret_key, encrypt):

	if encrypt == 0:

		for i in range(9, -1, -1):
			input_data = aes_add_round_key(aes_round_key(secret_key, i), input_data)

			if i != 9:
				input_data = aes_mix_columns_8bit(input_data, 0)

			input_data = aes_shift_rows(input_data, 0)

			input_data = np.uint8(aes_sbox(input_data, 0))

		input_data = aes_add_round_key(secret_key, input_data)

	else:

		input_data = aes_add_round_key(secret_key, input_data)
		for i in range(10):
			input_data = np.uint8(aes_sbox(input_data, 1))

			input_data = aes_shift_rows(input_data, 1)

			if i != 9:
				input_data = aes_mix_columns_8bit(input_data, 1)
			input_data = aes_add_round_key(aes_round_key(secret_key, i), input_data)

	result = input_data
	return result

# function [result state rkeys mixcolumn_leak]= aes_crypt_8bit_and_leak(input_data, secret_key, encrypt)

#  performs AES-128 encryptions or decryptions like an 8-bit uC would do them
#  and leaks internal state 
# 
#  DESCRIPTION:
# 
#  [result state rkeys mixcolumn_leak] = aes_crypt(input_data, secret_key, encrypt)
# 
#  This function performs an AES-128 encryption or decryption of the input
#  data with the given secret key.
# 
#  PARAMETERS:
# 
#  - input_data:
#    A matrix of bytes, where each line consists of a 16 bytes (128 bit)
#    data input value of the AES-128 en/decryption.
#  - secret_key:
#    A vector of 16 bytes that represents the secret key.
#  - encrypt:
#    Paramter indicating whether an encryption or a decryption is performed
#    (1=encryption, 0=decryption).
# 
#  RETURNVALUES:
# 
#  - result:
#    A matrix of bytes of the same size as the byte matrix 'input_data'.
#    Each line of this matrix consists of 16 bytes that represent the
#    128-bit output of an AES-128 en/decryption of the corresponding line of
#    'input_data'.
#  - state:
#    A matrix of byte of size |'input_data'| x 41, containins the state
#    progression of the encryption process.  
#    Legend of the state progression:
#    (P= plaintext, C=Ciphertext, K=after AddKey, B=after SubBytes, R=after
#    ShiftRows, M=after MixColumns)
#    P K BRMK BRMK BRMK BRMK BRMK BRMK BRMK BRMK BRMK BRK(=C)
#  - mixcolumn_leak:
#    A matrix of size |'input_data'| x 9 x 4 x 9 (for encryption), or
#                     |'input_data'| x 9 x 4 x 18 (for decryption),
#        where mixcolumn_leak(line, subround, col, :) is the list of
#        intermediate valutes generated by the 8-bit MC operation on the
#        [col] columns of line [line] in the input data during
#        subroun [subround]
#  EXAMPLE:
# 
#  result = aes_crypt([1:16; 17:32], 1:16, 1)


#  AUTHORS: Stefan Mangard, Mario Kirschbaum, Yossi Oren
# 
#  CREATION_DATE: 31 July 2001
#  LAST_REVISION: 28 October 2008


def aes_crypt_8bit_and_leak(input_data, secret_key, encrypt):
	list = [41]
	for item in np.shape(input_data):
		list += [item]
	state = np.zeros(list, dtype=np.uint8)
	rkeys = np.zeros([10, 16], dtype=np.uint8)
	if encrypt == 0:  # decryption
		mixcolumn_leak = np.zeros([9, 4, np.shape(input_data)[0], 18])
	else:  # encryption
		mixcolumn_leak = np.zeros([9, 4, np.shape(input_data)[0], 9])
	
	for round in range(10):
		rkeys[round, :] = aes_round_key(secret_key, round)
	
	#  expand the keys
	
	if encrypt == 0:  # decryption
		state[40, :] = input_data
	
		for i in range(9, -1, -1):
			if i != 9:
				input_data = aes_add_round_key(aes_round_key(secret_key, i), input_data)
				state[2 + i*4 + 2, :] = input_data
	
				[input_data, leak] = aes_mix_columns_8bit_and_leak(input_data, 0)
				mixcolumn_leak[i, :, :, :] = leak
				state[2 + i*4 + 1, :] = input_data
			else:
				input_data = aes_add_round_key(aes_round_key(secret_key, i), input_data)
				state[2 + i*4 + 1, :] = input_data
	
			input_data = aes_shift_rows(input_data, 0)
			state[2 + i*4, :] = input_data
	
			input_data = np.uint8(aes_sbox(input_data, 0))
			state[2 + i*4 - 1, :] = input_data
	
		input_data = aes_add_round_key(secret_key, input_data)
		state[0, :] = input_data
	
	else:  # encryption
	
		state[0, :] = np.copy(input_data)
		input_data = aes_add_round_key(secret_key, input_data)
		state[1, :] = np.copy(input_data)
	
	for i in range(10):
			input_data = np.uint8(aes_sbox(input_data, 1))
			state[2 + i*4, :] = np.copy(input_data)
	
			input_data = aes_shift_rows(input_data, 1)
			state[2 + i*4 + 1, :] = np.copy(input_data)
	
			if i != 9:
				[input_data, leak] = aes_mix_columns_8bit_and_leak(input_data, 1)
				mixcolumn_leak[i, :, :, :] = np.copy(leak)

				state[2 + i*4 + 2, :] = np.copy(input_data)
	
				input_data = aes_add_round_key(aes_round_key(secret_key, i), input_data)
				state[2 + i*4 + 3, :] = np.copy(input_data)
			else:
				input_data = aes_add_round_key(aes_round_key(secret_key, i), input_data)
				state[2 + i*4 + 2, :] = np.copy(input_data)

	result = np.copy(input_data)
	return result, state, rkeys, mixcolumn_leak
