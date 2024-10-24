def calcular_soma():
    INDICE = 12
    SOMA = 0
    K = 1
    
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    
    return SOMA

resultado = calcular_soma()
print(f"O valor final de SOMA é: {resultado}")
# A resposta é 77