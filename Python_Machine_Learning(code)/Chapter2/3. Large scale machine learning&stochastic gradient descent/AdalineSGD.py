import numpy as np
from numpy.random import seed

class AdalineSGD(object):
    """Perceptron classifier.

    Parameters
    ------------
    eta: float
        Learning rate(between 0.0 and 1.0)
    n_iter: int
        passes over the training dataset.

    Attrributes
    -------------
    w_:1d-array
       Weights after fitting.
    errors_: list
       Number of misclassifications in every epoch.
    shuffle : bool (default : True)
       shuffles training data every epoch
       if True to prevent cycles
    random_state : int (default:None)
       Set random state for shuffling
       and initializing the weights
    """

    def __init__(self, eta=0.01, n_iter=10, shuffle=True, random_state=None):
        self.eta = eta
        self.n_iter = n_iter
        self.w_initialized =False
        self.shuffle = shuffle
        if random_state:
            seed(random_state)

    def fit(self, X, y):
        """Fit training data

        parameter
        ___________
        X:{array_like},shape={n_samples,n_features}
          Training vectors,where n_samples
          is the number of samples and
          n_features is the number of features
        y: arrary-like,shape={n_sample}
           Target values.

        Returns
        __________
        self :object

        """

        self.    w_ = np.zeros(1+X.shape[1])
        self.cost_ = []

        for _ in range(self.n_iter):
            if  self.shuffle:
                X, y = self._shuffle(X, y)
            cost = []
            for xi, target in zip(X, y):
                cost.append(self._update_weights(xi, target))
            avg_cost = sum(cost)/len(y)
            self.cost_.append(avg_cost)

        return self

    def partial_fit(self, X, y):
        """Fit training data without reinitializing the weights,using for on-line learning"""
        if not self.w_initialized:
            self._initialize_weights(X.shape(1))
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X, y):
                self._update_weights(xi, target)
        else:
            self._update_weights(X, y)
        return self

    def _shuffle(selfself, X, y):
        """shuffle training data"""
        """r is a random sequence of unique numbers in the range 0 to 100
           Those numbers can then be used as indices to shuffle our feature matrix and class label vector"""
        r = np.random.permutation(len(y))
        return X[r], y[r]

    def _initialize_weights(self, m):
        """Initialize weights to zeros"""
        self.w_ = np.zeros(1 + m)
        self.w_initialized = True

    def _update_weights(self, xi, target):
        """Apply Adaline learning rule to update the weights"""
        output = self.net_input(xi)
        error = (target - output)
        self.w_[1:] += self.eta * xi.dot(error)
        self.w_[0] += self.eta * error
        cost = 0.5 * error**2
        return cost

    def net_input(self, X):
        """calculate net input"""
        """计算矩阵乘积得到z，再与阈值的相反数相加"""
        return np.dot(X, self.w_[1:])+self.w_[0]

    def activation(self, X):
        return self.net_input(X)

    def predict(self, X):
        """return class laber after unit step"""
        return np.where(self.activation(X) >= 0.0, 1, -1)

