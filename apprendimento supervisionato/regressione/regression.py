import numpy as np
import matplotlib.pyplot as plt

# Dati: superfici in metri quadrati (x) e prezzi corrispondenti (y)
x = np.array([50, 80, 100, 150])  # Superfici
y = np.array([150000, 200000, 250000, 350000])  # Prezzi

# Calcolo delle medie
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calcolo del coefficiente angolare (m)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
m = numerator / denominator

# Calcolo dell'intercetta (b)
b = y_mean - m * x_mean

# Stampa dei risultati
print(f"Coefficiente angolare (m): {m}")
print(f"Intercetta (b): {b}")
print(f"Equazione della retta: Y = {m:.2f}x + {b:.2f}")

# Visualizzazione dei dati e della retta
plt.scatter(x, y, color='blue', label='Dati originali')  # Dati originali
plt.plot(x, m * x + b, color='red', label=f'Retta: Y = {m:.2f}x + {b:.2f}')  # Retta di regressione
plt.xlabel('Superficie (m²)')
plt.ylabel('Prezzo (€)')
plt.title('Regressione Lineare - Superficie vs Prezzo')
plt.legend()
plt.grid()
plt.show()