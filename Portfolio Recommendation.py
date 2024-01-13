# For COLAB
# !pip install ortools
# !pip install matplotlib

# Import the libraries
# The following code imports the required libraries.
from ortools.algorithms import pywrapknapsack_solver
import sys
from matplotlib import pyplot as plt


def main():
    print("WELCOME PORTFOLIO RECOMMENDATION SYSTEM !!!")
    print("NIFTY50 ")
    print("RULES: \n Enter 1 to use stored data. \n Enter 2 for custom data. ")
    op = int(input())
    if op == 2:

        n = int(input("Enter number of stocks i.e entries\n"))
        print("Enter " + str(n) + "  prices i.e weights ")
        wts = []
        for i in range(n):
            x = int(input())
            wts.append(x)
        weights = [wts]

        print("Enter " + str(n) + " risk quotient i.e values ")
        print("Risk Quotient: \n 1 Low Risk \n 2 Moderate Risk \n 3 High Risk")
        values = []
        for j in range(n):
            y = int(input())
            if y < 1 or y > 3:
                print("Invalid input !!!")
                sys.exit()
            values.append(y)
        print("Enter " + str(n) + "  labels  ")
        lb = []
        for i in range(n):
            x = input()
            lb.append(x)
        labels = [lb]
    elif op == 1:
        # CREATE THE DATA
        values = [
            1, 3, 3, 2, 1, 3, 1, 2, 3, 2, 2, 1, 1, 2, 3, 1, 1, 3, 2, 2,
            2, 1, 2, 2, 2, 3, 3, 1, 2, 3, 2, 1, 1, 1, 3, 2, 3, 2, 1,
            3, 3, 1, 1, 3, 1, 3, 2, 1, 2, 3

        ]
        weights = [[
            360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
            78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
            87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
            312

        ]]

        labels = [
            ['ADANIENT', 'ADANIPORTS', 'APOLLOHOSP', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV',
             'BPCL', 'BHARTIARTL', 'BRITANNIA',
             'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFCBANK', 'HDFCLIFE',
             'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'HDFC', 'ICICIBANK',
             'ITC', 'INDUSINDBK', 'INFY', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NTPC', 'NESTLEIND', 'ONGC',
             'POWERGRID', 'RELIANCE', 'SBILIFE', 'SBIN', 'SUNPHARMA',
             'TCS', 'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN', 'UPL', 'ULTRACEMCO', 'WIPRO']]
    else:
        print('INVALID INPUT!!!')
        sys.exit()
    capacities = []
    c = int(input("Enter the amount to be invested. \n"))
    capacities.append(c)

    # CREATE THE SOLVER.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    # CALL THE SOLVER
    # The following code calls the solver and prints the solution.
    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    # PRINTING
    packed_items = []
    packed_weights = []
    packed_labels = []
    total_weight = 0
    # colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    print('RECOMMENDATION !!!')
    print('Total  Risk quotient i.e value =', computed_value)

    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i + 1)
            packed_weights.append(weights[0][i])
            packed_labels.append(labels[0][i])
            total_weight += weights[0][i]
    print('Total  Price i.e weight:', total_weight)

    print('Amount left after investment:', (c - total_weight))

    print('Stocks i.e items number:', packed_items)

    print('Prices : ', packed_weights)

    print('Stock name:', packed_labels)

    slices = packed_weights
    explode = []
    for i in packed_weights:
        explode.append(0.1)
    plt.pie(slices, labels=packed_labels, shadow=True, explode=explode, startangle=90, autopct='%1.1f%%',
            wedgeprops={'edgecolor': 'black'})
    plt.title("PORTFOLIO VISUALIZATION: \n")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
