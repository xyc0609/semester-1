import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
print(len(data))
# Find the mean average GPA of the students
print(data['GPA'].mean())
# Find the standard deviation of how much sleep students get per day
print(data['Sleep_Hours'].std())
# Find the maximum amount of study hours per day
print(data['Study_Hours'].max())
# Sort the students by social hours per day ascending (lowest -> highest)
print(data.sort_values('Social_Hours'), ascending=True)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
data['Total_hours'] = data['Sleep_Hours'] + data['Study_Hours'] + data['Social_Hours']

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
high_stress = data[data['Stress_Level'] == 'high']
low_stress = data[data['Stress_Level'] == 'low']

print("High stress students:")
print(high_stress['GPA'].mean())

print("Low stress students:")
print(low_stress['GPA'].mean())