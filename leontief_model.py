import numpy as np
import pandas as pd


# define a technology matrix for the Leontief model

A = np.array([
    [0.4, 0.1],
    [0.2, 0.3]
])

#Economic meaning

## Columns = industries being produced

## Rows = inputs used

## This is the structure of the economy

# 2. define value added vector

v_baseline = np.array([
    10,  # Agriculture
    20   # Manufacturing
])
## This is income per unit of output.

# 3. Price solver funtion using Leontief inverse
def solve_prices(A, v):
    """
    Solves p = (I - A.T)^(-1) v
    """
    I = np.eye(A.shape[0])
    price_multiplier = np.linalg.inv(I - A.T)
    p = price_multiplier @ v
    return p, price_multiplier


# Feynman explanation

## I - A.T = net value creation

### inverse = how costs ripple backward

### @ = matrix multiplication (economic transmission)

# 4. Solve baseline prices
p_baseline, price_multiplier = solve_prices(A, v_baseline)

# 5. Put results into a table

sectors = ["Agriculture", "Manufacturing"]

df_baseline = pd.DataFrame({
    "Sector": sectors,
    "Price": p_baseline
})

print("Baseline Prices")
print(df_baseline)

# PART 2 — Wage Shock Experiment

## Introduce a manufacturing wage shock
v_shock = np.array([
    10,  # Agriculture unchanged
    30   # Manufacturing wage increase
])

## Solve new prices

p_shock, _ = solve_prices(A, v_shock)

## compare prices
df_comparison = pd.DataFrame({
    "Sector": sectors,
    "Price Before": p_baseline,
    "Price After": p_shock,
    "Inflation": p_shock - p_baseline
})

print("\nWage Shock Impact")
print(df_comparison)

## This shows how a wage shock in manufacturing affects prices across the economy.

# Interpret the Multiplier
### the price propagation matrix

df_multiplier = pd.DataFrame(
    price_multiplier,
    columns=sectors,
    index=sectors
)

print("\nPrice Propagation Matrix")
print(df_multiplier)

## read it

### Columns = where the shock starts

#### Rows = where inflation ends up