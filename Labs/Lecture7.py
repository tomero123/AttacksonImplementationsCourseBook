import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sp
from hamming_weight import hamming_weight
from aes_scripts.aes_crypt_8bit_and_leak import aes_crypt_8bit_and_leak, aes_sbox

#  Differential power analysis and correlation power analysis
DPA = 0
CPA = 1
dpa_or_cpa = CPA  # DPA


# #
#  Make sure the matlab AES scripts are in the path

#  Load WS2, show a few traces
def main():
	ws2 = sp.loadmat('WS2.mat')
	print(np.shape(ws2['traces']))  # D = 200, T = 100000

	#  shrink it a little so it runs faster
	traces = ws2['traces'][:, 0:30000]
	input_count = np.shape(traces)[0]
	trace_length = np.shape(traces)[1]
	# #
	plt.plot(traces[0, :])
	plt.plot(traces[1, :])
	plt.xlim([300, 500])
	plt.ylim([-80, 100])
	plt.figure()
	# figure(gcf)
	# #
	#  We want to guess byte 1 in the key
	key_byte_to_guess = 12
	classification_output = np.zeros(shape=(2**8, trace_length))
	print(np.shape(classification_output))
	# #
	#  For each key guess
	trace_classification = np.zeros(shape=(2**8, input_count))
	inputs = ws2['inputs']

	for key_guess in range(2**8):
		# For each plaintext input
		for input in range(input_count):
			# Calculate what the value of S[P ^ K] is
			p_xor_k = np.bitwise_xor(inputs[input, key_byte_to_guess - 1], key_guess)
			s_p_xor_k = aes_sbox(p_xor_k, 1)

			if dpa_or_cpa == DPA:
				trace_classification[key_guess, input] = (np.bitwise_and(s_p_xor_k, 1) != 0)
			else:
				trace_classification[key_guess, input] = hamming_weight(s_p_xor_k)

		# % Calculate the mean of each classified set
		if dpa_or_cpa == DPA:
			mean_for_1 = np.mean(traces[trace_classification[key_guess, :] == 1, :])
			mean_for_0 = np.mean(traces[trace_classification[key_guess, :] == 0, :])
			# % Save the difference of means in the table
			classification_output[key_guess, :] = mean_for_1 - mean_for_0
		else:
			shape = np.shape(trace_classification[key_guess, :])
			my_trace = np.reshape(trace_classification[key_guess, :], newshape=(shape[0], 1))

			traces1 = (traces - traces.mean(axis=0))/traces.std(axis=0)  # A matrix
			my_trace = (my_trace - my_trace.mean(axis=0))/my_trace.std(axis=0)  # B matrix
			correlation = (np.dot(my_trace.T, traces1) / my_trace.shape[0])[0]

			classification_output[key_guess, :] = np.transpose(correlation)

		print('[{:02x}]'.format(key_guess), end=" ")
		if (key_guess % 16) == 15:
			print('\n')

	# #
	#  Plot the trace classification matrix
	plt.imshow(trace_classification)
	# #imagesc(trace_classification)
	plt.xlabel('Trace index')
	plt.ylabel(['Key guess for byte ' + str(key_byte_to_guess)])
	plt.figure()
	# ##figure(gcf)
	# #
	#  Find out the correct timne and correct key
	absolute = np.abs(classification_output)
	index = np.unravel_index(np.argmax(absolute, axis=None), absolute.shape)
	correct_time = index[1]

	absolute = np.abs(classification_output[:, correct_time])
	correct_key = np.argmax(absolute)  # this is actually correct_key + 1

	heights = np.abs(classification_output[:, correct_time])
	plt.bar(range(1, np.shape(classification_output)[0] + 1), heights)
	plt.xlabel('Key guess')
	plt.figure()
	# #
	#  CPA only: show the actual power consumption at correct time, compared to
	#  power model
	temp = traces[:, correct_time]
	plot1 = np.true_divide(traces[:, correct_time], 5)
	plt.plot(plot1)
	plt.plot(np.transpose(trace_classification[correct_key, :]))
	plt.xlabel('Trace index')
	plt.ylabel({'Power consumption at correct time (blue)', 'Power model for correct key (red)'})
	plt.figure()
	# #
	#  plot the correct key at the correct time
	plt.plot(np.transpose(classification_output))
	plt.xlim([correct_time - 100, correct_time + 100])
	plt.figure()
	# hold on
	plt.plot(classification_output[correct_key, :], linestyle='dashed', linewidth=5)
	# hold off
	plt.figure()
	plt.show()


if __name__ == '__main__':
	main()
