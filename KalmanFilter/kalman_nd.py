import numpy as np

def kalman_filter(mu, sig):
    for n, measurement in enumerate(measurements):
        mu_bar = A * mu + B * u
        sig_bar = A * sig * A.transpose()

        s = C * sig_bar * C.transpose() + Q
        K = sig_bar * C.transpose() * np.linalg.inv(s)

        z = np.matrix([[measurement]])
        mu = mu_bar + K * (z - C * mu_bar)
        sig = (I - K * C) * sig_bar
    return mu, sig

measurements = [1, 2, 3, 4, 5]

mu = np.matrix([[0.], [0.]])
sig = np.matrix([[1000., 0.], [0., 1000.]])
u = np.matrix([[0.], [0.]])
A = np.matrix([[1., 1.], [0, 1.]])
C = np.matrix([[1., 0.]])
Q = np.matrix([[1.]])
I = np.eye(2)
B = np.eye(2)

print(kalman_filter(mu, sig))