import matplotlib.pyplot as plt


def display_scatter(X, Y, title="Datas", xlabel="mileages", ylabel="prices"):
    rplt = plt.figure(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.scatter(X, Y)
    return rplt

def display_scatter_ax(scatter, ax, title="Datas", xlabel="mileages", ylabel="prices"):
    rplt = plt.figure(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.scatter(scatter['X'], scatter['Y'])
    plt.axline(xy1=ax['xy1'], slope=ax['slope'], color='#ff7f00')
    return rplt

def display_scatter_plot(scatter, plot, title="Datas", xlabel="mileages", ylabel="prices"):
    rplt = plt.figure(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.scatter(scatter['X'], scatter['Y'])
    plt.plot(plot['X'], plot['Y'], color='#ff7f00')
    return rplt