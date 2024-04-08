import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# regression lineaire
# definition du modele soit ax + b
# fonction cout
# descente de gradiant sur la fonction cout pour optimiser les facteurs a et b



class LinearRegression:

    def __init__(self, X: list, Y: list):
        self.t0 = 0
        self.t1 = 0
        self.R = 0.01
        self.steps = 1000
        self.m = len(X)
        self.X = X
        self.Y = Y
        self.costs = []

    def estimate_price(self, mileage: int, display=False):
        estimated_price = self.theta0 + self.theta1 * mileage 
        if display:
            print(f'estimate_price({mileage}): {estimated_price}')
        return extimated_price


    def calcosts(self, Y_pred):
        return (1 / (2 * self.m)) * (np.sum(Y_pred - self.Y)**2)


    def normalize(self):
        x_min = min(self.X)
        x_max = max(self.X)
        y_min = min(self.Y)
        y_max = max(self.Y)
        normalize_x = lambda x: (x - x_min) / (x_max - x_min) 
        normalize_y = lambda y: (y - y_min) / (y_max - y_min) 
        self.X = self.X.apply(normalize_x) 
        self.Y = self.Y.apply(normalize_y) 


    def evaluate_costs(self):
        tmp_t0 = 0
        tmp_t1 = 0
        for i in range(30):
            Y_predict = tmp_t0 + tmp_t1 * self.X
            tmp_t0 = tmp_t0 - self.R * ((1 / self.m) * np.sum(Y_predict - self.Y))  
            tmp_t1 = tmp_t1 - self.R * ((1 / self.m) * np.sum((Y_predict - self.Y) * self.X))  
            self.costs.append(self.calcosts(Y_predict))
        self.costs += self.costs


    def train(self):
        tmp_t0 = 0
        tmp_t1 = 0 
        for i in range(self.steps):
            Y_predict = tmp_t0 + tmp_t1 * self.X
            tmp_t0 = tmp_t0 - self.R * ((1 / self.m) * np.sum(Y_predict - self.Y))  
            tmp_t1 = tmp_t1 - self.R * ((1 / self.m) * np.sum((Y_predict - self.Y) * self.X))  
        print(tmp_t0, tmp_t1)
        self.t0 = tmp_t0
        self.t1 = tmp_t1


    def getCoefficients(self):
        return self.t0, self.t1




file = pd.read_csv("data.csv")
X = file.iloc[:, 0]
Y = file.iloc[:, 1]

l = LinearRegression(X, Y)

l.normalize()
#l.train()

#t0, t1 = l.getCoefficients()


l.evaluate_costs()

plt.plot(np.arange(len(l.costs)), l.costs)
plt.show()


