from load_csv import load
import matplotlib.pyplot as plt


"""
A program that calls the load function
from the previous exercise, loads the file
life_expectancy_years.csv, and displays
the country information of your campus. Your
graph must have a title and a legend for each axis.
"""


def main():
        try:
                    file = load("life_expectancy_years.csv")
                            if file is None:
                                            return

                                                dates = file.columns
                                                        dates = [int(label) for label in dates if label != "country"]

                                                                valid_columns = ~file.columns.isin(["country"])
                                                                        france_ages = file.loc[file.country == "France", valid_columns]
                                                                                france_ages = france_ages.squeeze().to_numpy()

                                                                                        indexes = [i for i in range(1800, 2081, 40)]
                                                                                                values = [str(x) for x in indexes]

                                                                                                        plt.plot(dates, france_ages)
                                                                                                                plt.xticks(indexes, values)
                                                                                                                        plt.xlabel("Year")
                                                                                                                                plt.ylabel("Life expectancy")
                                                                                                                                        plt.title("France Life expectancy Projections")
                                                                                                                                                plt.show()
                                                                                                                                                    except Exception as msg:
                                                                                                                                                                print("Error:", msg)


                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                        main()

