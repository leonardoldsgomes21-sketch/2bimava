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
