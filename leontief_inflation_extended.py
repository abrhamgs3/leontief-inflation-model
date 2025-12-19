# Leontief inflation model with an added Energy sector and visual inflation plot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Define sectors
# -----------------------------
sectors = ["Agriculture", "Manufacturing", "Energy"]

# -----------------------------
# 2. Technology matrix A
# Rows = input sectors, Columns = output sectors
# -----------------------------
A = np.array([
    [0.3, 0.1, 0.2],  # Agriculture inputs
    [0.2, 0.4, 0.2],  # Manufacturing inputs
    [0.1, 0.2, 0.3]   # Energy inputs
])

# -----------------------------
# 3. Value added (baseline)
# -----------------------------
v_baseline = np.array([
    10,  # Agriculture
    20,  # Manufacturing
    15   # Energy
])

# -----------------------------
# 4. Price solver
# -----------------------------
def solve_prices(A, v):
    I = np.eye(A.shape[0])
    multiplier = np.linalg.inv(I - A.T)
    prices = multiplier @ v
    return prices, multiplier

# -----------------------------
# 5. Baseline prices
# -----------------------------
p_baseline, multiplier = solve_prices(A, v_baseline)

# -----------------------------
# 6. Energy wage shock
# -----------------------------
v_shock = np.array([
    10,  # Agriculture unchanged
    20,  # Manufacturing unchanged
    30   # Energy wage shock
])

p_shock, _ = solve_prices(A, v_shock)

# -----------------------------
# 7. Inflation table
# -----------------------------
df = pd.DataFrame({
    "Sector": sectors,
    "Price Before": p_baseline,
    "Price After": p_shock,
    "Inflation": p_shock - p_baseline
})

df
