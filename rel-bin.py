#######################################################################
#  CLASSIFICAÇÃO DE RELAÇÕES COM ABSTRAÇÃO DE CONJUNTOS PARA NÚMEROS  #
#######################################################################

# Dado um conjunto A, o algoritmo calcula:
# - A x A
# - P(A x A)
#
# e classifica cada elemento de P(A x A) como uma relação
#
# OBS: este programa difere de 'rel.py' por abstrair conjuntos para números. Cada relação contida em A x A é abstraída
# para um número de acordo com os elementos que contém
#
# EX: Dado A x A = {(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)}, temos:
#
# -------------------------------------------------------------------------
# |                RELAÇÃO                |        BIN        |    DEC    |
# ------------------------------------------------------------------------|
# | R1 = {}                               |     000000000     |    0      |
# | R2 = {(1,1), (2,1), (3,2), (3,3)}     |     100100011     |    291    |
# | R3 = {(3,1), (3,3)}                   |     000000101     |    5      |
# | R4 = A x A                            |     111111111     |    511    |
# -------------------------------------------------------------------------


from base import bin_dec                             # Função de conversão de base 2 para base 10
from time import time

##########################################################################################################################

# Produto Cartesiano - A x A
def prod_cart(A):
    return [(a, b) for a in A for b in A]

##########################################################################################################################

# Partes de um conjunto - P(A)
def partes(conj):
    subs = [[]]

    for elem in conj:
        subs += [[elem] + sub for sub in subs]

    return subs

##########################################################################################################################

# Associa um número binário a uma relação R contida em A x B
def rel_bin(rel, pc):
    bin_num = "0"

    for par in pc:
        if par in rel:
            bin_num += "1"                           # Se o par estiver em R, acrescenta-se 1 para indicar presença
        else:
            bin_num += "0"                           # Senão, acrescenta-se 0 para indicar ausência

    return int(bin_num)

##########################################################################################################################

# Associa um número decimal a uma relação R contida em A x B
def rel_dec(rel, pc):
    return bin_dec(rel_bin(rel, pc))

##########################################################################################################################

# Verifica se um par está contido em uma relação R utilizando abstração de números
def contem_par(par, rel_num, conj):
    i = par[0]
    j = par[1]

    pc = prod_cart(conj)

    # Determinação de expoente por cálculos de progressões aritméticas com índices de matriz
    x = len(pc) - 1 - conj.index(j) - len(conj) * conj.index(i)

    # 1 * (2 ** x)
    par_num = 1 << x

    return par_num & rel_num == par_num

##########################################################################################################################

# Verifica se a relação é reflexiva
def reflexiva(rel, conj):
    pc = prod_cart(conj)

    rel_num = rel_dec(rel, pc)

    for elem in conj:
        par = (elem, elem)

        if not contem_par(par, rel_num, conj):
            return ''

    return 'R'

##########################################################################################################################

# Verifica se a relação é simétrica
def simetrica(rel, conj):
    pc = prod_cart(conj)

    rel_num = rel_dec(rel, pc)

    for a in conj:
        for b in conj:
            par1 = (a, b)
            par2 = (b, a)

            if contem_par(par1, rel_num, conj) and not contem_par(par2, rel_num, conj):
                return ''

    return 'S'

##########################################################################################################################

# Verifica se a relação é transitiva
def transitiva(rel, conj):
    pc = prod_cart(conj)

    rel_num = rel_dec(rel, pc)

    for a in conj:
        for b in conj:
            for c in conj:
                par1 = (a, b)
                par2 = (b, c)
                par3 = (a, c)

                if contem_par(par1, rel_num, conj) and contem_par(par2, rel_num, conj) and not contem_par(par3, rel_num, conj):
                    return ''

    return 'T'

##########################################################################################################################

# Classifica uma relação
def classificar(rel, conj):
    cls = reflexiva(rel, conj) + simetrica(rel, conj) + transitiva(rel, conj)

    if cls == "RST":
        cls += "E"

    return cls

##########################################################################################################################

# Função principal
def main():
    antes = time()                                                                       # Tempo inicial

    S = [1, 2, 3]
    SxS = prod_cart(S)
    P_SxS = partes(SxS)

    file = open("relacao-bin.txt", "w")
    file.write("S : {}\n".format(S))
    file.write("S x S : {}\n".format(SxS))
    file.write("P(S x S) : {}\n\n".format(P_SxS))
 
    for elem in P_SxS:
        file.write("{} : {}\n".format(elem, classificar(elem, S)))

    depois = time()                                                                      # Tempo final

    print(f"TEMPO = {depois - antes} s")                                                 # Tempo decorrido

main()

