import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    "Age": [18, 19, 20, 21, 22, 23, 24],
    "Marks": [65, 70, 72, 78, 85, 88, 90]
}

df = pd.DataFrame(data)

# Line Plot
plt.figure()
plt.plot(df["Age"], df["Marks"])
plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Line Plot: Age vs Marks")
plt.show()

# Bar Chart
plt.figure()
plt.bar(df["Age"], df["Marks"])
plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Bar Chart: Age vs Marks")
plt.show()

# Histogram
plt.figure()
plt.hist(df["Marks"])
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram of Marks")
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(df["Age"], df["Marks"])
plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Scatter Plot: Age vs Marks")
plt.show()

# Seaborn Heatmap
plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Heatmap of Correlation")
plt.show()

# Seaborn Pairplot
sns.pairplot(df)
plt.show()