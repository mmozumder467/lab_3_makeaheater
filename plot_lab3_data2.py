import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = 'lab_heater_data2.csv' 

try:

    data = pd.read_csv(FILE_NAME)
    
    time_col = data.columns[0]
    pot_col = data.columns[1]
    therm_col = data.columns[2]

    print(f"Successfully loaded data from {FILE_NAME}")
    print("Column names found:", list(data.columns))

    fig, ax1 = plt.subplots(figsize=(12, 7))

    color = 'tab:red'
    ax1.set_xlabel(time_col)
    ax1.set_ylabel(therm_col, color=color)
    ax1.plot(data[time_col], data[therm_col], color=color, label=therm_col)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx() 
    color = 'tab:blue'
    ax2.set_ylabel(pot_col, color=color)
    ax2.plot(data[time_col], data[pot_col], color=color, label=pot_col, linestyle='--')
    ax2.tick_params(axis='y', labelcolor=color)


    plt.title('Heater Lab: Potentiometer vs. Thermistor')
    fig.tight_layout()  
    

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left')

    plt.show()

except FileNotFoundError:
    print(f"Error: Could not find the file '{FILE_NAME}'")
    print("Please make sure your data file is in the same directory as this script,")
    print("or change the FILE_NAME variable at the top of the code.")
except Exception as e:
    print(f"An error occurred: {e}")
    print("Make sure your CSV file is formatted correctly (e.g., 'col1,col2,col3')")