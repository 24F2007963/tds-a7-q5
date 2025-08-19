# chart.py
# Author: Smriti Rani
# Email: 24f2007963@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Generate synthetic seasonal revenue data
np.random.seed(42)
months = pd.date_range("2024-01-01", "2024-12-31", freq="M").strftime("%b")
segments = ["Premium", "Standard", "Budget"]

data = []
for seg in segments:
    base = np.linspace(100, 200, len(months))  # growth trend
    seasonal = 20 * np.sin(np.linspace(0, 3 * np.pi, len(months)))  # seasonality
    noise = np.random.normal(0, 10, len(months))  # random fluctuations
    revenue = base + seasonal + noise + np.random.randint(50, 150)
    data.extend(zip(months, [seg]*len(months), revenue))

df = pd.DataFrame(data, columns=["Month", "Segment", "Revenue"])

# 2. Set Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# 3. Create lineplot
plt.figure(figsize=(8, 8))  # ensures 512x512 pixels with dpi=64
sns.lineplot(data=df, x="Month", y="Revenue", hue="Segment", marker="o", palette="deep")

# 4. Customize chart
plt.title("Monthly Revenue Trends by Customer Segment", fontsize=16, weight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue (in $1000s)")
plt.xticks(rotation=45)

# 5. Save chart
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
