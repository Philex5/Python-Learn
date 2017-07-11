import numpy as np
class Perceptron(object):
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

    """

    def __init__(self,eta=0.01,n_iter=10):
        self.eta=eta
        self.n_iter=n_iter

    def fit(self,X,y):
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

        self.w_=np.zeros(1+X.shape[1])
        self.errors_=[]

        for _ in range(self.n_iter):
            errors=0
            for xi,target in zip(X,y):
                update=self.eta*(target-self.predict(xi))
                self.w_[1:]+=update*xi
                self.w_[0]+=update
                errors+=int(update!=0.0)
            self.errors_.append(errors)
        return self

    def net_input(self,X):
        """calculate net input"""
        """计算矩阵和得到z，再与阈值的相反数相加"""
        return np.dot(X,self.w_[1:])+self.w_[0]

    def predict(self,X):
        """return class laber after unit step"""
        return np.where(self.net_input(X) >= 0.0,1,-1)


