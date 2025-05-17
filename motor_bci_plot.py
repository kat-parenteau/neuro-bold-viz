import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bold_data_BCI_motor.csv")


time = df["Time (s)"]

plt.figure(figsize=(10, 6))

for col in df.columns:
    if col != "Time (s)":
        plt.plot(time, df[col], label=col)

plt.axvspan(15, 35, color='lightgreen', alpha=0.3, label="Mock Task")

plt.xlabel("Time (s)")
plt.ylabel("BOLD Signal Amplitude")
plt.title("Simulated BOLD Activity During BCI-Controlled Prosthetic Arm Task")
plt.legend()
plt.grid(True)

plt.show()