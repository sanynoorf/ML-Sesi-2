import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

pendapatan_rata_rata = np.array([5, 10, 20, 8, 4, 6, 12, 15])
penjualan_pizza = np.array([27, 46, 73, 40, 30, 28, 46, 59])

plt.scatter(pendapatan_rata_rata, penjualan_pizza)
plt.title('Scatter Diagram Pendapatan Rata-Rata vs Penjualan Pizza')
plt.xlabel('Pendapatan Rata-Rata (1000$)')
plt.ylabel('Penjualan Pizza (1000 Buah)')

correlation_coefficient = np.corrcoef(pendapatan_rata_rata, penjualan_pizza)[0,1]
print(f"Korelasi antara pendapatan rata-rata dan penjualan pizza: {correlation_coefficient}")

slope, intercept, r_value, p_value, std_err = linregress(pendapatan_rata_rata, penjualan_pizza)

predicted_values = slope * pendapatan_rata_rata + intercept
SSR = np.sum((predicted_values - np.mean(penjualan_pizza))**2)
SSE = np.sum((penjualan_pizza - predicted_values)**2)
SST = SSR + SSE
R_squareed = SSR / SST

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"SSR (Sum of Squares Regression): {SSR}")
print(f"SST (Sum of Squares Error): {SSE}")
print(f"SST (Total Sum of Squares): {SST}")
print(f"R-squared: {R_squareed}")

plt.show()