# Portfolio Recommendation System

## Introduction
Welcome to the Portfolio Recommendation System! This Python script provides a basic implementation of a portfolio recommendation system using the 0/1 knapsack problem. Users can either input their own data or use pre-defined data for NIFTY50 stocks.

## Prerequisites
Before running the script, make sure you have the necessary libraries installed. If you're using Google Colab, the required libraries can be installed by uncommenting the following lines at the beginning of the script:


# For COLAB
# !pip install ortools
# !pip install matplotlib

## Getting Started
Run the script.
Choose whether to use stored data or input custom data by entering 1 or 2, respectively.
Using Stored Data (Option 1)
The script already contains data for NIFTY50 stocks.
Enter the amount to be invested.
Using Custom Data (Option 2)
Enter the number of stocks, their prices (weights), risk quotients (values), and labels.
Specify the amount to be invested.
Output
The script will provide a portfolio recommendation based on the knapsack problem solution. It includes the total risk quotient, total investment, remaining amount after investment, and details of selected stocks.

## Visualization
The script generates a pie chart visualizing the recommended portfolio with stock names, prices, and proportions.

##Example Usage

WELCOME PORTFOLIO RECOMMENDATION SYSTEM !!!
NIFTY50 
RULES: 
 Enter 1 to use stored data. 
 Enter 2 for custom data. 
1
Enter the amount to be invested. 
500
RECOMMENDATION !!!
Total  Risk quotient i.e value = 36
Total  Price i.e weight: 485
Amount left after investment: 15
Stocks i.e items number: [3, 6, 14, 15, 20, 24, 27, 29, 36, 37, 40, 44, 46, 47]
Prices :  [59, 67, 38, 48, 17, 35, 22, 50, 15, 26, 36, 43, 10, 19]
Stock name: ['APOLLOHOSP', 'BAJAJ-AUTO', 'DIVISLAB', 'DRREDDY', 'HDFCLIFE', 'HDFC', 'INDUSINDBK', 'JSWSTEEL', 'ONGC', 'POWERGRID', 'SBIN', 'TATAMOTORS', 'TECHM', 'TITAN']
