import numpy as np

mean, covariance = [10,10] , [[4,4],[4,9]]
number_of_samples = 1000

samples = [[],[]]

samples[0] = np.random.multivariate_normal(mean,covariance,number_of_samples)
samples[1] = np.random.multivariate_normal(mean,covariance,number_of_samples)

