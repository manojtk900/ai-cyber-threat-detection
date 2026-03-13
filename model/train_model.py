import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from utils.preprocess import load_data

# load dataset
X, y = load_data("dataset/Friday-WorkingHours-Afternoon-DDoS.pcap_ISCX.csv")

# split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train model
model = RandomForestClassifier(n_estimators=100)

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Model Accuracy:", accuracy)

# save model
pickle.dump(model, open("model.pkl", "wb"))