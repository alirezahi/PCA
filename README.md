# PCA
Principal Components Analysis using normal distribution

Normal Distribution (also called Gaussian Distribution) is a very common continuous probability distribution.

It cann be achieved using numpy in python : 

~~~
import numpy as np

#single dimenstional
mean, covariance, number_of_samples = 3, 2, 1000
random_numbers = np.random.normal(mean,covariance,number_of_samples)

#multi dimenstional
mean, covariance, number_of_samples = [10,10], [[4,4],[4,9]], 1000
random_numbers = np.random.multivariate_normal(mean,covariance,number_of_samples)
~~~