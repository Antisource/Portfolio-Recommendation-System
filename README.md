Overview
Welcome to the Portfolio Recommendation System! This Python script provides a basic implementation of a portfolio recommendation system using the 0/1 knapsack problem. Users can either input their own data or use pre-defined data for NIFTY50 stocks.

Features
User Input Options: Choose between using stored data or providing custom data for portfolio optimization.

Data Visualization: The script generates a pie chart to visually represent the recommended portfolio.

Getting Started
To run the Portfolio Recommendation System locally, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/YourGitHubUsername/Portfolio-Recommendation-System.git
Run the Script:

bash
Copy code
python portfolio_recommendation.py
Follow On-Screen Instructions:

Choose 1 for using stored data or 2 for custom data.
Enter the necessary inputs as prompted.
Prerequisites
Ensure you have the required libraries installed. For Google Colab, uncomment the following lines at the beginning of the script:

python

# For COLAB
# !pip install ortools
# !pip install matplotlib
Output
The script will provide a portfolio recommendation based on the knapsack problem solution. It includes the total risk quotient, total investment, remaining amount after investment, and details of selected stocks.

Visualization
The script generates a pie chart visualizing the recommended portfolio with stock names, prices, and proportions.

Example Usage
bash
Copy code

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
