import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = sys.argv[1]
df = pd.read_csv(file_path)

plt.figure(figsize=(16,12))


# Plot 1: Purchase Amount Distribution (Histogram)

plt.subplot(2,2,1)
sns.histplot(df['Purchase Amount (USD)'], bins=30, kde=True, color='skyblue')
plt.title("Distribution of Purchase Amounts")
plt.xlabel("Purchase Amount (USD)")
plt.ylabel("Frequency")


# Plot 2: Gender vs Average Purchase (Bar Plot)

plt.subplot(2,2,2)
avg_purchase_gender = df.groupby('Gender')['Purchase Amount (USD)'].mean().reset_index()
sns.barplot(x='Gender', y='Purchase Amount (USD)', data=avg_purchase_gender, palette='pastel')
plt.title("Average Purchase Amount by Gender")
plt.ylabel("Average Purchase Amount (USD)")


# Plot 3: Category vs Total Revenue (Bar Plot)

plt.subplot(2,2,3)
revenue_by_category = df.groupby('Category')['Purchase Amount (USD)'].sum().sort_values(ascending=False).reset_index()
sns.barplot(x='Purchase Amount (USD)', y='Category', data=revenue_by_category, palette='viridis')
plt.title("Total Revenue by Category")
plt.xlabel("Total Revenue (USD)")
plt.ylabel("Category")


# Plot 4: Correlation Heatmap

plt.subplot(2,2,4)
numeric_df = df.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Between Numeric Features")




plt.tight_layout()
plt.savefig("summary_plot.png", dpi=300)





os.system("python cluster.py data_preprocessed.csv")