import math
from .bandgap import Eg

_K_B_EV_PER_K = 8.617333262e-5

def n_i(x: float, T: float, model: str = "hansen1982") -> float:
    if T <= 0.0:
        return 0.0
    Eg_val = Eg(x, T, model=model)
    if Eg_val <= 0.0:
        return 0.0

    F = (
        5.585
        - 3.82 * x
        + 1.753e-3 * T
        - 1.364e-3 * T * x
    )
    if F <= 0.0:
        return 0.0

    main = (
        1.0e14
        * (Eg_val ** 0.75)
        * (T ** 1.5)
        * math.exp(-Eg_val / (2.0 * _K_B_EV_PER_K * T))
    )
    return F * main
