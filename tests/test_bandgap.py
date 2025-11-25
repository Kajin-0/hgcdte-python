import pytest
from hgcdte.bandgap import Eg, lambda_c_um


def test_Eg_reasonable():
    # For x=0.22 at 77 K, Eg should be ~0.1 eV
    Eg_val = Eg(0.22, 77)
    assert 0.05 < Eg_val < 0.20


def test_lambda_c_from_Eg():
    # Expect ~10–12 µm for x=0.22 at 77 K
    lambda_val = lambda_c_um(0.22, 77, mode="from_Eg")
    assert 5 < lambda_val < 20


def test_lambda_poly_exists():
    lambda_val = lambda_c_um(0.22, 77, mode="hansen_poly")
    assert lambda_val > 0
