def verifica_A(string):
    string = string.lower()
    
    contador = 0
    
    for i in string:
        if i == 'a':
            contador += 1
    
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vezes na string")
    else:
        print(f"A letra 'a' não está presente na string")

verifica_A("Etapa técnica")