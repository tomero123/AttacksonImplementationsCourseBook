import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# Create two random vectors
def main():
	mu_1 = 10
	mu_2 = 10.5

	sigma2_1 = 4
	sigma2_2 = 4

	vector_length = 400

	x = np.random.normal(size=vector_length) * sigma2_1 + mu_1
	y = np.random.normal(size=vector_length) * sigma2_2 + mu_2

	plt.plot(x, np.zeros(400), '*', y, np.ones(400), '*')
	plt.ylim(-2, 3)
	plt.show()

	# Are these from the same distribution?
	# (0 = same distribution, 1 = different distribution)
	# p - probability they're from the same distribution
	h, p = stats.ttest_ind(x, y)
	if p > 0.05:
		print('Same distribution w.p. %1.3g\n', p)
	else:
		print('Different distributions w.p. %1.3g\n', 1 - p)


if __name__ == '__main__':
	main()
