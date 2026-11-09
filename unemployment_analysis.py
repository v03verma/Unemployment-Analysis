import pandas as pd

# Load the unemployment dataset
df = pd.read_csv("Unemployment in India.csv")

# Display first 5 rows
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Calculate total missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# Display rows where all values are missing
missing_rows = df[df.isnull().all(axis=1)]

print("\nCompletely Empty Rows:")
print(missing_rows)

print("\nTotal Empty Rows:", len(missing_rows))

# Remove completely empty rows
df = df.dropna(how="all")

# Reset the index
df = df.reset_index(drop=True)

# Check dataset after cleaning
print("\nDataset Shape After Cleaning:")
print(df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum().sum())

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Display cleaned column names
print("\nCleaned Column Names:")
print(df.columns.tolist())

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Check the data type
print("\nDate Column Data Type:")
print(df["Date"].dtype)

# Display first 5 dates
print("\nFirst 5 Dates:")
print(df["Date"].head())

# Statistical summary of numerical columns
print("\nStatistical Summary:")
print(df.describe())

# Find highest unemployment rate
highest = df.loc[df["Estimated Unemployment Rate (%)"].idxmax()]

print("\nHighest Unemployment Rate:")
print(highest[["Region", "Date", "Estimated Unemployment Rate (%)", "Area"]])

# Find lowest unemployment rate
lowest = df.loc[df["Estimated Unemployment Rate (%)"].idxmin()]

print("\nLowest Unemployment Rate:")
print(lowest[["Region", "Date", "Estimated Unemployment Rate (%)", "Area"]])

# Calculate average unemployment rate by region
region_unemployment = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean()

# Sort regions by average unemployment rate
region_unemployment = region_unemployment.sort_values(ascending=False)

print("\nAverage Unemployment Rate by Region:")
print(region_unemployment)

# Display top 5 regions
print("\nTop 5 Regions with Highest Unemployment:")
print(region_unemployment.head(5))

# Display bottom 5 regions
print("\nTop 5 Regions with Lowest Unemployment:")
print(region_unemployment.tail(5))

import matplotlib.pyplot as plt

# Top 5 regions with highest unemployment
top_5 = region_unemployment.head(5)

# Create bar chart
plt.figure(figsize=(10, 5))
top_5.plot(kind="bar", color="orange")

plt.title("Top 5 Regions with Highest Unemployment")
plt.xlabel("Region")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()

# Display graph
plt.savefig("images/top_5_regions.png", dpi=300, bbox_inches="tight")
plt.show()

# Calculate monthly average unemployment rate
monthly_unemployment = df.groupby("Date")["Estimated Unemployment Rate (%)"].mean()

# Create line graph
plt.figure(figsize=(12, 5))

monthly_unemployment.plot(kind="line", marker="o")

plt.title("Monthly Average Unemployment Rate in India")
plt.xlabel("Month")
plt.ylabel("Average Unemployment Rate (%)")

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("images/monthly_unemployment.png", dpi=300, bbox_inches="tight")
plt.show()

# Calculate pre-COVID average unemployment
pre_covid = df[df["Date"] < "2020-03-01"]

pre_covid_avg = pre_covid["Estimated Unemployment Rate (%)"].mean()

# Calculate COVID period average unemployment
covid_period = df[df["Date"] >= "2020-03-01"]

covid_avg = covid_period["Estimated Unemployment Rate (%)"].mean()


print("\nCOVID-19 Impact Analysis:")

print("Pre-COVID Average Unemployment:", round(pre_covid_avg, 2), "%")

print("COVID Period Average Unemployment:", round(covid_avg, 2), "%")

# Calculate average unemployment by area
area_unemployment = df.groupby("Area")["Estimated Unemployment Rate (%)"].mean()

print("\nRural vs Urban Unemployment:")
print(area_unemployment)

# Rural vs Urban comparison graph

plt.figure(figsize=(8, 5))

area_unemployment.plot(kind="bar", color=["green", "blue"])

plt.title("Rural vs Urban Unemployment Rate")
plt.xlabel("Area")
plt.ylabel("Average Unemployment Rate (%)")

plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("images/rural_vs_urban.png", dpi=300, bbox_inches="tight")
plt.show()