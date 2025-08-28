Scaling tecnique

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
