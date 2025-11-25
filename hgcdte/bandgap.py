import math
from .utils import load_material_model


def Eg(x: float, T: float, model: str = "hansen1982") -> float:
    """
    Hansen 1982 bandgap model (default).
    Returns Eg in eV.
    """
    m = load_material_model(model)

    p = m["Eg_polynomial"]

    # Eg(x,T)
    Eg_val = (
        p["E0"]
        + p["A1"] * x
        + p["A2"] * x**2
        + p["A3"] * x**3
        + p["alpha"] * T * (1 - 2*x)
    )

    return Eg_val


def lambda_c_from_Eg(x: float, T: float, model: str = "hansen1982") -> float:
    """
    Cutoff wavelength computed from Eg:
    λc [µm] = 1.23984 / Eg[eV]
    """
    Eg_val = Eg(x, T, model=model)
    if Eg_val <= 0:
        return float("inf")
    return 1.23984 / Eg_val


def lambda_c_hansen_poly(x: float, T: float, model: str = "hansen1982") -> float:
    """
    Hansen direct polynomial fit for the cutoff wavelength λp(x,T).
    """
    m = load_material_model(model)
    p = m["lambda_polynomial"]

    inv_lambda = (
        p["L0"]
        + p["L1"] * x
        + p["L2"] * x**2
        + p["L3"] * x**3
        + p["alpha_lambda"] * T * (1 - 2*x)
    )

    if inv_lambda <= 0:
        return float("inf")

    return 1.0 / inv_lambda


def lambda_c_um(x: float, T: float, mode: str = "from_Eg", model: str = "hansen1982") -> float:
    """
    Unified public interface:

    mode = "from_Eg" (default)
    mode = "hansen_poly"
    """
    if mode == "from_Eg":
        return lambda_c_from_Eg(x, T, model=model)
    elif mode == "hansen_poly":
        return lambda_c_hansen_poly(x, T, model=model)
    else:
        raise ValueError(f"Unknown mode '{mode}'")
