import sys
import pandas as pd
import numpy as np
import os

file_path = sys.argv[1]
df = pd.read_csv(file_path)


# Insight 1: Top Category by Total Revenue

if 'Purchase Amount (USD)' in df.columns:
    revenue_by_category = df.groupby('Category')['Purchase Amount (USD)'].sum()
    top_category_revenue = revenue_by_category.idxmax()
    top_category_value = revenue_by_category.max()

    with open("insight1.txt", "w") as f:
        f.write(f"Category generating highest total revenue: {top_category_revenue} (${top_category_value:.2f})\n")


# Insight 2: Average Purchase Amount by Gender

if 'Gender' in df.columns and 'Purchase Amount (USD)' in df.columns:
    avg_purchase_gender = df.groupby('Gender')['Purchase Amount (USD)'].mean()
    with open("insight2.txt", "w") as f:
        f.write("Average purchase amount by gender:\n")
        for gender, amount in avg_purchase_gender.items():
            f.write(f"{gender}: ${amount:.2f}\n")


# Insight 3: High-Value Customers (Top 10% by Purchase Amount)

if 'Customer ID' in df.columns and 'Purchase Amount (USD)' in df.columns:
    threshold = np.percentile(df['Purchase Amount (USD)'], 90)
    top_customers = df[df['Purchase Amount (USD)'] >= threshold]['Customer ID'].nunique()
    with open("insight3.txt", "w") as f:
        f.write(f"Number of high-value customers (top 10% of purchases): {top_customers}\n")

# Insight 4: Most Preferred Payment Method
if 'Payment Method' in df.columns:
    most_used_payment = df['Payment Method'].value_counts().idxmax()
    count_payment = df['Payment Method'].value_counts().max()
    insight4 = f"The most preferred payment method is '{most_used_payment}' with {count_payment} purchases."
    
    with open("insight4.txt", "w") as f:
        f.write(insight4)


# Insight 5: Top 3 Shipping Methods
if 'Shipping Type' in df.columns:
    top_shipping = df['Shipping Type'].value_counts().head(3)
    with open("insight5.txt", "w") as f:
        f.write("Top 3 shipping methods:\n")
        for method, count in top_shipping.items():
            f.write(f"{method}: {count} shipments\n")


# Insight 6: Top Purchased Category by Gender
if 'Gender' in df.columns and 'Category' in df.columns:
    top_by_gender = df.groupby('Gender')['Category'] \
                      .agg(lambda x: x.value_counts().idxmax())
    with open("insight6.txt", "w") as f:
        f.write("Top purchased category by gender:\n")
        for gender, category in top_by_gender.items():
            gender_name = "Female" if gender == 0 else "Male"
            f.write(f"{gender_name}: {category}\n")

os.system("python visualize.py data_preprocessed.csv")