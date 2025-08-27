regression models

| Model                 | Regularization             | Notes                       |
| --------------------- | -------------------------- | --------------------------- |
| LinearRegression      | None                       | Standard OLS                |
| Ridge                 | L2                         | Prevents large coefficients |
| Lasso                 | L1                         | Feature selection           |
| ElasticNet            | L1 + L2                    | Hybrid of Ridge & Lasso     |
| BayesianRidge         | Probabilistic              | Uncertainty estimation      |
| SGDRegressor          | L1, L2, ElasticNet         | Scalable for large data     |
| Polynomial Regression | None (feature engineering) | Captures non-linear trends  |


Uses Gradidnet descent?

| Model                 | Uses Gradient Descent? | Notes                                       |
| --------------------- | ---------------------- | ------------------------------------------- |
| LinearRegression      | No                     | Analytical solution                         |
| Ridge                 | Usually no             | Can use iterative solver for large datasets |
| Lasso                 | Yes                    | Iterative (coordinate descent)              |
| ElasticNet            | Yes                    | Iterative (coordinate descent)              |
| BayesianRidge         | No                     | Bayesian posterior computation              |
| SGDRegressor          | Yes                    | Stochastic gradient descent                 |
| Polynomial Regression | Depends on base model  | Usually LinearRegression → no               |
