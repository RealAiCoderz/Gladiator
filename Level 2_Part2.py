import mysql.connector
import pandas as pd

# Establishing a connection to your MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root123@",
  database="MyDB"
)

# Creating a cursor to execute SQL queries
mycursor = mydb.cursor()

# SQL query to retrieve data from both tables
sql_query = """
SELECT Marvel.Name, Marvel.Height, Marvel.Weight, Marvel.Games_Played
FROM Marvel
UNION ALL
SELECT DC.Name, DC.Height, DC.Weight, DC.Games_Played
FROM DC;
"""

# Executing the SQL query
mycursor.execute(sql_query)

# Fetching all the rows from the result set
data = mycursor.fetchall()


import numpy as np
# Extracting weights (index 2) and games played (index 3) from each tuple
weights = [idx[2] for idx in data]
weights = [int(item) for item in weights]
games_played = [idx[3] for idx in data]

#Plotting ScatterPlot
import matplotlib.pyplot as plt
plt.scatter(weights, games_played, c='darkgray', s=100)
plt.xticks(range(min(weights), max(weights) + 1, 20))
plt.yticks(range(min(games_played), max(games_played) + 1, 50))
plt.xlabel('Weight')
plt.ylabel('Games Played')
plt.show()

#Linear Regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Weights and games_played to arrays
weights = np.array(weights).reshape(-1, 1)
games_played = np.array(games_played).reshape(-1, 1)

model = LinearRegression()
model.fit(weights, games_played)

slope = model.coef_[0][0]  # Accessing the slope value
intercept = model.intercept_[0]  # Accessing the intercept value

print(f"Linear Regression Equation: y = {round(slope,3)} * x + {round(intercept,3)}")

# Calculate Mean Squared Error
predicted_values = model.predict(weights)
mse = mean_squared_error(games_played, predicted_values)
print("Mean Squared Error:", round(mse,3))
'''moderate to high MSE indicates that the model's predictions are somewhat close to the actual values'''

from sklearn.metrics import r2_score
# Calculate R-squared/ goodness of fit
r_squared = r2_score(games_played, model.predict(weights))
print("R-squared:", round(r_squared,3))
'''low R-squared value suggests that the linear regression model may not be capturing 
much of the variability in the 'games_played' variable based on the 'weights' variable alone'''