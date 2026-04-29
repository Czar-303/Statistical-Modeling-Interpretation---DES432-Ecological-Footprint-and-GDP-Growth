import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import statsmodels.api as sm
from scipy import stats
#imports

df = pd.read_csv("EF_GDP(constant2010USD).csv")

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (8, 5)

# Quick check
print(df.head())
print(df.info())

# Keep only relevant columns
df = df[['Country', 'EFDelta', 'GDPDelta', 'GDP2009']]

# Convert to numeric (VERY IMPORTANT)
df['EFDelta'] = pd.to_numeric(df['EFDelta'], errors='coerce')
df['GDPDelta'] = pd.to_numeric(df['GDPDelta'], errors='coerce')
df['GDP2009'] = pd.to_numeric(df['GDP2009'], errors='coerce')

# Drop missing values
df = df.dropna()

# Histogram (GDP growth)
plt.figure()
sns.histplot(df['GDPDelta'], bins=20, kde=True)
plt.title("Distribution of GDP Growth (GDPDelta)", fontsize=13)
plt.xlabel("GDP Growth")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
# Scatterplot (main relationship)
plt.figure()
sns.scatterplot(data=df, x='EFDelta', y='GDPDelta', alpha=0.7)
plt.title("EFDelta vs GDPDelta", fontsize=13)
plt.xlabel("Change in Ecological Footprint")
plt.ylabel("GDP Growth")
plt.tight_layout()
plt.show()

# Pearson correlation test
corr, p_value = stats.pearsonr(df['EFDelta'], df['GDPDelta'])

print("Correlation:", corr)
print("p-value:", p_value)

# Multiple Linear Regression
plt.figure()

sns.regplot(
    data=df,
    x='EFDelta',
    y='GDPDelta',
    scatter_kws={'alpha':0.6},
    line_kws={'linewidth':2}
)

plt.text(
    0.05, 0.95,
    f"r = {corr:.2f}\np = {p_value:.4f}",
    transform=plt.gca().transAxes,
    verticalalignment='top'
)

plt.title("Regression: EFDelta vs GDPDelta", fontsize=13)
plt.xlabel("EFDelta")
plt.ylabel("GDPDelta")
plt.tight_layout()
plt.show()

# Multiple Linear Regression
X = df[['EFDelta', 'GDP2009']]
y = df['GDPDelta']

X = sm.add_constant(X)

model_multi = sm.OLS(y, X).fit()

print(model_multi.summary())

# Get predictions & residuals
predictions = model_multi.predict(X)
residuals = y - predictions

# Residual plot
plt.figure()
sns.scatterplot(x=predictions, y=residuals, alpha=0.7)
plt.axhline(y=0, linestyle='--')
plt.title("Residual Plot", fontsize=13)
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.tight_layout()
plt.show()

df[['EFDelta','GDPDelta']].describe()
