###############################
#  CLASSIFICAÇÃO DE RELAÇÕES  #
###############################

# Dado um conjunto A, o programa calcula:
# 
# - A x A
# - P(A x A)
#
# e classifica cada elemento de P(A x A) como uma relação

from time import time

##############################################################################################################################################

# Produto cartesiano A x A
def prod_cart(conj):
    return [(a, b) for a in conj for b in conj]

##############################################################################################################################################

# Partes de um conjunto A
def partes(conj):
    particoes = [[]]

    for elem in conj:
        particoes += [[elem] + resto for resto in particoes]

    return particoes

##############################################################################################################################################

# Verificação de reflexividade de uma relação
def reflexiva(conj, rel):
    for a in conj:
        if (a, a) not in rel:
            return ""

    return "R"

##############################################################################################################################################

# Verificação de simetria de um relação
def simetrica(conj, rel):
    for a in conj:
        for b in conj:
            if (a, b) in rel and (b, a) not in rel:
                return ""

    return "S"

##############################################################################################################################################

# Verificação de transitividade de uma relação
def transitiva(conj, rel):
    for a in conj:
        for b in conj:
            for c in conj:
                if (a, b) in rel and (b, c) in rel and (a, c) not in rel:
                    return ""

    return "T"

##############################################################################################################################################

# Classificação de uma relação
def classificar(conj, rel):
    cls = reflexiva(conj, rel) + simetrica(conj, rel) + transitiva(conj, rel)

    if cls == "RST":
        cls += "E"

    return cls

##############################################################################################################################################

# Função principal
def main():
    antes = time()                                                                       # Tempo inicial

    S = [1, 2, 3]
    SxS = prod_cart(S)
    P_SxS = partes(SxS)

    file = open("relacao.txt", "w")
    file.write("S : {}\n".format(S))
    file.write("S x S : {}\n".format(SxS))
    file.write("P(S x S) : {}\n\n".format(P_SxS))
 
    for elem in P_SxS:
        file.write("{} : {}\n".format(elem, classificar(S, elem)))

    depois = time()                                                                      # Tempo final

    print(f"TEMPO = {depois - antes} s")                                                 # Tempo decorrido

main()
