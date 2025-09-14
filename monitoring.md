| Drift Type                | Cause / Definition                  | Detection Method                          |
| ------------------------- | ----------------------------------- | ----------------------------------------- |
| Data Drift                | Feature distribution changes        | PSI, KL divergence, histograms, KS tests  |
| Concept Drift             | Feature-target relationship changes | Calibration plots, Brier score, AUC drop  |
| Population / Cohort Drift | Different borrower cohorts appear   | Vintage-level PD, PSI, cohort performance |
| Label / Target Drift      | Baseline PD changes (macro, cycle)  | Average PD vs predicted PD, recalibration |
