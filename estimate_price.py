from load import load
import numpy as np
import sys

"""
The first program will be used to predict the price of a car for a given mileage.
When you launch the program, it should prompt you for a mileage, and then give
you back the estimated price for that mileage. The program will use the following
hypothesis to predict the price :
    estimateP rice(mileage) = θ0 + (θ1 ∗ mileage)
    Before the run of the training program, theta0 and theta1 will be set to 0.
"""

# f(x) = ax + b  _    _   _
#     Cov(X;Y)   xy - x * y
# a = -------- = -_-----_--
#       V(X)      x^2 - x^2

# b = /y - a * /x


def variance(x: list):
    square_x_avrg = sum([e ** 2 for e in x]) / len(x)  
    square_avrg_x = (sum(x) / len(x)) ** 2
    return square_x_avrg - square_avrg_x


def covariance(x: list, y: list):
    avrg_x = sum(x) / len(x)
    avrg_y = sum(y) / len(y)
    avrg_xy = sum([x[i] * y[i] for i in range(0, len(x))]) / len(x)
    return avrg_xy - avrg_x * avrg_y
    

def linear_function(x: list, y: list):
    a = covariance(x, y) / variance(x)

    avrg_y = sum(y) / len(y)
    avrg_x = sum(x) / len(x)
    b = avrg_y - a * avrg_x

    return (a, b)


def main():
    file = load("data.csv")
    file = np.array(file)
    mileages = file[0:, 0]
    prices = file[0:, 1]
    a, b = linear_function(mileages, prices)
    if len(sys.argv) == 2:
        a, b = linear_function(mileages, prices) 
        print(f'mileages: {sys.argv[1]}\nprices: {a * int(sys.argv[1]) + b}') 
        return 
    print(f'mileages: 50000\nprices: {a * 50000 + b}')


if __name__ == "__main__":
    main()
