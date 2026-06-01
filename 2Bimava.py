#LEONAARDO ALMEIDA 1:logica matematica
def calcular_imc(p, a):
    """
    Função desenvolvida pelo Programador 1.
    Recebe:
        p (float): peso em quilogramas (ex: 75.0)
        a (float): altura em metros (ex: 1.75)
    retorna:
        o valor do IMC calculado (peso / altura**2)
    """
    imc = p / (a ** 2)
    return imc
#kennedy 2: classificação de dados
def classificar(valor_imc):
    if valor_imc < 25:
        return"normal"
    else:
        return"acima do peso"
#Breno 3: especialista em Conteúdo ---
def gerar_aviso(status):
    """
    Recebe o status (texto) e retorna uma recomendação de saúde personalizada
    """
    if status
