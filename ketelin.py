nome=(input(f"qual o nome o aluo?"))

primeira_nota = float( input(f"  coloque a primeira nota"))
segunda_nota = float( input(f"  coloque a segunda nota"))
terceira_nota = float( input(f"  coloque a terceira nota"))
soma = ((primeira_nota+segunda_nota+terceira_nota)/3)

if soma == 9 and 10:
    print(" exelente")
elif soma == 7 and 8.9:
    print("bom")
elif soma == 5 and 6.9:
    print(" regular")
elif soma == 3 and 4.9:
    print (" ruim")
elif soma== 0 and 2.9:
    print(" crítico")
else:
    print(" nota inválida")
    
