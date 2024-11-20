import numpy as np
import matplotlib.pyplot as plt

def plot_function():
    """
    Plots the function Y(x) = x^cos(x) for x in the range [0, 10].
    The plot includes a solid blue line with a specified thickness, labeled axes,
    a title, and a legend.
    """
    # Define the range of x values, avoiding x=0 to prevent undefined behavior
    x = np.linspace(0.01, 10, 1000)
    
    # Calculate Y(x) = x^cos(x)
    y = x ** np.cos(x)
    
    # Create the plot with a solid blue line of linewidth 2
    plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label=r'$Y(x) = x^{\cos(x)}$')
    
    # Label the x-axis and y-axis
    plt.xlabel('x')
    plt.ylabel('Y(x)')
    
    # Set the title of the plot
    plt.title('Plot of the Function Y(x) = x^cos(x)')
    
    # Add a legend to the plot
    plt.legend()
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    plot_function()
