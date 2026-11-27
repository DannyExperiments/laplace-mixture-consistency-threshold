# Q1095 — exact consistency threshold for the Laplace NPMLE

**Answer:** For fixed a>0 and nondecreasing b_n>0, the exact NPMLE over probability measures on I=[-a,a] is W₁-consistent at every fixed mixing law if and only if b_n=o(n^{1/3}). Sufficiency is uniform in the true mixing law and applies to any maximizing choice. If the condition fails, no estimator can be consistent at both of two fixed laws.

## Sufficiency

Set t=1/b_n, T=1/b_1. For H supported on I, let
u_H(t,x)=∫exp(−t|x−θ|)dH(θ), p_H(x)=(t/2)u_H(t,x),
Z_H(t)=∫_I u_H(t,x)dx, q_H(t,x)=u_H(t,x)/Z_H(t) on I.
The likelihood has a maximizer by compactness in W₁ and continuity of each positive p_H(X_i).

**Uniform separation of interior shapes.** For each ε>0 with a nonempty separated pair set, there exists c_ε>0 such that for all H,G with W₁(H,G)≥ε and all 0<t≤T,
‖q_H−q_G‖₁≥c_ε t.
Indeed (q_H−q_G)/t extends continuously in the uniform norm at t=0. Writing A_H(x)=∫|x−θ|dH(θ), L=2a, and an overbar for uniform averaging on I, the extension is −[(A_H−A_G)−overline(A_H−A_G)]/L, by uniformly bounded Taylor remainders on I. Continuity jointly in H,G,t follows from uniformly Lipschitz dependence of the kernels and absolute-distance functions on θ and the uniform remainder. This extension cannot vanish for H≠G: on the interval interior, the almost-everywhere derivative of A_H−A_G is 2(F_H−F_G). Right continuity identifies both CDFs on (−a,a), hence also at −a, and both CDFs are 1 at a. For t>0, equality q_H=q_G means u_H=k u_G on I for k=Z_H/Z_G>0. In distributions on the interior, (∂²_x−t²)u_H=−2t H, so H−kG is supported at the endpoints. Its convolution on the interior is a linear combination of exp(tx) and exp(−tx) and vanishes identically; both coefficients are zero. Total masses force k=1. Compactness of the separated pair set times [0,T] now gives the stated positive minimum. Pinsker gives D(q_G‖q_H)≥c_ε²t²/2.

**Exact likelihood decomposition.** Label reports by their categories (left tail, interior, right tail); write π_H for the three masses and m for the number of interior reports. Conditional on a tail category the density is a shifted exponential of rate t independent of H, since outside I the factor u_H is an exponential times ∫e^{±tθ}dH. Thus the full log likelihood ratio of H to G is the sum of the three-category ratio and the interior conditional ratio. If π̂ denotes empirical category fractions, the categorical ratio is bounded above (simultaneously for all H) by nD(π̂‖π_G)≤n∑_j(π̂_j−π_{G,j})²/π_{G,j}. The last term has expectation 2 by multinomial variances, even when the interior probability vanishes. These inequalities follow respectively from maximizing over unrestricted category probabilities and log x≤x−1.

Given the category labels, the m interior observations are iid q_G. The function h_H=log(q_H/q_G) has Lipschitz constant ≤2t: the triangle inequality bounds each log u_H by t times the displacement, and normalization is constant in x. Consequently its variation on I is at most 4at, and integration by parts bounds the centered empirical average by 4at times the Kolmogorov distance of the interior empirical CDF from the true conditional CDF. The usual Dvoretzky–Kiefer–Wolfowitz bound controls this distance by O_P(m^{-1/2}), uniformly in G conditional on every label sequence with m>0. The worst interior log likelihood ratio over W₁(H,G)≥ε is therefore at most
−m c_ε²t²/2 + O_P(t√m),
with constants/tightness uniform in G.

Here π_{G,in}=(t/2)Z_G∈[at exp(−2aT),at]. If nt³→∞, then nt→∞ since t≤T. Binomial concentration implies m is within fixed positive constant factors of nt with probability tending to one uniformly. Thus mt²→∞ in probability, the negative term beats both the empirical fluctuation and the O_P(1) categorical gain, and the log likelihood is strictly smaller than at G for all separated H with probability tending to one. This proves the result for the ordinary, full-data NPMLE, not merely an estimator discarding the tails.

## Necessity

Take fixed G₀=δ₀ and G₁=(δ_{−a}+δ_a)/2, at W₁ distance a. Write r=p_{G₁}/p_{G₀}. For x outside I, r=cosh(at), so |r−1|=O(t²) as t→0. On I each shifted single-atom ratio lies between e^{−at} and e^{at}, so |r−1|=O(t). Under G₀, P(X∈I)=1−e^{−at}≤at. It follows that χ²(P₁‖P₀)=E₀[(r−1)²]=O(t³). The single-report affinity ρ=∫√(p₀p₁) satisfies 1−ρ≤χ²/2, by (√r−1)²≤(r−1)². The affinity of n iid reports is ρ^n. If nt³ fails to tend to infinity, it is bounded on an infinite subsequence, on which t→0 and ρ^n stays bounded away from zero. By Cauchy–Schwarz the total variation distance of the products is at most √(1−ρ^{2n}), bounded away from 1. A consistent estimator at both G₀ and G₁ would give a vanishing-error test (pick the nearer of the two laws), contradiction. In particular the order b_n∼const·n^{1/3} does not suffice.
