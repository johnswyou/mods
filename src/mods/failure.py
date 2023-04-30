import matplotlib.pyplot as plt
import numpy as np

def von_mises(sigma_Y):
    """
    Plots the Von Mises failure envelope for a given yield strength.

    Parameters:
        sigma_Y (float): Yield strength of the material

    Returns:
        None
    """
    # Set up the figure and axis
    fig, ax = plt.subplots()

    # Create an array of values for sigma_1
    sigma_1 = np.linspace(0, 1.1 * sigma_Y, 1000)

    # Calculate the corresponding values of sigma_2
    sigma_2 = np.sqrt(sigma_Y**2 - sigma_1**2)

    # Plot the Von Mises failure envelope
    ax.plot(sigma_1, sigma_2, label='Von Mises')

    # Add the yield strength to the plot
    ax.axvline(x=sigma_Y, color='black', linestyle='--', label='Yield strength')

    # Add labels and legend
    ax.set_xlabel(r'$\sigma_1$')
    ax.set_ylabel(r'$\sigma_2$')
    ax.set_aspect('equal', adjustable='box')
    ax.legend()

    # Show the plot
    plt.show()
