"""Bound formulas for the matched-means Laplace witness by exact arithmetic."""
from fractions import Fraction as F


def exponential_bounds(x):
    """Return bounds for exp(x) using a geometric majorant for the positive tail."""
    assert x >= 0
    total = term = F(1)
    count = 24
    for k in range(1, count + 1):
        term *= x / k
        total += term
    next_term = term * x / (count + 1)
    next_ratio_bound = x / (count + 2)
    assert next_ratio_bound < 1
    return total, total + next_term / (1 - next_ratio_bound)


def negative_exponential_bounds(x):
    low, high = exponential_bounds(x)
    return 1 / high, 1 / low


def cosh_bounds(x):
    ep = exponential_bounds(abs(x))
    en = negative_exponential_bounds(abs(x))
    return tuple((p + n) / 2 for p, n in zip(ep, en))


assert exponential_bounds(F(1))[1] < 3
profiles = 0
for k in range(1, 17):
    t = F(k, 16)
    en = negative_exponential_bounds(t)
    mass_upper = 1 - en[0]
    assert 0 < mass_upper <= t
    tail = cosh_bounds(t)
    assert 0 <= tail[0] - 1 <= tail[1] - 1 < t * t
    for i in range(-16, 17):
        x = F(i, 16)
        observed = exponential_bounds(t * abs(x))
        plus = negative_exponential_bounds(t * abs(x + 1))
        minus = negative_exponential_bounds(t * abs(x - 1))
        via_kernel = tuple(e * (p + m) / 2 for e, p, m in zip(observed, plus, minus))
        prefactor = negative_exponential_bounds(t * (1 - abs(x)))
        ch = cosh_bounds(t * x)
        via_formula = tuple(p * c for p, c in zip(prefactor, ch))
        left, right = max(via_kernel[0], via_formula[0]), min(via_kernel[1], via_formula[1])
        assert left <= right
        assert max(abs(left - 1), abs(right - 1)) < 2 * t
        if abs(x) == 1:
            assert max(left, tail[0]) <= min(right, tail[1])
        profiles += 1
    assert (2 * t) ** 2 * mass_upper + (tail[1] - 1) ** 2 <= 5 * t ** 3
print(f"{profiles} rational interval checks of the interior ratio, 16 mass/tail bounds and cubic certificates.")
