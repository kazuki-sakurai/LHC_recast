import sympy as sy

def get_S95(b0, sigma):

    S95 = sy.Symbol('S95', positive = True, real = True)
    b = sy.Symbol('b', positive = True)
    chi21 = sy.Symbol('chi21')
    chi22 = sy.Symbol('chi22')

    chi2 = 3.84
    N = b0 

    replacements = [(b, (b0 - S95 - sigma**2)/2 + 1./2*((b0 - S95 - sigma**2)**2 + 4*(sigma**2*N - S95*sigma**2 + S95*b0))**0.5)]

    replacements2 = [(S95, 0.)]

    chi21 = -2*( N*sy.log(S95 + b) - (S95 + b) - ((b-b0)/sigma)**2)

    chi21 = chi21.subs(replacements)
    chi22 = chi21.subs(replacements2)

    eq = chi2 - chi21 + chi22

    S95_new = sy.nsolve(eq, S95, 1)

    return float(S95_new)
