import numpy as np
import pandas as pd

# Parameters
players = ["CR7", "Messi", "Mbappe", "Osihmen"]
n_points = 500
pitch_length, pitch_width = 105, 68

# Generate synthetic touch‐point data
rows = []
rng = np.random.default_rng(42)
for p in players:
    # Example: different players favor different thirds
    if p == "CR9":
        xs = rng.normal(loc=pitch_length*0.25, scale=10, size=n_points)
        ys = rng.normal(loc=pitch_width*0.50,  scale=15, size=n_points)
    elif p == "Messi":
        xs = rng.normal(loc=pitch_length*0.75, scale=12, size=n_points)
        ys = rng.normal(loc=pitch_width*0.30,  scale=10, size=n_points)
    elif p == "Mbappe":
        xs = rng.normal(loc=pitch_length*0.10, scale=20, size=n_points)
        ys = rng.normal(loc=pitch_width*0.20,  scale=10, size=n_points)
    else:  # Osihmen 
        xs = rng.uniform(0, pitch_length, size=n_points)
        ys = rng.uniform(0, pitch_width,  size=n_points)
    for x, y in zip(xs, ys):
        rows.append({"player": p, "x": np.clip(x, 0, pitch_length), "y": np.clip(y, 0, pitch_width)})

df = pd.DataFrame(rows)
df.to_csv("player_positions2.csv", index=False)
print("Saved synthetic dataset to player_positions2.csv")
