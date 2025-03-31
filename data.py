import pandas as pd
import matplotlib.pyplot as plt

# grab the movie data from csv file
df = pd.read_csv("movies.csv")

# Clean up non-numeric values in 'Income'
df['Income'] = pd.to_numeric(df['Income'], errors='coerce')

# Sort movies by income in descending order
df = df.sort_values(by="Income", ascending=False)

# Print data
print(df)

# Bar Chart
plt.figure(figsize=(10,5))
plt.bar(df["Movies"], df["Income"], color='tomato')
plt.xticks(rotation=45, ha='right')
plt.xlabel("Pixar Movies")
plt.ylabel("Income (in Millions)")
plt.title("Income of Pixar Movies with Highest Ranking By Tomatometer")
plt.show()

# Pie chart
def format_label(pct, all_vals):
    absolute = int(round(pct/100. * sum(all_vals)))
    return f"{pct:.1f}%\n(${absolute}M)"

plt.figure(figsize=(8, 8))
plt.pie(
    df["Income"], 
    labels=df["Movies"], 
    autopct=lambda pct: format_label(pct, df["Income"]),
    startangle=140, 
    colors=plt.cm.Paired.colors
)
plt.title("Income of Pixar Movies with Highest Ranking By Tomatometer")
plt.show()