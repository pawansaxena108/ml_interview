'''import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Monte Carlo Simulation: Online Store Revenue
# -------------------------------

# Parameters
n_customers = 1000       # number of customers
p_buy = 0.3              # probability a customer makes a purchase
n_sims = 10000           # number of Monte Carlo simulations

# Simulate purchases: lognormal distribution (like spending data)
mu, sigma = 3.5, 0.7     # mean and stddev of log spending

total_revenues = []

for _ in range(n_sims):
    # Each customer decides to buy (1) or not (0)
    buys = np.random.binomial(1, p_buy, size=n_customers)
    
    # Revenue if they buy (lognormal distributed amounts)
    revenues = buys * np.random.lognormal(mean=mu, sigma=sigma, size=n_customers)
    
    # Total revenue for this simulation
    total_revenues.append(revenues.sum())

total_revenues = np.array(total_revenues)

# -------------------------------
# Results
# -------------------------------`
mean_rev = np.mean(total_revenues)
std_rev = np.std(total_revenues)
ci_lower, ci_upper = np.percentile(total_revenues, [2.5, 97.5])

print(f"Estimated Revenue Distribution (Monte Carlo, {n_sims} sims):")
print(f"Mean Revenue     : {mean_rev:,.2f}")
print(f"Std Deviation    : {std_rev:,.2f}")
print(f"95% CI for Total : ({ci_lower:,.2f}, {ci_upper:,.2f})")

# -------------------------------
# Visualization
# -------------------------------
plt.figure(figsize=(8,5))
plt.hist(total_revenues, bins=50, color="skyblue", edgecolor="black", alpha=0.7)
plt.axvline(mean_rev, color="red", linestyle="--", label=f"Mean = {mean_rev:,.0f}")
plt.axvline(ci_lower, color="green", linestyle="--", label=f"95% CI lower = {ci_lower:,.0f}")
plt.axvline(ci_upper, color="green", linestyle="--", label=f"95% CI upper = {ci_upper:,.0f}")
plt.title("Monte Carlo Simulation of Total Revenue (Online Store)")
plt.xlabel("Total Revenue")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
'''


🔎 What this does
Generates 10,000 possible business outcomes (revenue totals).
Gives you the expected revenue and uncertainty range.
Plots the distribution so you can see how likely different revenue levels are.

