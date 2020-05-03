import numpy as np


def hamming_weight2(_input):

	# %HAMMING_WEIGHT Hamming weight for rows of an input of any size
	input_as_uint32 = np.uint32(np.reshape(_input, np.shape(_input)))
	hw = np.zeros(np.shape(_input)[0])

	# % while there are still nonzero values in the vector
	while np.count_nonzero(input_as_uint32) > 0:
		# % take the LSBs of all the input
		hw = hw + np.sum((input_as_uint32 & 1), 1)
		# % shift it right by one position
		input_as_uint32 = input_as_uint32 >> 1

	# % remove redundant dimensions
	hw = np.squeeze(np.transpose(hw))
	return np.sum(hw)


def hamming_weight(_input):
	# function [ hw ] = hamming_weight( input )
	# %HAMMING_WEIGHT Hamming weight for rows of an input of any size
	if np.shape(_input).__len__() > 2:
		dim = 1
		for n in np.shape(_input):
			dim *= n
		dim1 = np.shape(_input)[0]
		dim = int(dim / dim1)
		input_as_uint32 = np.uint32(np.reshape(_input, (dim1, dim)))
		hw = np.zeros((np.shape(_input)[0], 1))
		# % while there are still nonzero values in the vector
		while np.count_nonzero(input_as_uint32) > 0:
			# % take the LSBs of all the input
			hw = hw + np.reshape(np.transpose(np.sum((np.squeeze(input_as_uint32) & 1), 1)), newshape=np.shape(hw))
			# % shift it right by one position
			input_as_uint32 = input_as_uint32 >> 1

		# % remove redundant dimensions
		hw = np.squeeze(np.transpose(hw))
		return hw
	else:
		return hamming_weight2(_input)
