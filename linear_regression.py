import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import display_scatter, display_plot, display_scatter_ax, display_scatter_plot

# regression lineaire
# definition du modele soit ax + b
# fonction cout
# descente de gradiant sur la fonction cout pour optimiser les facteurs a et b


class LinearRegression:

    def __init__(self, X: list, Y: list):
        self.t0 = 0
        self.t1 = 0
        self.R = 0.1
        self.steps = 1000
        self.m = len(X)
        self.X = X
        self.Y = Y
        self.X_raw = X
        self.Y_raw = Y
        self.y_min = min(Y)
        self.y_max = max(Y)
        self.x_min = min(X)
        self.x_max = max(X)
        self.costs = []
        self.data_normalized = False
        self.trained = False
        self.normalize()


    def display_costs(self):
        if len(self.costs) == 0:
            return
        display_plot(np.arange(len(self.costs)), self.costs, 
        title="Costs", xlabel="iterations theta/params", ylabel="value mse errors")


    def display_raw(self, norm=False):
        display_scatter(self.X_raw, self.Y_raw, "Datas Raw")
        if norm: display_scatter(self.X, self.Y, "Datas Normalized")


    def display_final(self, norm=False): 
        if self.trained is False:
            return
        if norm:
            display_scatter_ax(scatter={'X': self.X, 'Y': self.Y},
            ax={'xy1': (0, self.t0), 'slope':self.t1}, 
            title="After Training (norm)")

        x_values = self.X_raw
        y_values = [ self.denormalize(self.estimate_price(x), "Y") for x in self.X]
        display_scatter_plot(scatter={'X': self.X_raw, 'Y': self.Y_raw},
        plot={'X': x_values, 'Y': y_values}, 
        title="After Training")


    def estimate_price(self, x, norm_x=False, norm_y=True):
        if norm_x:
            x = (x - self.x_min) / (self.x_max - self.x_min)
        res = self.t0 + self.t1 * x
        if norm_y is False:
            res = self.denormalize(res, "Y")
            res = res if res > 0 else 0
        return res


    def normalize(self):
        if self.data_normalized:
            return 
        self.data_normalized = True
        x_min = min(self.X)
        x_max = max(self.X)
        y_min = min(self.Y)
        y_max = max(self.Y)
        normalize_x = lambda x: (x - x_min) / (x_max - x_min) 
        normalize_y = lambda y: (y - y_min) / (y_max - y_min) 
        if len(self.X.shape) > 1:
            for line in self.X:
                line = line.apply(normalize_x) 
        self.X = self.X.apply(normalize_x)
        self.Y = self.Y.apply(normalize_y) 


    def denormalize(self, value, l='X'):
        if value == 0: return 0 
        if l == 'X':
            return value * (self.x_max - self.x_min) + self.x_min
        else:
            return value * (self.y_max - self.y_min) + self.y_min


    def calcosts(self, Y_pred):
        return (1 / (2 * self.m)) * (np.sum(Y_pred - self.Y)**2)


    def displayTrain(self, rplt, tmp_t0, tmp_t1):
        plt.scatter(self.X, self.Y, label="real datas")
        plt.axline(xy1=(tmp_t0, tmp_t1*0), slope=tmp_t1, c='#ff7f00', label="hypothese(x)")
        plt.legend(loc="lower right")
        plt.pause(0.00000001)
        rplt.clear()


    def train(self, display=False, costs=False):
        if self.trained:
            return 
        self.trained = True
        tmp_t0 = self.t0
        tmp_t1 = self.t1
        if display:
            rplt = plt.figure("Training")
            plt.xlabel("mileages")
            plt.ylabel("prices")
        for i in range(self.steps):
            print(f'\r{"Training ...":19} ({i+1}/{self.steps}) t0={tmp_t0} t1={tmp_t1}', flush=True, end='')
            Y_predict = self.estimate_price(self.X)
            tmp_t0 = tmp_t0 - self.R * ((1 / self.m) * np.sum(Y_predict - self.Y))  
            tmp_t1 = tmp_t1 - self.R * ((1 / self.m) * np.sum((Y_predict - self.Y) * self.X))  
            self.t0 = tmp_t0
            self.t1 = tmp_t1
            if costs: self.costs.append(self.calcosts(Y_predict))
            if display: self.displayTrain(rplt, tmp_t0, tmp_t1)    
        print("")

    """
    def tests(self):
        t0 = self.t0
        t1 = self.t1
        print(f'\n{"MILEAGES":20} | {"ESTIMATION":12} | {"REAL PRICE":20}')
        _X = list(self.X)
        _X.sort()
        _Y = list(self.Y)
        _Y.sort()
        for i in range(0, len(_X)):
            print(f'{self.denormalize(_X[i]):<20} | {int(self.denormalize(t0 + t1 * _X[i], "Y")):<12} | {self.denormalize(_Y[i], "Y"):<20}')
    """
