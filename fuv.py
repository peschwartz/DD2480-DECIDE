'''
The Final Unlocking Vector (FUV) is generated from the Preliminary Unlocking Matrix. The
input PUV indicates whether the corresponding LIC is to be considered as a factor in signaling
interceptor launch. FUV[i] should be set to true if PUV[i] is false (indicating that the associated
LIC should not hold back launch) or if all elements in PUM row i are true.
'''
def compute_fuv_from_pum(puv, pum):
    fuv = [False] * len(pum)
    for i in range(len(pum)):
        fuv[i] = (not puv[i]) or all(pum[i])
    return fuv
