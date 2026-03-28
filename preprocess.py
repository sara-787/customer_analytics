import sys
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
import os

file_path = sys.argv[1]
df = pd.read_csv(file_path)


# descrption of the dataset
print(df.describe())
print('\n')
print(df.info())


# Removing irrelevant columns
df = df.drop(['Item Purchased', 'Promo Code Used', 'Preferred Payment Method','Color'], axis=1)

# Checking  duplicates and null values
print(f"Checking percentage of missing values ")
missing_percentage = (df.isna().sum() / len(df)) * 100
print(f"Missing values percentage:\n{missing_percentage}")


duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Removing duplicates and handling missing values
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

#Numeric columns mean imputation
df.fillna(df.mean(numeric_only=True), inplace=True)
# Categorical columns mode imputation
cols = ['Gender', 'Subscription Status', 'Discount Applied']
for col in cols:
    if col in df.columns:
        df[col].fillna(df[col].mode()[0], inplace=True)



#Encoding categorical variables
binary_cols = ['Gender', 'Subscription Status', 'Discount Applied']
for col in binary_cols:
    df[col] = LabelEncoder().fit_transform(df[col])




# Checking Outliers using IQR method for numeric columns only
cols = df.select_dtypes(include=['number']).columns
for col in cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    mask_upper = df[col] > upper
    mask_lower = df[col] < lower
    print("=" * 40)
    print(f"Column: {col}")
    print(f"Lower Bound  : {lower:.2f}")
    print(f"Upper Bound  : {upper:.2f}")
    print(f"Outliers Above Upper : {mask_upper.sum()}")
    print(f"Outliers Below Lower : {mask_lower.sum()}")

    df[col] = df[col].clip(lower, upper)

# SCALING
#scaled_cols = ['Purchase Amount (USD)', 'Review Rating', 'Previous Purchases']
#scaler = StandardScaler()
#df[scaled_cols] = scaler.fit_transform(df[scaled_cols])






if 'Purchase Amount (USD)' in df.columns:
    df['Purchase_Bin'] = pd.cut(
        df['Purchase Amount (USD)'],
        bins=3,
        labels=["Low", "Medium", "High"]
    )


df.to_csv("data_preprocessed.csv", index=False)


os.system("python analytics.py data_preprocessed.csv")