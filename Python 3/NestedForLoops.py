# Code Checkpoint

# rows = 3
# pets = ["dog", "cat", "fish", "turtle", "alien"]

# #Iteration between each element of the words in the list

# thing = [[j for j in pets] for i in range(rows)]
# print(thing)

# ---------------------------------------------------------

# Challenge 1

# mylist = [1, 2, 3, 4, 5]
# user = int(input("How many rows do u want"))
# rows = user

# #I'm the goat

# thing = [[i * rows for i in mylist] for j in range(rows)]
# print(thing)

# ---------------------------------------------------------

# # Challenge 2

# weather_conditions = input("Input a list of weather: ").split()

# wind_speeds = ["windy", "breezy", "calm"]

# weather_wind_speeds = []
# for weather in weather_conditions:
#     row = [weather + ' ' + wind for wind in wind_speeds]
#     weather_wind_speeds.append(row)

# print(weather_wind_speeds)
