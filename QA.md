1) Scaling tecnique

Different scalers in machine learning include **MinMaxScaler, StandardScaler, RobustScaler, and Normalizer**, each suited for specific data characteristics and modeling goals.[1][2][3]

## Types of Scalers

- **MinMaxScaler**: Scales data to a fixed range, usually. It maintains the relative distances but is sensitive to outliers, meaning extreme values compress most points into a small range. Best used when data does not contain outliers or is already bounded, such as pixel data in images.[4][2][3][1]
- **StandardScaler**: Transforms features to have mean 0 and variance 1 using z-score normalization. Suitable when data follows (or roughly follows) a normal distribution, and many algorithms like linear regression or KMeans benefit from standardized features.[2][3]
- **RobustScaler**: Uses median and interquartile range, making it robust to outliers. Ideal when data has many outliers or is skewed, and you want relative distances between most values preserved while reducing extreme influence.[3][1]
- **Normalizer**: Scales each sample (row) to unit norm (usually L2 or L1). Best for algorithms sensitive to Euclidean distances or angles between samples, such as text classification or clustering where the direction of the data points matters.[3]

## When to Use Each Scaler

| Scaler         | Use Case                                  | Outlier Sensitivity        |
|----------------|-------------------------------------------|----------------------------|
| MinMaxScaler   | Bounded, non-Gaussian data, no outliers   | High (affected by outliers)[1][2]|
| StandardScaler | Normal (Gaussian) distributed data         | Moderate (affected by outliers but less than MinMax)[2][3]|
| RobustScaler   | Data with many outliers/skewed distributions| Low (robust to outliers)[1][3]|
| Normalizer     | Row-level scaling, when direction matters  | N/A (operates per row, not feature)[3]|

## Summary Table

| Scaler         | Transformation                            | When to use                               | Algorithms That Benefit      |
|----------------|-------------------------------------------|-------------------------------------------|-----------------------------|
| MinMaxScaler   | $$\frac{X - X_{min}}{X_{max} - X_{min}}$$ | Data with fixed bounds, low outliers      | KNN, SVM, neural nets       |
| StandardScaler | $$\frac{X - \mu}{\sigma}$$                | Gaussian data, standardized features      | Linear regression, clustering|
| RobustScaler   | $$\frac{X - median}{IQR}$$                | Skewed data, presence of outliers         | Same as StandardScaler      |
| Normalizer     | $$\frac{X}{\|X\|}$$ (L2, L1 norm)         | Text or data where magnitude/direction    | Text classification, KNN    |

Choose the scaler based on data distribution, presence of outliers, and requirements of the machine learning algorithm being used.[5][1][2][3]


2) Market risk is measured using Value-at-Risk to estimate potential losses under normal conditions, while stress testing evaluates portfolio performance under extreme or crisis scenarios to capture tail risks that VaR may miss

3) | **Metric**              | **Definition**                                                                                                    | **Purpose**                                                    | **Method/Approach**                                                                                                                                                                        | **Key Points / Limitations**                                                                                                                                        |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Value-at-Risk (VaR)** | Estimates the **maximum potential loss** of a portfolio over a specified time horizon at a given confidence level | Quantifies potential losses under **normal market conditions** | - Historical Simulation: Uses past returns<br>- Variance-Covariance: Assumes normal distribution of returns<br>- Monte Carlo Simulation: Simulates random scenarios based on distributions | - Focuses on typical market conditions<br>- Does not capture extreme events or liquidity risk<br>- Often used with 95% or 99% confidence levels                     |
| **Stress Testing**      | Evaluates the **impact of extreme but plausible scenarios** on a portfolio                                        | Identifies vulnerabilities under **adverse market conditions** | - Historical Scenarios: Apply past crises (e.g., 2008 crash)<br>- Hypothetical Scenarios: Construct extreme scenarios that could happen                                                    | - Complements VaR by capturing tail risks<br>- Useful for regulatory reporting and internal risk assessment<br>- Can include market, credit, and liquidity stresses |


| **Risk Type**      | **Definition**                                                           | **Causes / Drivers**                                                                          | **Measurement / Metrics**                                                                                  | **Mitigation / Controls**                                                                                     | **Interview Notes**                                                                                       |
| ------------------ | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Credit Risk**    | Risk of loss if a borrower or counterparty fails to meet obligations     | Default on loans, bonds, derivatives; counterparty failure                                    | - Probability of Default (PD)<br>- Loss Given Default (LGD)<br>- Exposure at Default (EAD)<br>- Credit VaR | - Credit limits & approval processes<br>- Collateral & guarantees<br>- Diversification of counterparties      | *“Credit risk is about counterparty default and the potential financial loss if obligations aren’t met.”* |
| **Market Risk**    | Risk of losses due to changes in market prices or rates                  | Interest rate changes, stock price volatility, currency fluctuations, commodity price changes | - Value-at-Risk (VaR)<br>- Stress Testing / Scenario Analysis<br>- Sensitivity analysis (Delta, Beta)      | - Hedging with derivatives<br>- Position limits & diversification<br>- Continuous monitoring & risk reporting | *“Market risk is about potential losses from market movements, measured with VaR and stress testing.”*    |
| **Liquidity Risk** | Risk of being unable to meet short-term obligations without large losses | Inability to sell assets quickly, funding shortages                                           | - Liquidity Coverage Ratio (LCR)<br>- Net Stable Funding Ratio (NSFR)<br>- Cash flow forecasts             | - Maintain cash buffers<br>- Contingency funding plans<br>- Diversify funding sources                         | *“Liquidity risk is about not having enough cash or marketable assets to meet obligations promptly.”*     |
