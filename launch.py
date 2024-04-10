import sys 
from load import load
from linear_regression import LinearRegression
import matplotlib.pyplot as plt


def show(inp, l):
    if inp == "show raw":
        l.display_raw(norm=True)
    elif inp == "show costs":
        l.display_costs()
    elif inp == "show final":
        l.display_final(norm=True)
    plt.show()


def main():
    # recup les coeff dans le fichier .coffs
    # et applique notre hypothese
    file = load("data.csv")
    X = file["km"]
    Y = file["price"]
    l = LinearRegression(X, Y)
    print("Commands:\n- \"train\": train the model\n- \"estimate\": estimate a price from a mileage (int)\n- Shows commands: show graphs\n\t-\"show raw\": show raw datas\n\t-\"show costs\": show costs plot\n\t-\"show trained\": show final graphs\n")
    while True:
        inp = input("waiting a command: ")
        if inp == "Exit":
            break
        elif inp == "estimate":
            m = input("Pick a mileage: ")
            try:
                print("Estimate price:", l.estimate_price(int(m), norm_x=True, norm_y=False))
            except Exception:
                print("error: invalid mileage")
        elif inp.startswith("train"):
            if inp == "train -":
                l.train(costs=True, display=False)
            elif inp == "train":
                l.train(costs=True)
        elif inp.startswith("show"):
            show(inp, l)
        print("")
    

if __name__ == "__main__":
    main()
