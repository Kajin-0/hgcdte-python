import math

def x_from_Z_half(Z_half: float, t_um: float) -> float:
    '''
    Compute Cd mole fraction x from the 50% transmission point Z1/2 (wavenumber).
    Based on Gopal et al., Infrared Physics, 33, 39–45 (1992).

    Parameters
    ----------
    Z_half : float
        Wavenumber at 50% transmission (cm^-1).
    t_um : float
        Epilayer thickness in micrometers.
    '''
    # Eq. (8): x0(Z1/2)
    x0 = 1.013456e-4 * (Z_half ** 2) + 6.229919e-2

    # Eq. (7): full relation
    numerator = (-9.549999e-3 - 2e-4 * Z_half) * math.log(10.0 / t_um)
    denominator = 1.0 + x0

    return x0 + numerator / denominator


def x_from_Z_i(Z_i: float, t_um: float) -> float:
    '''
    Compute Cd mole fraction x from the zero-transmission cut-on Z_i (wavenumber).
    Based on Gopal et al., Infrared Physics, 33, 39–45 (1992).

    Parameters
    ----------
    Z_i : float
        Zero-transmission cut-on wavenumber (cm^-1).
    t_um : float
        Epilayer thickness in micrometers.
    '''
    # Eq. (10): x0(Zi)
    x0 = 9.95625e-5 * Z_i + 5.453485e-2

    # Eq. (9): full relation
    numerator = (9.1e-3 - 7e-6 * Z_i) * math.log(10.0 / t_um)
    denominator = 1.0 + x0

    return x0 + numerator / denominator


def x_from_lambda_half(lambda_half_um: float, t_um: float) -> float:
    '''
    Compute Cd mole fraction x from the 50% transmission wavelength λ1/2 (µm).

    This is a thin wrapper around x_from_Z_half, using
        Z_half [cm^-1] = 1e4 / λ_half[µm].
    '''
    if lambda_half_um <= 0.0:
        raise ValueError("lambda_half_um must be positive")
    Z_half = 1.0e4 / lambda_half_um
    return x_from_Z_half(Z_half, t_um)


def x_from_lambda_i(lambda_i_um: float, t_um: float) -> float:
    '''
    Compute Cd mole fraction x from the zero-transmission cut-on wavelength λ_i (µm).

    This is a thin wrapper around x_from_Z_i, using
        Z_i [cm^-1] = 1e4 / λ_i[µm].
    '''
    if lambda_i_um <= 0.0:
        raise ValueError("lambda_i_um must be positive")
    Z_i = 1.0e4 / lambda_i_um
    return x_from_Z_i(Z_i, t_um)
