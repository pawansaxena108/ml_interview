from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve

# Generate binary classification data
X, y = make_classification(n_samples=1000, n_classes=2, random_state=42)
trainX, testX, trainy, testy = train_test_split(X, y, test_size=0.5, random_state=42)

# Train base classifier (SVM, no calibration)
base_model = SVC(probability=True, random_state=42)
base_model.fit(trainX, trainy)

# Predict raw probabilities
probs_uncalibrated = base_model.predict_proba(testX)[:, 1]

# Calibrate with Platt Scaling (sigmoid)
platt_model = CalibratedClassifierCV(base_model, method='sigmoid', cv=5)
platt_model.fit(trainX, trainy)
probs_platt = platt_model.predict_proba(testX)[:, 1]

# Calibrate with Isotonic Regression
iso_model = CalibratedClassifierCV(base_model, method='isotonic', cv=5)
iso_model.fit(trainX, trainy)
probs_iso = iso_model.predict_proba(testX)[:, 1]

# Plot calibration curves
plt.plot([0,1],[0,1],'k--')
for prob, label in zip([probs_uncalibrated, probs_platt, probs_iso],
                       ['Uncalibrated', 'Platt Scaling', 'Isotonic Regression']):
    fraction_of_positives, mean_predicted_value = calibration_curve(testy, prob, n_bins=10)
    plt.plot(mean_predicted_value, fraction_of_positives, marker='.', label=label)

plt.xlabel('Mean Predicted Probability')
plt.ylabel('Fraction of Positives')
plt.legend()
plt.title('Calibration Curves for SVM')
plt.show()
