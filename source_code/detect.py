import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import joblib
import matplotlib.pyplot as plt

# 1. Load the System
print("[*] Loading System Modules...")
model = load_model("nids_autoencoder.keras")
scaler = joblib.load("scaler.save") # CRITICAL: Use the SAME scaler from training
print("[*] AI Brain & Scaler Loaded.")

# 2. Load the Attack Data (Wednesday)
print("[*] Loading Test Traffic (Wednesday)...")
df_test = pd.read_csv("test_data.csv")

# 3. Preprocess (Normalize)
# Note: We use .transform(), NOT .fit_transform(). 
# We treat this data exactly like the training data.
x_test = scaler.transform(df_test.values)

# 4. The Detection Loop
print("[*] Running Inference...")
reconstructions = model.predict(x_test)

# Calculate MSE (Mean Squared Error) for each specific row
# Formula: (Input - Output)^2
mse = np.mean(np.power(x_test - reconstructions, 2), axis=1)

# 5. The Threshold Logic
# In a real system, we calculate this dynamically. 
# For this demo, anything with error > 0.05 is suspicious.
THRESHOLD = 0.05 

anomalies = mse > THRESHOLD
num_anomalies = np.sum(anomalies)

print(f"\n[REPORT] Analysis Complete.")
print(f"Total Flows Scanned: {len(df_test)}")
print(f"Anomalies Detected:  {num_anomalies}")
print(f"Attack Ratio:        {num_anomalies / len(df_test) * 100:.2f}%")


# 6. Visualization (Professional Engineering Grade)
plt.figure(figsize=(12, 7))

# Plot all points as small blue dots first
plt.scatter(range(len(mse)), mse, s=15, color="blue", alpha=0.4, label="Normal Traffic")

# Overlay the Anomalies as red dots
# This makes the attacks pop out visually
attack_indices = np.where(anomalies)[0]
attack_errors = mse[anomalies]
plt.scatter(attack_indices, attack_errors, s=20, color="red", label="DoS Attack Detected")

# Draw the Threshold Line
plt.axhline(y=THRESHOLD, color='black', linestyle='--', linewidth=2, label=f"Threshold ({THRESHOLD})")

# THE FIX: Logarithmic Scale
# This expands the bottom of the graph so you can see the 'normal' noise
plt.yscale('log') 

plt.title("NIDS Detection Analysis (Log Scale)", fontsize=14)
plt.xlabel("Flow Sequence (Time Order)", fontsize=12)
plt.ylabel("Reconstruction Error (MSE) - Log Scale", fontsize=12)
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.2) # Adds a subtle grid for precision

# Save it as a high-res image for your report
plt.savefig("Final_Detection_Graph.png", dpi=300)
plt.show()


# 7. Save the attackers to a file
if num_anomalies > 0:
    attack_df = df_test[anomalies]
    attack_df.to_csv("detected_attacks.csv", index=False)
    print(f"[*] Details of {num_anomalies} attacks saved to 'detected_attacks.csv'")