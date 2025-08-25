import numpy as np
from sklearn.calibration import CalibratedClassifierCV, calibration_curve
from sklearn.linear_model import LogisticRegression
from sklearn.isotonic import IsotonicRegression
import matplotlib.pyplot as plt

# Suppose these are raw predicted probabilities from your neural network on validation data
# For binary classification: preds_uncalibrated shape: (num_samples,)
# True binary labels for calibration data:
preds_uncalibrated = np.array([...])  # neural network probability outputs for positive class
true_labels = np.array([...])         # true labels (0 or 1)

# Platt Scaling (sigmoid calibration) with logistic regression model on the validation set
platt_model = LogisticRegression()
platt_model.fit(preds_uncalibrated.reshape(-1, 1), true_labels)

# Calibrated probabilities from Platt Scaling
probs_platt = platt_model.predict_proba(preds_uncalibrated.reshape(-1, 1))[:, 1]

# Isotonic Regression calibration
iso_model = IsotonicRegression(out_of_bounds='clip')
iso_model.fit(preds_uncalibrated, true_labels)

# Calibrated probabilities from Isotonic Regression
probs_iso = iso_model.predict(preds_uncalibrated)

# Plot calibration curves to compare
plt.plot([0, 1], [0, 1], "k--")

for probs, label in zip([preds_uncalibrated, probs_platt, probs_iso],
                        ["Uncalibrated", "Platt Scaling", "Isotonic Regression"]):
    frac_pos, mean_pred = calibration_curve(true_labels, probs, n_bins=10)
    plt.plot(mean_pred, frac_pos, marker='.', label=label)

plt.xlabel("Mean Predicted Probability")
plt.ylabel("Fraction of Positives")
plt.legend()
plt.title("Calibration Curves - Neural Network Post-Hoc Calibration")
plt.show()
