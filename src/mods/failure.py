import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from mods.stress_transformation import principal_stress

def plot_von_mises_failure_envelope(sy, sigma_x=None, sigma_y=None, tau_xy=None):
    # Sy is the yield strength of the material
    ellipse = Ellipse((0, 0), width=sy*np.sqrt(2)*2, height=sy*np.sqrt(2/3)*2, angle=45, alpha=0.4)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.add_patch(ellipse)
    ax.set_xlim(-sy*np.sqrt(2), sy*np.sqrt(2))
    ax.set_ylim(-sy*np.sqrt(2), sy*np.sqrt(2))
    ax.set_aspect('equal', adjustable='box')

    # Draw bold black lines at x=0 and y=0
    ax.axhline(0, color='black', linewidth=1.5)
    ax.axvline(0, color='black', linewidth=1.5)

    # If stress values are given, calculate and plot the principal stresses
    if sigma_x is not None and sigma_y is not None and tau_xy is not None:
        sigma_1, sigma_2 = principal_stress(sigma_x, sigma_y, tau_xy)
        ax.plot(sigma_1, sigma_2, 'ro', markersize=8)
    elif sigma_x is not None or sigma_y is not None or tau_xy is not None:
        raise ValueError("Please provide all three stress values: sigma_x, sigma_y, and tau_xy")
    
    plt.title("Von Mises Failure Envelope for Plane Stress")
    plt.xlabel("Major Principal Stress (σ1)")
    plt.ylabel("Minor Principal Stress (σ2)")
    plt.grid(True)
    plt.show()
