import math
import matplotlib.pyplot as plt

def average_normal_stress(sigma_x, sigma_y):
    """
    Calculate the average normal stress.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.

    Returns:
        float: Average normal stress.
    """
    sigma_avg = (sigma_x + sigma_y)/2
    return sigma_avg

def normal_stress_transform(sigma_x, sigma_y, tau_xy, theta):
    """
    Calculate the normal stress on an inclined plane.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.
        tau_xy (float): Shear stress in the x-y plane.
        theta (float): Angle of the inclined plane in degrees.

    Returns:
        float: Normal stress on the inclined plane.
    """
    theta_rad = math.radians(theta)  # converting degrees to radians
    sigma_n = (sigma_x + sigma_y)/2 + (sigma_x - sigma_y)/2*math.cos(2*theta_rad) + tau_xy*math.sin(2*theta_rad)
    return sigma_n

def shear_stress_transform(sigma_x, sigma_y, tau_xy, theta):
    """
    Calculate the shear stress on an inclined plane.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.
        tau_xy (float): Shear stress in the x-y plane.
        theta (float): Angle of the inclined plane in degrees.

    Returns:
        float: Shear stress on the inclined plane.
    """
    theta_rad = math.radians(theta)  # converting degrees to radians
    tau_n = -(sigma_x - sigma_y)/2*math.sin(2*theta_rad) + tau_xy*math.cos(2*theta_rad)
    return tau_n

def principal_stress(sigma_x, sigma_y, tau_xy, stress_type):
    """
    Calculate the principal stress.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.
        tau_xy (float): Shear stress in the x-y plane.
        stress_type (str): 'max' for major principal stress, 'min' for minor principal stress.

    Returns:
        float: Principal stress, either major or minor based on stress_type.

    Raises:
        ValueError: If stress_type is not 'max' or 'min'.
    """
    if stress_type == "max":
        sigma = (sigma_x + sigma_y)/2 + math.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)
    elif stress_type == "min":
        sigma = (sigma_x + sigma_y)/2 - math.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)
    else:
        raise ValueError("Invalid stress_type. Choose either 'max' or 'min'.")
    return sigma

def principal_stress_angle(sigma_x, sigma_y, tau_xy):
    """
    Calculate the principal stress angle.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.
        tau_xy (float): Shear stress in the x-y plane.

    Returns:
        float: Principal stress angle in degrees.
    """
    numerator = 2 * tau_xy
    denominator = sigma_x - sigma_y
    theta_p_rad = math.atan2(numerator, denominator) / 2  # atan2 takes care of the angle quadrant
    theta_p_deg = math.degrees(theta_p_rad)  # converting radians to degrees
    return theta_p_deg

def maximum_in_plane_shear_stress(sigma_x, sigma_y, tau_xy):
    """
    Calculate the maximum in-plane shear stress.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.
        tau_xy (float): Shear stress in the x-y plane.

    Returns:
        float: Maximum in-plane shear stress.
    """
    tau_max = math.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)
    return tau_max

def maximum_in_plane_shear_stress_angle(sigma_x, sigma_y, tau_xy):
    """
    Calculate the maximum in-plane shear stress angle.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.
        tau_xy (float): Shear stress in the x-y plane.

    Returns:
        float: Maximum in-plane shear stress angle in degrees.
    """
    numerator = sigma_y - sigma_x
    denominator = 2 * tau_xy
    theta_max_rad = math.atan2(numerator, denominator) / 2  # atan2 takes care of the angle quadrant
    theta_max_deg = math.degrees(theta_max_rad)  # converting radians to degrees
    return theta_max_deg

def mohrs_circle(sigma_x, sigma_y, tau_xy):
    """
    Calculate the center and radius of the Mohr's circle.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.
        tau_xy (float): Shear stress in the x-y plane.

    Returns:
        tuple: (center, radius) of the Mohr's circle.
    """
    center = (sigma_x + sigma_y)/2
    radius = math.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2)
    return (center, radius)

def mohrs_circle_plot(sigma_x, sigma_y, tau_xy):
    """
    Plot the Mohr's circle.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.
        tau_xy (float): Shear stress in the x-y plane.

    Returns:
        matplotlib.pyplot.plot: Mohr's circle plot.
    """
    
    center, radius = mohrs_circle(sigma_x, sigma_y, tau_xy)
    circle = plt.Circle((center, 0), radius, fill=False)
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.add_artist(circle)
    
    # Set the x and y limits
    ax.set_xlim([center - radius - 0.1 * radius, center + radius + 0.1 * radius])  # adding a little extra space
    ax.set_ylim([-radius - 0.1 * radius, radius + 0.1 * radius])  # adding a little extra space
    
    plt.xlabel("Normal Stress")
    plt.ylabel("Shear Stress")
    plt.title("Mohr's Circle")
    plt.grid()
    plt.show()
    return fig

def mohrs_circle_stress(sigma_x, sigma_y, tau_xy, theta):
    """
    Calculate the normal and shear stresses on an inclined plane.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.
        tau_xy (float): Shear stress in the x-y plane.
        theta (float): Angle of the inclined plane in degrees.

    Returns:
        tuple: (sigma_n, tau_n) on the inclined plane.
    """
    theta_rad = math.radians(theta)  # converting degrees to radians
    center, radius = mohrs_circle(sigma_x, sigma_y, tau_xy)
    sigma_n = center + radius*math.cos(2*theta_rad)
    tau_n = radius*math.sin(2*theta_rad)
    return (sigma_n, tau_n)

def mohrs_circle_stress_plot(sigma_x, sigma_y, tau_xy, theta):
    """
    Plot the normal and shear stresses on an inclined plane on the Mohr's circle.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.
        tau_xy (float): Shear stress in the x-y plane.
        theta (float): Angle of the inclined plane in degrees.

    Returns:
        matplotlib.pyplot.plot: Normal and shear stresses on the inclined plane on the Mohr's circle.
    """
    sigma_n, tau_n = mohrs_circle_stress(sigma_x, sigma_y, tau_xy, theta)
    center, radius = mohrs_circle(sigma_x, sigma_y, tau_xy)
    circle = plt.Circle((center, 0), radius, fill=False)
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.add_artist(circle)

    # Set the x and y limits
    ax.set_xlim([center - radius - 0.1 * radius, center + radius + 0.1 * radius])  # adding a little extra space
    ax.set_ylim([-radius - 0.1 * radius, radius + 0.1 * radius])  # adding a little extra space

    plt.plot(sigma_n, tau_n, 'ro')
    plt.xlabel("Normal Stress")
    plt.ylabel("Shear Stress")
    plt.title("Mohr's Circle")
    plt.grid()
    plt.show()
    return fig

def mohrs_circle_plane_angle(sigma_x, sigma_y, tau_xy, theta):
    """
    Calculate the angle of the plane that has the normal and shear stresses on the Mohr's circle.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.
        tau_xy (float): Shear stress in the x-y plane.
        theta (float): Angle of the inclined plane in degrees.

    Returns:
        float: Angle of the plane that has the normal and shear stresses on the Mohr's circle in degrees.
    """
    sigma_n, tau_n = mohrs_circle_stress(sigma_x, sigma_y, tau_xy, theta)
    theta_rad = math.atan2(tau_n, sigma_n) / 2  # atan2 takes care of the angle quadrant
    theta_deg = math.degrees(theta_rad)  # converting radians to degrees
    return theta_deg

def mohrs_circle_plane_angle_plot(sigma_x, sigma_y, tau_xy, theta):
    """
    Plot the angle of the plane that has the normal and shear stresses on the Mohr's circle.

    Parameters:
        sigma_x (float): Normal stress in the x direction.
        sigma_y (float): Normal stress in the y direction.
        tau_xy (float): Shear stress in the x-y plane.
        theta (float): Angle of the inclined plane in degrees.

    Returns:
        matplotlib.pyplot.plot: Angle of the plane that has the normal and shear stresses on the Mohr's circle.
    """
    theta_deg = mohrs_circle_plane_angle(sigma_x, sigma_y, tau_xy, theta)
    sigma_n, tau_n = mohrs_circle_stress(sigma_x, sigma_y, tau_xy, theta)
    center, radius = mohrs_circle(sigma_x, sigma_y, tau_xy)
    circle = plt.Circle((center, 0), radius, fill=False)
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.add_artist(circle)

    # Set the x and y limits
    ax.set_xlim([center - radius - 0.1 * radius, center + radius + 0.1 * radius])  # adding a little extra space
    ax.set_ylim([-radius - 0.1 * radius, radius + 0.1 * radius])  # adding a little extra space

    plt.plot(sigma_n, tau_n, 'ro')
    plt.plot([center, sigma_n], [0, tau_n], 'k-')
    plt.plot([center, sigma_n], [0, 0], 'k-')
    plt.plot([sigma_n, sigma_n], [0, tau_n], 'k-')
    plt.xlabel("Normal Stress")
    plt.ylabel("Shear Stress")
    plt.title("Mohr's Circle")
    plt.grid()
    plt.show()
    return fig

