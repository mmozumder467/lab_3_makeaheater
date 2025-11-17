import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


FILE_NAME = 'lab_heater_data2.csv' 


TIME_START_MS = 18000
TIME_END_MS = 25000


def cooling_func(t, a, b, c):
    return a + b * np.exp(-t / c)


try:
   
    data = pd.read_csv(FILE_NAME)
    time_col = data.columns[0]
    therm_col = data.columns[2]

    
    cooling_data = data[
        (data[time_col] >= TIME_START_MS) & 
        (data[time_col] <= TIME_END_MS)
    ].copy() # Use .copy() to avoid a common warning

    if cooling_data.empty:
        print(f"Error: No data found between {TIME_START_MS}ms and {TIME_END_MS}ms.")
        print("Please check your TIME_START_MS and TIME_END_MS variables.")
    else:
        print(f"Successfully isolated {len(cooling_data)} data points for fitting.")

     
        x_data = cooling_data[time_col] - cooling_data[time_col].min()
        y_data = cooling_data[therm_col]

  
        initial_guess = [y_data.min(), y_data.max() - y_data.min(), 1000]
        params, covariance = curve_fit(cooling_func, x_data, y_data, p0=initial_guess)

        
        a_opt, b_opt, c_opt = params
        tau = c_opt
        
        print(f"Fit complete!")
        print(f"  Final Temp (a): {a_opt:.2f}")
        print(f"  Temp Drop (b): {b_opt:.2f}")
        print(f"  Time Constant (tau): {tau:.2f} ms")

        
        plt.figure(figsize=(10, 6))
        
        
        plt.plot(x_data, y_data, 'bo', label='Experimental Data', markersize=4)
        
      
        x_smooth = np.linspace(x_data.min(), x_data.max(), 100)
        y_fit = cooling_func(x_smooth, a_opt, b_opt, c_opt)
        
        plt.plot(x_smooth, y_fit, 'r-', label=f'Exponential Fit ($\\tau$ = {tau:.1f} ms)')
        
        plt.title('Physics Fit: Thermistor Cooling Curve')
        plt.xlabel(f'Time since cooling started (ms)')
        plt.ylabel('Thermistor Value')
        plt.legend()
        plt.grid(True)
        plt.show()

except FileNotFoundError:
    print(f"Error: Could not find the file '{FILE_NAME}'")
except Exception as e:
    print(f"An error occurred: {e}")