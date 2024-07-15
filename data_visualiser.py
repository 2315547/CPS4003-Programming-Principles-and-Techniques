# data_visualizer.py

import matplotlib
import seaborn
import matplotlib.pyplot as plt
import seaborn as sns
from data_handler import df

def visualize_department_pie_chart():
    global df
    if df is not None:
        plt.figure(figsize=(8, 6))
        df['Department'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title('Number of Employees in Each Department')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()
    else:
        print("No data loaded for visualization.")
