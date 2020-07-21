import numpy as np
from aes_scripts.aes_sbox import aes_sbox
from aes_scripts.aes_xtimes import aes_xtimes

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
