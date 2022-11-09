###################################################################
#  ALGORITMO DE CONVERSÃO DE BASES NUMÉRICAS - DEC, BIN, OCT, HEX #
###################################################################

# --------------------------------
# DEC -> XXX
# --------------------------------


# DEC -> BIN
def dec_bin(dec_num):                              # O algoritmo decompõe o número em grupos de 2^n elementos
    bin_num = ""

    while dec_num:
        bin_num += str(dec_num % 2)                # Armazena o resto das divisões
        dec_num //= 2

    bin_num = "0" + bin_num[::-1]                  # E inverte a ordem dos dígitos (adiciona 0 em caso de 'dec_num' nulo)

    return int(bin_num)


# DEC -> OCT
def dec_oct(dec_num):                              # O algoritmo decompõe o número em grupos de 8^n elementos
    oct_num = ""

    while dec_num:
        oct_num += str(dec_num % 8)                # Armazena o resto das divisões
        dec_num //= 8

    oct_num = "0" + oct_num[::-1]                  # E inverte a ordem dos dígitos (adiciona 0 em caso de 'dec_num' nulo)

    return int(oct_num)


# DEC -> HEX
def dec_hex(dec_num):                              # O algoritmo decompõe o número em grupos de 16^n elementos
    if not dec_num:
        return "0"                                 # Se o número é nulo, retorna 0

    hex_num = ""

    while dec_num:
        hex_num += hex_encode(str(dec_num % 16))   # Armazena o resto das divisões
        dec_num //= 16

    hex_num = hex_num[::-1]                        # E inverte a ordem dos dígitos

    return hex_num


# --------------------------------
# BIN -> XXX
# --------------------------------


# BIN -> DEC
def bin_dec(bin_num):
    bin_list = [int(i) for i in str(bin_num)]      # Lista de digitos BIN

    dec_num = 0                                    # Número inicial: 0
    base = 2 ** (len(bin_list) - 1)                # Base inicial: 2 ^ (TAMANHO - 1)

    for b in bin_list:
        dec_num += b * base
        base //= 2                                 # Reduz a base pela metade

    return dec_num


# BIN -> OCT
def bin_oct(bin_num):
    return dec_oct(bin_dec(bin_num))               # BIN -> DEC -> OCT


# BIN -> HEX
def bin_hex(bin_num):
    return dec_hex(bin_dec(bin_num))               # BIN -> DEC -> HEX


# --------------------------------
# OCT -> XXX
# --------------------------------


# OCT -> BIN
def oct_bin(oct_num):
    return dec_bin(oct_dec(oct_num))               # OCT -> DEC -> BIN


# OCT -> DEC
def oct_dec(oct_num):
    oct_list = [int(i) for i in str(oct_num)]      # Lista de digitos OCT

    dec_num = 0                                    # Número inicial: 0
    base = 8 ** (len(oct_list) - 1)                # Base inicial: 8 ^ (TAMANHO - 1)

    for b in oct_list:
        dec_num += b * base
        base //= 8                                 # Reduz a base por 1 / 8

    return dec_num


# OCT -> HEX
def oct_hex(oct_num):
    return dec_hex(oct_dec(oct_num))               # OCT -> DEC -> HEX


# --------------------------------
# HEX -> XXX
# --------------------------------


# HEX -> BIN
def hex_bin(hex_num):
    return dec_bin(hex_dec(hex_num))               # HEX -> DEC -> BIN


# HEX -> OCT
def hex_oct(hex_num):
    return dec_oct(hex_dec(hex_num))               # HEX -> DEC -> OCT


# HEX -> DEC
def hex_dec(hex_num):
    hex_list = [i for i in str(hex_num)]           # Lista de digitos HEX

    dec_num = 0                                    # Número inicial: 0
    base = 16 ** (len(hex_list) - 1)               # Base inicial: 16 ^ (TAMANHO - 1)

    for b in hex_list:
        b = hex_decode(str(b))
        dec_num += b * base
        base //= 16                                # Reduz a base por 1 / 16

    return dec_num


# -------------------------------------------------------
# FUNÇÕES ESPECIAIS DE TRATAMENTO DE ALGARISMOS HEX 
# -------------------------------------------------------


# Decodificação de algarismos HEX
def hex_decode(digit):
    char = "ABCDEF"                                # Algarismos HEX alfabéticos

    if digit in "0123456789":                      # Algarismos HEX numéricos
        return int(digit)                          # Retorna o próprio número

    return 10 + char.find(digit.upper())           # Retorna o número que representa


# Encodificação para algarismos HEX
def hex_encode(num):
    char = "ABCDEF"                                # Algarismos HEX alfabéticos

    if int(num) >= 10:
        return char[int(num) % 10]                 # Retorna a letra que representa

    return str(num)                                # Retorna o próprio número

