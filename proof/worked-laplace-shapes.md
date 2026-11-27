# Where the matched-means pair differs

Set a=1, t=1/b, G₀=δ₀, and G₁=(δ₋₁+δ₁)/2. Their means both vanish, and their W₁ distance is one. Let r(x) be the ratio of the observation densities under G₁ and G₀.

For |x|≤1, the exact ratio is exp[−t(1−|x|)] cosh(tx). For |x|≥1 it is cosh(t). The formulas agree at both endpoints. As t decreases, (r−1)/t converges uniformly on the interior to |x|−1, while the scaled tail contrast tends to zero.

Under law G₀, the probability of an interior report is 1−exp(−t), asymptotic to t. The squared relative density difference there is of order t². More precisely, multiplying its integral against the density by t⁻³ and taking the limit gives (1/2)∫₋₁¹(1−|x|)²dx=1/3. The tail contribution is of order t⁴. These computations give χ² asymptotic to t³/3 for this normalized example.

The rotating graphic shows the scaled ratio across position and inverse scale. The explorer displays the exact formulas evaluated in floating point for reading convenience. The replay bounds them with rational Taylor intervals.
