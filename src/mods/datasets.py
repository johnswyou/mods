from importlib import resources
import pandas as pd

def get_mechanical_properties_si():
    """Get path to 'avg_mech_prop_si.csv'

    Returns
    -------
    pandas.DataFrame

    References
    ----------
    [1] R.C. Hibbeler, Mechanics of Materials, 9th ed., Pearson, 2014.
    """
    with resources.path("mods.data", "avg_mech_prop_si.csv") as f:
        data_file_path = f
    df = pd.read_csv(data_file_path)
    return df

def get_mechanical_properties_imperial():
    """Get path to 'avg_mech_prop_imperial.csv'

    Returns
    -------
    pandas.DataFrame

    References
    ----------
    [1] R.C. Hibbeler, Mechanics of Materials, 9th ed., Pearson, 2014.
    """
    with resources.path("mods.data", "avg_mech_prop_imperial.csv") as f:
        data_file_path = f
    df = pd.read_csv(data_file_path)
    return df

def get_w_shapes_imperial():
    """Get path to 'w_shapes_fps_imperial.csv'

    Returns
    -------
    pandas.DataFrame

    References
    ----------
    [1] R.C. Hibbeler, Mechanics of Materials, 9th ed., Pearson, 2014.
    """
    with resources.path("mods.data", "w_shapes_fps_imperial.csv") as f:
        data_file_path = f
    df = pd.read_csv(data_file_path)
    return df

def get_w_shapes_si():
    """Get path to 'w_shapes_fps_si.csv'

    Returns
    -------
    pandas.DataFrame

    References
    ----------
    [1] R.C. Hibbeler, Mechanics of Materials, 9th ed., Pearson, 2014.
    """
    with resources.path("mods.data", "w_shapes_fps_si.csv") as f:
        data_file_path = f
    df = pd.read_csv(data_file_path)
    return df
