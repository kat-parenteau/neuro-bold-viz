import pandas as pd
import numpy as np

np.random.seed(0)
time = np.arange(0, 60, 2)

def simulate_bold(base=0.2, task_start=20, task_end=40):
    signal = base + np.random.normal(0, 0.01, len(time))
    task_effect = (time >= task_start) & (time <= task_end)
    signal[task_effect] += 0.05 
    return signal

df = pd.DataFrame({
    "Time (s)": time,
    "Premotor Cortex": simulate_bold(),
    "Supplementary Motor Areas": simulate_bold(base=0.25),
    "Posterior Parietal Cortex": simulate_bold(base=0.22),
})

df.to_csv("bold_data_BCI_motor.csv", index=False)