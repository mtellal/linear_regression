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
        self.steps = 10000
        self.m = len(X)
        self.X = X
        self.Y = Y
        self.costs = []
        self.data_normalized = False
        self.normalize()

    def estimate_price(self, mileage: int, display=False):
        estimated_price = self.theta0 + self.theta1 * mileage 
        if display:
            print(f'estimate_price({mileage}): {estimated_price}')
        return extimated_price


    def calcosts(self, Y_pred):
        return (1 / (2 * self.m)) * (np.sum(Y_pred - self.Y)**2)

    def display_raw(self):
        rplt = plt.figure("Datas")
        plt.xlabel("mileages")
        plt.ylabel("prices")
        plt.scatter(X, Y)
        rplt.show()

    def display_norm(self):
        rplt = plt.figure("Datas normalized")
        plt.xlabel("mileages")
        plt.ylabel("prices")
        plt.scatter(self.X, self.Y)
        rplt.show()

    def display_final_norm(self):
        rplt = plt.figure("Datas normalized")
        plt.xlabel("mileages")
        plt.ylabel("prices")
        plt.scatter(self.X, self.Y)
        plt.axline(xy1=(self.t1*min(self.X), self.t0), slope=self.t1, color='#ff7f00')
        rplt.show()

    def display_final(self):
        rplt = plt.figure("Datas final")
        plt.xlabel("mileages")
        plt.ylabel("prices")
        plt.scatter(X, Y)
        x_values = X
        y_values = [ self.denormalize(x * self.t1 + self.t0, Y) for x in self.X]
        plt.plot(x_values, y_values, c='#ff7f00')
        rplt.show()

    def normalize(self):
        if self.data_normalized is True:
            return 
        self.data_normalized = True
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
        for i in range(self.steps):
            Y_predict = tmp_t0 + tmp_t1 * self.X
            tmp_t0 = tmp_t0 - self.R * ((1 / self.m) * np.sum(Y_predict - self.Y))  
            tmp_t1 = tmp_t1 - self.R * ((1 / self.m) * np.sum((Y_predict - self.Y) * self.X))  
            self.costs.append(self.calcosts(Y_predict))


    def display_costs(self):
        self.evaluate_costs()
        cplt = plt.figure("costs")
        plt.plot(np.arange(len(l.costs)), l.costs)
        cplt.show()


    def train(self):
        tmp_t0 = 0
        tmp_t1 = 0
        tplot = plt.figure("training")
        for i in range(self.steps):
            Y_predict = tmp_t0 + tmp_t1 * self.X
            tmp_t0 = tmp_t0 - self.R * ((1 / self.m) * np.sum(Y_predict - self.Y))  
            tmp_t1 = tmp_t1 - self.R * ((1 / self.m) * np.sum((Y_predict - self.Y) * self.X))  
        self.t0 = tmp_t0
        self.t1 = tmp_t1

    def denormalize(self, value, X):
        return value * (max(X) - min(X)) + min(X)


    def tests(self):
        t0 = self.t0
        t1 = self.t1
        for i in range(0, len(self.X)):
            print("X =", self.denormalize(self.X[i], X))
            print(f'estimate_Price: {self.denormalize(t0 + t1 * self.X[i], Y)} - real price: {self.denormalize(self.Y[i], Y)}')

    def getCoefficients(self):
        return self.t0, self.t1




file = pd.read_csv("data.csv")
X = file.iloc[:, 0]
Y = file.iloc[:, 1]

l = LinearRegression(X, Y)

#l.display_raw()
#l.display_norm()
l.train()

l.display_final_norm()
l.display_final()

l.tests()

plt.show()
