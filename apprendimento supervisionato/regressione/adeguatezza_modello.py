
#### Esempio in Python

import numpy as np

# Dati: superfici in metri quadrati (x) e prezzi corrispondenti (y)
x = np.array([50, 80, 100, 150])  # Superfici
y = np.array([150000, 200000, 250000, 350000])  # Prezzi

# Calcolo delle medie
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calcolo del coefficiente angolare (m) e dell'intercetta (b)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
m = numerator / denominator
b = y_mean - m * x_mean

# Predizioni del modello
y_pred = m * x + b
print(f"Predizioni: {y_pred}")

# Calcolo di SS_res e SS_tot
#somma dei quadrati delle differenze tra i valori osservati e quelli previsti
ss_res = np.sum((y - y_pred) ** 2)
#somma dei quadrati delle differenze tra i valori osservati e la loro media
ss_tot = np.sum((y - y_mean) ** 2)

# Calcolo di R²
r2 = 1 - (ss_res / ss_tot)

# Stampa del risultato
print(f"R²: {r2:.2f}")