import math

def x_from_Z_half(Z_half: float, t_um: float) -> float:
    '''
    Compute Cd mole fraction x from the 50% transmission point Z1/2.
    Based on Gopal et al., Infrared Physics, 33, 39–45 (1992).
    '''
    # Eq. (8): x0(Z1/2)
    x0 = 1.013456e-4 * (Z_half ** 2) + 6.229919e-2

    # Eq. (7)
    numerator = (-9.549999e-3 - 2e-4 * Z_half) * math.log(10.0 / t_um)
    denominator = 1.0 + x0

    return x0 + numerator / denominator


def x_from_Z_i(Z_i: float, t_um: float) -> float:
    '''
    Compute Cd mole fraction x from the zero-transmission cut-on Z_i.
    Based on Gopal et al., Infrared Physics, 33, 39–45 (1992).
    '''
    # Eq. (10): x0(Zi)
    x0 = 9.95625e-5 * Z_i + 5.453485e-2

    # Eq. (9)
    numerator = (9.1e-3 - 7e-6 * Z_i) * math.log(10.0 / t_um)
    denominator = 1.0 + x0

    return x0 + numerator / denominator
