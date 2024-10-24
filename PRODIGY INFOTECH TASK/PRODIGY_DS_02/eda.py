import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Install required libraries (if not already installed)
# Open VS Code terminal and run: pip install pandas matplotlib seaborn

# Load the dataset
url = "train.csv"
df = pd.read_csv(url)

# Data cleaning (replace with your specific steps)
print("--- Data Cleaning ---")

# Check for missing values
print(f"Missing values: {df.isnull().sum().to_frame(name='Count')}")

# Handle missing values (consider imputation methods)
# df.fillna(..., inplace=True)  # Replace with your preferred method (e.g., mean, median)

# Explore data types
print(f"Data types:\n{df.dtypes}")

# Convert categorical columns to numerical (if applicable)
categorical_cols = [col for col in df.columns if df[col].dtype == 'object']
for col in categorical_cols:
    df[col] = pd.Categorical(df[col]).codes  # Example using category codes

# Exploratory data analysis (EDA)
print("--- Exploratory Data Analysis ---")

# Describe basic statistics
print(df.describe(include='all'))

# Visualize distributions
df['Age'].hist(bins=20)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')
plt.show()

sns.countplot(x="Sex", hue="Survived", data=df)
plt.title('Survival by Sex')
plt.show()

sns.boxplot(
    x = "Pclass",
    y = "Fare",
    showmeans=True,
    data=df
)
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.title('Fare by Passenger Class')
plt.show()

sns.heatmap(df.corr(), annot=True)
plt.title('Correlation Matrix')
plt.show()

# Explore relationships between variables (e.g., scatter plots, cross-tabulations)
sns.jointplot(x='Age', y='Fare', data=df)
plt.title('Fare vs. Age')
plt.show()

# Identify patterns and trends in the data

# (Add your analysis here, e.g., survival by passenger class, age, etc.)
# You can use visualizations, pivot tables, or group by operations