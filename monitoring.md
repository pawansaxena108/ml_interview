| Drift Type                | Cause / Definition                  | Detection Method                          |
| ------------------------- | ----------------------------------- | ----------------------------------------- |
| Data Drift                | Feature distribution changes        | PSI, KL divergence, histograms, KS tests  |
| Concept Drift             | Feature-target relationship changes | Calibration plots, Brier score, AUC drop  |
| Population / Cohort Drift | Different borrower cohorts appear   | Vintage-level PD, PSI, cohort performance |
| Label / Target Drift      | Baseline PD changes (macro, cycle)  | Average PD vs predicted PD, recalibration |


| Drift Type       | Typical Metrics                         | Use Case              |
| ---------------- | --------------------------------------- | --------------------- |
| **Numerical**    | KS-test, Wasserstein, PSI, JSD          | Feature distributions |
| **Categorical**  | Chi-square, PSI, JSD                    | Frequency tables      |
| **Target drift** | Chi-square, KS, PSI                     | Label distribution    |
| **Model drift**  | JSD, PSI (on predictions/probabilities) | Prediction monitoring |
| **Stability**    | Missing values %, constant features     | Pipeline reliability  |
