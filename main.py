def main():
    print("--------------PROGRAMA DE CONVERSÃO DE UNIDADES--------------")
print("Escolha a base da unidade que deseja converter")
op1 = int(input("""
( 1 ) Decimal
( 2 ) Binário
( 3 ) Octal
( 4 ) Hexadecimal
 """))
if op1 == 1:
    d = int(input("A base escolhida foi Decimal, agora, digite um número inteiro qualquer: "))
    opd = int(input("""Para qual das seguintes bases deseja converter?
    ( 1 ) Binário
    ( 2 ) Octal
    ( 3 ) Hexadecimal
     """))
    if opd == 1:
        print(f"{d} convertido em binário vale: {bin(d)[2:]}")
    elif opd == 2:
        print(f"{d} convertido em octal vale: {oct(d)[2:]}")
    elif opd == 3:
        print(f"{d} convertido em hexadecimal vale: {hex(d)[2:]}")
    else:
        print("Opção inválida.")
if op1 == 2:
    b = input("A base escolhida foi Binário, agora, digite um número em binário qualquer: ")
    dec1 = int(b, 2)
    opb = int(input("""Para qual das seguintes bases deseja converter?
    ( 1 ) Decimal
    ( 2 ) Octal
    ( 3 ) Hexadecimal
     """))
    if opb == 1:
        dec = int(b, 2)
        print(f"{b} convertido em decimal vale: ", dec)
    elif opb == 2:
        print(f"{b} convertido em octal vale: {oct(dec1)[2:]}")
    elif opb == 3:
        print(f"{b} convertido em hexadecimal vale: {hex(dec1)[2:]}")
    else:
        print("Opção inválida.")
if op1 == 3:
    o = input("A base escolhida foi Octal, agora digite um número em Octal qualquer: ")
    dec2 = str(int(o, 8))
    opo = int(input("""Para qual das seguintes bases deseja converter?
    ( 1 ) Binário
    ( 2 ) Decimal
    ( 3 ) Hexadecimal
     """))
    if opo == 1:
        dec3 = str(int(o, 8))
        dec4 = int(dec3)
        print(f"{o} convertido em binário vale: {bin(dec4)[2:]}")
    elif opo == 2:
        print(f"{o} convertido em decimal vale: {dec2}")
    elif opo == 3:
        dec3 = int(dec2)
        print(f"{o} convertido em hexadecimal vale: {hex(dec3)[2:]}")
    else:
     print("Opção inválida.")
if op1 == 4:
    h = input("A base escolhida foi Hexadecimal, agora digite um número em Hexadecimal qualquer: ")
    dec3 = int(h, 16)
    oph = int(input("""Para qual das seguintes bases deseja converter?
    ( 1 ) Binário
    ( 2 ) Decimal
    ( 3 ) Octal
     """))
    if oph == 1:
        print(f"{h} convertido em binário vale: {bin(dec3)[2:]}")
    elif oph == 2:
        print (f"{h} convertido em decimal vale: {str(dec3)}")
    elif oph == 3:
        print (f"{h} convertido em octal vale: {oct(dec3)[2:]}")
    else:
        print("Opção inválida.")

main()