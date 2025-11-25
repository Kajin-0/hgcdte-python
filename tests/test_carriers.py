from hgcdte.carriers import n_i

def test_n_i_positive():
    val = n_i(0.22, 77.0)
    assert val >= 0.0
