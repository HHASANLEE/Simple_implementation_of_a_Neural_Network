import numpy as np

# array of any amount of numbers
X = np.array([[1, 2, 3],
              [3, 4, 1],
              [2, 5, 3]])

# multiplication
y = np.array([.2, .5, .3])

# transpose of y
y = y.T

# sigma value
sigm = 2

# find the delta
delt = np.random.random((3, 3)) - 1

for j in range(100):

    # find matrix in 1. 100 layers
    m1 = (y - (1 / (1 + np.exp(-(np.dot((1 / (1 + np.exp(
        -(np.dot(X, sigm))))), delt))))))*((1 /
         (1 + np.exp(-(np.dot((1 / (1 + np.exp(
        -(np.dot(X, sigm))))), delt)))))*(1 - (1 /
         (1 + np.exp(-(np.dot((1 / (1 + np.exp(
        -(np.dot(X, sigm))))), delt)))))))

    # find matrix 2
    m2 = m1.dot(delt.T)*((1 / (1 + np.exp(-(np.dot(X, sigm)))))*
                        (1 - (1 / (1 + np.exp(-(np.dot(X, sigm)))))))

    # find delta
    delt = delt + (1 / (1 + np.exp(-(np.dot(X, sigm))))).T.dot(m1)

    #find sigma
    sigm = sigm + (X.T.dot(m2))

    #print output from the matrix
    print(1 / (1 + np.exp(-(np.dot(X, sigm)))))
