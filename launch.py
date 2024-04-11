import sys 
from load import load
from linear_regression import LinearRegression
import matplotlib.pyplot as plt

def verify_file(file):
    try:
        X = file["km"]
        Y = file["price"]
        assert len(X) == len(Y), "km and price differents length"
        for i in range(0, len(X)):
            tkm = int(X[i])
            tprice = int(Y[i])
        return X, Y
    except Exception as msg:
        raise(Exception("invalid file:", msg))
    return None


def show(inp, l):
    if inp == "show raw":
        l.display_raw(norm=True)
    elif inp == "show costs":
        l.display_costs()
    elif inp == "show final":
        l.display_final(norm=True)
    plt.show()


def main():
    try:
        file = load("data.csv")
        if file is None:
            return
        X, Y = verify_file(file)
        l = LinearRegression(X, Y)
        print("Commands:\n- \"train\": train the model\n- \"train +\": train and animate\n- \"estimate\": estimate a price from a mileage (int)\n- \"show raw\": show raw datas\n- \"show costs\": show costs plot\n- \"show final\": show final graphs\n")
        while True:
            inp = input("waiting a command: ")
            if inp == "estimate":
                m = input("Pick a mileage: ")
                try:
                    print("Estimate price:", l.estimate_price(int(m), norm_x=True, norm_y=False))
                except Exception:
                    print("error: invalid mileage")
            elif inp.startswith("train"):
                if inp == "train +":
                    l.train(costs=True, display=True)
                elif inp == "train":
                    l.train(costs=True)
            elif inp.startswith("show"):
                show(inp, l)
    except KeyboardInterrupt:
        print("\nBye !")
    except EOFError:
        print("\nBye !")
    except Exception as msg:
        print("Error:", msg)
    

if __name__ == "__main__":
    main()
