import matplotlib.pyplot as plt
import seaborn as sns


def visualize_department_pie_chart():
    """
    Visualizes the number of employees in each department using a pie chart.
    """
    global df
    if df is not None:
        plt.figure(figsize=(8, 6))
        df['Department'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title('Number of Employees in Each Department')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()
    else:
        print("No data loaded for visualization.")


def visualize_distance_histogram():
    """
    Visualizes the distribution of distance employees work from home using a histogram.
    """
    global df
    if df is not None:
        plt.figure(figsize=(10, 6))
        sns.histplot(df['DistanceFromHome'], bins=20, kde=True)
        plt.title('Distribution of Distance from Home for Employees')
        plt.xlabel('Distance from Home')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print("No data loaded for visualization.")
