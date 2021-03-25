import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

# Data for plotting
t = np.linspace(10, 1001, 100)

# Random walk in 1D: version #1
# define the number of steps 
n = 100
  
dB_with_ships = np.zeros(n) 
dB_with_ships[0] = 100

# filling the coordinates with random variables 
for i in range(1, n): 
    val = np.random.randint(60,100)
    if val >=81: 
        dB_with_ships[i] = dB_with_ships[i - 1] - 0.75
    else: 
        dB_with_ships[i] = dB_with_ships[i - 1] + 0.25
        
dB_with_ships[7] +=4
    
dB_no_ships = np.zeros(n) 
dB_no_ships[0] = 90

# filling the coordinates with random variables 
for i in range(1, n): 
    val = np.random.randint(50,90)
    if val >=67: 
        dB_no_ships[i] = dB_no_ships[i - 1] - 0.75
    else: 
        dB_no_ships[i] = dB_no_ships[i - 1] + 0.25
        
fundamental_freq = np.array([93.25,92])
dB_no_ships[1:3] = fundamental_freq
dB_no_ships[7] +=5

# Create figure
fig, ax = plt.subplots()

# log x axis
ax.semilogx(t, dB_with_ships, label = "with ships", color = 'black')
ax.semilogx(t, dB_no_ships, label = "no ships", color = 'gray')
ax.set(ylabel='Sound Pressure Level (dB luPA^2/Hz)')
ax.set(xlabel='Frequency (Hz)')
ax.grid(axis = "both")
ax.legend(loc="lower left")

