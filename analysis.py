import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")

# ---------------------------------------------------------
# 1. Load and Clean User Logs (50,000 users)
# ---------------------------------------------------------
# Simulated dataset structure matching your project description
np.random.seed(42)
n_users = 50000

df = pd.DataFrame({
    'user_id': np.arange(1, n_users + 1),
    'completed_onboarding': np.random.choice([0, 1], size=n_users, p=[0.4, 0.6]),
    'support_tickets': np.random.poisson(lam=1.5, size=n_users),
    'feature_usage_count': np.random.randint(1, 100, size=n_users)
})

# Simulate Month 3 churn probability (higher risk for incomplete onboarding)
base_churn_prob = 0.15
df['churn_prob'] = np.where(
    df['completed_onboarding'] == 0, 
    base_churn_prob * 1.82,  # 82% higher probability
    base_churn_prob
)
df['churned_month_3'] = np.random.binomial(1, df['churn_prob'])

# ---------------------------------------------------------
# 2. Key Insight Calculation (Quantifying Month 3 Risk)
# ---------------------------------------------------------
churn_summary = df.groupby('completed_onboarding')['churned_month_3'].mean() * 100
prob_incomplete = churn_summary[0]
prob_complete = churn_summary[1]

relative_increase = ((prob_incomplete - prob_complete) / prob_complete) * 100

print(f"Churn Rate (Completed Onboarding): {prob_complete:.2f}%")
print(f"Churn Rate (Incomplete Onboarding): {prob_incomplete:.2f}%")
print(f"Calculated Probability Increase: {relative_increase:.1f}%")

# ---------------------------------------------------------
# 3. Visualization: Churn Probability by Onboarding & Tickets
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
ax = sns.barplot(
    data=df, 
    x='completed_onboarding', 
    y='churned_month_3', 
    palette=['#e74c3c', '#2ecc71'],
    ci=None
)

plt.title('Month 3 Churn Rate by Onboarding Checklist Status', fontsize=14, fontweight='bold')
plt.xlabel('Completed Initial Onboarding Checklist', fontsize=12)
plt.ylabel('Churn Rate at Month 3 (%)', fontsize=12)
plt.xticks([0, 1], ['No (Incomplete)', 'Yes (Completed)'])

# Format percentage labels on top of bars
for bar in ax.patches:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('month_3_churn_analysis.png', dpi=300)
plt.show()
