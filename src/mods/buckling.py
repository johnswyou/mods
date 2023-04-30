import math

def max_stress(P, A, e, c, r, L, E):
    """
    Calculates the maximum stress experienced by a column using the secant formula.

    Parameters:
        P (float): Applied load
        A (float): Cross-sectional area of the column
        e (float): Eccentricity of the load
        c (float): Distance from the centroid of the cross-section to the extreme fiber
        r (float): Radius of gyration of the cross-section
        L (float): Length of the column
        E (float): Modulus of elasticity of the material

    Returns:
        float: Maximum stress experienced by the column
    """
    sec_term = math.sec((L/(2*r)) * math.sqrt(P/(E*A)))
    max_stress = (P/A) * (1 + (e*c)/(r**2) * sec_term)
    return max_stress

def critical_load(E, I, L, support):
    """
    Calculates the critical load on an ideal column using Euler's formula.
    This is the maximum axial load that a member can carry before buckling.

    Parameters:
        E (float): Modulus of elasticity of the material
        I (float): Moment of inertia of the cross-section of the column
        L (float): Length of the column
        support (str): Type of support, can be 'pin', 'fixed', 'pin-fixed', or 'fixed-free'

    Returns:
        float: Critical load on the column
    """
    K_dict = {'pin': 1, 'fixed': 0.5, 'pin-fixed': 0.7, 'fixed-free': 2}
    K = K_dict[support]

    P_cr = (math.pi**2 * E * I)/(K * L)**2

    return P_cr

def critical_stress(E_t, L, r, support):
    """
    Calculates the critical stress on an ideal column using Engesser's equation with tangent modulus.

    Parameters:
        E_t (float): Tangent modulus of elasticity of the material
        L (float): Length of the column
        r (float): Radius of gyration of the cross-section of the column
        support (str): Type of support, can be 'pin', 'fixed', 'pin-fixed', or 'fixed-free'

    Returns:
        float: Critical stress on the column
    """
    K_dict = {'pin': 1, 'fixed': 0.5, 'pin-fixed': 0.7, 'fixed-free': 2}
    K = K_dict[support]

    sigma_cr = (math.pi**2 * E_t)/((K * L/r)**2)

    return sigma_cr
