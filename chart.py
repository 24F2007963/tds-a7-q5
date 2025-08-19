import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
months = pd.date_range(start="2023-01", periods=12, freq="M")
segments = ["Retail", "Wholesale", "Online"]
data = {
    "Month": np.tile(months, len(segments)),
    "Segment": np.repeat(segments, len(months)),
    "Revenue": np.random.randint(80, 200, len(months) * len(segments))
}
df = pd.DataFrame(data)

# Professional styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create fixed 512x512 output
fig, ax = plt.subplots(figsize=(8, 8), dpi=64)  # 8*64 = 512 pixels

sns.lineplot(data=df, x="Month", y="Revenue", hue="Segment", marker="o", ax=ax)
ax.set_title("Monthly Revenue Trends by Segment", fontsize=16)
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (in $K)")

# Save WITHOUT bbox_inches to keep 512x512
plt.savefig("chart.png", dpi=64)
plt.close()
