import numpy as np

temperature = np.array([28, 31, 29, 33, 35, 30, 32])

print("Temperatures:", temperature)

print("Average temperature:", np.mean(temperature))
print("Highest temperature:", np.max(temperature))
print("Lowest temperature:", np.min(temperature))

print("Temperatures above 30°C:", temperature[temperature > 30])

updated_temperature = temperature + 2

print("Updated temperatures:", updated_temperature)