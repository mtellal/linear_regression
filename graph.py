import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from estimate_price import linear_function
from load import load

def main():
    try:
        file = load("data.csv")
        file = np.array(file)
        if file is None:
            return
        mileages = file[1:, 0].tolist()
        prices = file[1:, 1].tolist()

        a, b = linear_function(mileages, prices)
        y = [e for e in range(20000, 200000, 10000)]
        x = [a * e + b for e in y]
        plt.plot(x, y)

        plt.xlabel("mileages")
        plt.ylabel("prices")
        plt.scatter(prices, mileages)
        plt.title("France Life expectancy Projections")
        plt.show()
    except Exception as msg:
        print("Error:", msg)


if __name__ == "__main__":
    main()
