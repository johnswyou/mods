import math

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
