import Perceptron
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
sys.path.append("..")
import Plot_decision_regions


"""
    Visualize the misclassifications error
"""

df = pd.read_csv('https://archive.ics.uci.edu/ml/'
            'machine-learning-databases/iris/iris.data',header=None)
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

X = df.iloc[0:100, [0, 2]].values


ppn = Perceptron.Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors_) + 1 ), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Num of misclassification')
plt.show()


"""
   Visualize the decision boundaries
"""


Plot_decision_regions.plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sapal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()
time.sleep(10)
plt.close()
