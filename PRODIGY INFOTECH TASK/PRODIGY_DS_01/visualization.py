import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Choose a categorical or continuous variable (e.g., petal length)
variable = "petal length (cm)"

# Create a bar chart (for categorical) or histogram (for continuous)
if isinstance(df[variable].dtype, pd.CategoricalDtype):
    df[variable].value_counts().plot(kind="bar")
else:
    df[variable].plot.hist(bins=10)  # Adjust the number of bins as needed

plt.xlabel(variable)
plt.ylabel("Frequency")
plt.title(f"Distribution of {variable} in Iris Dataset")
plt.show()
