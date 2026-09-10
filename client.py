class FRIProximityTester:
    """
    FRI (Fast Reed-Solomon Interactive Oracle Proof of Proximity).
    Successively folds polynomial evaluations by half using random challenge alpha.
    """
    def __init__(self):
        pass

    def fold_codeword(self, evaluations, alpha):
        # Splits evaluation into even/odd parts:
        # f_folded(x^2) = f_even(x) + alpha * f_odd(x)
        half = len(evaluations) // 2
        folded = []
        for i in range(half):
            f_even = (evaluations[2 * i] + evaluations[2 * i + 1]) / 2.0
            f_odd = (evaluations[2 * i] - evaluations[2 * i + 1]) / 2.0
            folded.append(round(f_even + alpha * f_odd, 4))
        return folded

    def full_fri_commit_rounds(self, initial_evals, alphas):
        layers = [initial_evals]
        curr = initial_evals
        for alpha in alphas:
            if len(curr) <= 1:
                break
            curr = self.fold_codeword(curr, alpha)
            layers.append(curr)
        return layers
