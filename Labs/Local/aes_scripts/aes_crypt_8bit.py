import numpy as np
from aes_scripts.aes_sbox import aes_sbox
from aes_scripts.aes_mix_columns_8bit import aes_mix_columns_8bit
from aes_scripts.aes_shift_rows import aes_shift_rows
from aes_scripts.aes_add_round_key import aes_add_round_key
from aes_scripts.aes_round_key import aes_round_key

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
