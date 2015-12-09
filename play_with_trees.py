# optimal
source = '''         - z[s] + etree.values[s]   | z[s]
                     - e[s] + a/(a+c)*E[ e[x]   | x in S(s)] + 1.0/(a+c)*(z[s]-f[s]) | e[s]
len(s)==1:           - Gamma[s] + (e[s]-estar)                                    | Gamma[s]
len(s)>1:            - Gamma[s] + a/(a+c)*Gamma[P(s)] + beta**t*(e[s]-estar)      | Gamma[s]
len(s)==1:           - Gamma[s] + E[ Gamma[x] | x in S(s) ] + psi[s] - phi[s]     | f[s]
1<len(s)<len(etree): - Gamma[s] + E[ Gamma[x] | x in S(s) ] + psi[s] - phi[s]     | f[s]
len(s)==len(etree):  - f[s]                                                       | f[s]
                     - psi[s] + 1000*( Sum[f[x] | x in H(s)] - Rbar  )             | 0 <= psi[s]
                     - phi[s] + (-(f[s]-min_f))*1000                              | 0 <= phi[s]
'''


# peg
source_2 = """

                     - z[s] + etree.values[s] | z[s]
                     - e[s] + a/(a+c)*E[ e[x] | x in S(s)] + 1.0/(a+c)*(z[s]-f[s]) | e[s]
len(s)==1:           - Gamma[s] + (e[s]-estar)                                 |    Gamma[s]
len(s)>1:            - Gamma[s] + a/(a+c)*Gamma[P(s)] + beta**t*(e[s]-estar)   |    Gamma[s]
len(s)<len(etree):   - e[s] + z[s]/c*(1-kappa) + psi[s]                     | f[s]
len(s)==len(etree):  - f[s]                                                | f[s]
                     - phi[s] + (-(f[s]-min_f))*1000                            | phi[s]
                     - psi[s] + ( Sum[ f[x] | x in H(s) ] - Rbar)*1000 |  0 <= psi[s]

"""

# volume
source_3 = """

                     - z[s] + etree.values[s] | z[s]
                     - e[s] + a/(a+c)*E[ e[x] | x in S(s)] + 1.0/(a+c)*(z[s]-f[s]) | e[s]
len(s)==1:           - Gamma[s] + (e[s]-estar)                                 |    Gamma[s]
len(s)>1:            - Gamma[s] + a/(a+c)*Gamma[P(s)] + beta**t*(e[s]-estar)   |    Gamma[s]
len(s)<len(etree):   - f[s] + kappa*z[s] - psi[s]                   | f[s]
len(s)==len(etree):  -f[s]                                                | f[s]
                     -phi[s] + (-(f[s]-min_f))*1000                            | phi[s]
                     -psi[s] + ( Sum[ f[x] | x in H(s) ] - Rbar)*1000 |  0 <= psi[s]

"""



from pattern import *
