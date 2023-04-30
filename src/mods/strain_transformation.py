import math
import matplotlib.pyplot as plt

def average_strain(epsilon_x, epsilon_y):
    """
    Calculates the average strain and returns the value.

    Parameters:
        epsilon_x (float): Strain value in the x-direction
        epsilon_y (float): Strain value in the y-direction

    Returns:
        float: Average strain value
    """
    epsilon_avg = (epsilon_x + epsilon_y)/2

    return epsilon_avg

def normal_strain_transform(epsilon_x, epsilon_y, gamma_xy, theta):
    """
    Applies a strain transformation to the given strains and returns the transformed strain value.

    Parameters:
            epsilon_x (float): Strain value in the x-direction
            epsilon_y (float): Strain value in the y-direction
            gamma_xy (float): Shear strain value in the xy-plane
            theta (float): Angle of rotation in degrees

    Returns:
        tuple: Transformed strain value in the x'-direction and y'-direction
    """
    theta_rad = math.radians(theta)
    cos_theta = math.cos(2*theta_rad)
    sin_theta = math.sin(2*theta_rad)

    epsilon_x_prime = (epsilon_x + epsilon_y)/2 + (epsilon_x - epsilon_y)/2 * cos_theta + gamma_xy/2 * sin_theta
    epsilon_y_prime = (epsilon_x + epsilon_y)/2 - (epsilon_x - epsilon_y)/2 * cos_theta - gamma_xy/2 * sin_theta

    return epsilon_x_prime, epsilon_y_prime

def shear_strain_transform(epsilon_x, epsilon_y, gamma_xy, theta):
    """
    Applies a transformation to the given shear strain and returns the transformed shear strain value.

    Parameters:
        epsilon_x (float): Strain value in the x-direction
        epsilon_y (float): Strain value in the y-direction
        gamma_xy (float): Shear strain value in the xy-plane
        theta (float): Angle of rotation in degrees

    Returns:
        float: Transformed shear strain value in the x'y'-plane
    """
    theta_rad = math.radians(theta)
    cos_theta = math.cos(2*theta_rad)
    sin_theta = math.sin(2*theta_rad)

    gamma_xy_prime = -1*(epsilon_x - epsilon_y)/2 * sin_theta + gamma_xy/2 * cos_theta

    return gamma_xy_prime

def principal_strain(epsilon_x, epsilon_y, gamma_xy):
    """
    Calculates the principal strains and returns the values in a tuple.

    Parameters:
        epsilon_x (float): Strain value in the x-direction
        epsilon_y (float): Strain value in the y-direction
        gamma_xy (float): Shear strain value in the xy-plane

    Returns:
        tuple: Principal strain values in the x'-direction and y'-direction
    """
    epsilon_prime = (epsilon_x + epsilon_y)/2
    epsilon_double_prime = (epsilon_x - epsilon_y)/2
    gamma_prime = gamma_xy/2

    epsilon_1 = epsilon_prime + math.sqrt(epsilon_double_prime**2 + gamma_prime**2)
    epsilon_2 = epsilon_prime - math.sqrt(epsilon_double_prime**2 + gamma_prime**2)

    return epsilon_1, epsilon_2

def principal_strain_angle(epsilon_x, epsilon_y, gamma_xy):
    """
    Calculates the principal directions and returns the values in a tuple.

    Parameters:
        epsilon_x (float): Strain value in the x-direction
        epsilon_y (float): Strain value in the y-direction
        gamma_xy (float): Shear strain value in the xy-plane

    Returns:
        tuple: Principal direction values in degrees
    """
    epsilon_double_prime = (epsilon_x - epsilon_y)/2
    gamma_prime = gamma_xy/2

    theta_1 = math.degrees(math.atan2(gamma_prime, epsilon_double_prime))/2
    theta_2 = theta_1 + 90

    return theta_1, theta_2

def maximum_in_plane_shear_strain(epsilon_x, epsilon_y, gamma_xy):
    """
    Calculates the maximum in-plane shear strain and returns the value.

    Parameters:
        epsilon_x (float): Strain value in the x-direction
        epsilon_y (float): Strain value in the y-direction
        gamma_xy (float): Shear strain value in the xy-plane

    Returns:
        float: Maximum in-plane shear strain value
    """
    epsilon_double_prime = (epsilon_x - epsilon_y)/2
    gamma_prime = gamma_xy/2

    gamma_max = 2*math.sqrt(epsilon_double_prime**2 + gamma_prime**2)

    return gamma_max

def maximum_in_plane_shear_strain_angle(epsilon_x, epsilon_y, gamma_xy):
    """
    Calculates the angle of the maximum in-plane shear strain and returns the value.

    Parameters:
        epsilon_x (float): Strain value in the x-direction
        epsilon_y (float): Strain value in the y-direction
        gamma_xy (float): Shear strain value in the xy-plane

    Returns:
        float: Angle of the maximum in-plane shear strain value in degrees
    """
    epsilon_double_prime = (epsilon_x - epsilon_y)/2
    gamma_prime = gamma_xy/2

    theta_max = math.degrees(math.atan2(-epsilon_double_prime, gamma_prime))/2

    return theta_max, theta_max + 90

def mohrs_circle(epsilon_x, epsilon_y, gamma_xy):
    """
    Calculates the center and radius of the Mohr's circle and returns the values in a tuple.

    Parameters:
        epsilon_x (float): Strain value in the x-direction
        epsilon_y (float): Strain value in the y-direction
        gamma_xy (float): Shear strain value in the xy-plane

    Returns:
        tuple: Center and radius of the Mohr's circle
    """
    epsilon_prime = (epsilon_x + epsilon_y)/2
    epsilon_double_prime = (epsilon_x - epsilon_y)/2
    gamma_prime = gamma_xy/2

    center = (epsilon_prime, 0)
    radius = math.sqrt(epsilon_double_prime**2 + gamma_prime**2)

    return center, radius

def mohrs_circle_plot(epsilon_x, epsilon_y, gamma_xy):
    """
    Plots the Mohr's circle and returns the plot.

    Parameters:
        epsilon_x (float): Strain value in the x-direction
        epsilon_y (float): Strain value in the y-direction
        gamma_xy (float): Shear strain value in the xy-plane

    Returns:
        matplotlib.pyplot.plot: Plot of the Mohr's circle
    """
    center, radius = mohrs_circle(epsilon_x, epsilon_y, gamma_xy)

    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_aspect('equal')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.set_xlabel(r'$\epsilon$')
    ax.set_ylabel(r'$\gamma$')
    ax.set_title("Mohr's Circle")

    circle = plt.Circle(center, radius, color='b', fill=False)
    ax.add_artist(circle)
    return fig

def mohrs_circle_strain(epsilon_x, epsilon_y, gamma_xy, theta):
    """
    Calculates the center and radius of the transformed Mohr's circle and returns the values in a tuple.

    Parameters:
        epsilon_x (float): Strain value in the x-direction
        epsilon_y (float): Strain value in the y-direction
        gamma_xy (float): Shear strain value in the xy-plane
        theta (float): Angle of rotation in degrees

    Returns:
        tuple: Center and radius of the transformed Mohr's circle
    """
    epsilon_x_prime, epsilon_y_prime = normal_strain_transform(epsilon_x, epsilon_y, gamma_xy, theta)
    gamma_xy_prime = shear_strain_transform(epsilon_x, epsilon_y, gamma_xy, theta)

    return mohrs_circle_strain(epsilon_x_prime, epsilon_y_prime, gamma_xy_prime)

def mohrs_circle_strain_plot(epsilon_x, epsilon_y, gamma_xy, theta):
    """
    Plots the Mohr's circle and a point representing the transformed strain state and returns the plot.

    Parameters:
        epsilon_x (float): Strain value in the x-direction
        epsilon_y (float): Strain value in the y-direction
        gamma_xy (float): Shear strain value in the xy-plane
        theta (float): Plane inclination angle in degrees

    Returns:
        matplotlib.pyplot.plot: Plot of the Mohr's circle and transformed strain state
    """
    epsilon_x_prime, gamma_xy_prime = mohrs_circle_strain(epsilon_x, epsilon_y, gamma_xy, theta)
    center, radius = mohrs_circle(epsilon_x, epsilon_y, gamma_xy)
    circle = plt.Circle((center, 0), radius, fill=False)
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.add_artist(circle)

    # Set the x and y limits
    ax.set_xlim([center - radius - 0.1 * radius, center + radius + 0.1 * radius])  # adding a little extra space
    ax.set_ylim([-radius - 0.1 * radius, radius + 0.1 * radius])  # adding a little extra space

    plt.plot(epsilon_x_prime, gamma_xy_prime, 'ro')
    plt.xlabel("Normal Strain")
    plt.ylabel("Shear Strain")
    plt.title("Mohr's Circle")
    plt.grid()
    plt.show()
    return fig
