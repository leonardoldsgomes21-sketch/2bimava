#LEONAARDO ALMEIDA 1:(logica matematica)
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
#kennedy 2: (classificação de dados)
def classificar(valor_imc):
    if valor_imc < 25:
        return "IDEAL"
    else:
        return "ACIMA DO PESO"
#Breno 3: (especialista em Conteúdo) 
def gerar_aviso(status):
    """
    Recebe o status (texto) e retorna uma recomendação de saúde personalizada
    """
    if status == "IDEAL":
        return "Òtimo! Mantenha seus hábitos saudáveis"
    elif status == "ACIMA DO PESO":
        return "Atenção: Considere buscar uma orientação médica"
    else:
        return "Status não reconhece."


# leonardo Leite 4:(engenheiro de integração)
def main():
    # fluxo principal do sistema: coleta dados, integra as funções e exibe o resultado
    print("--- bem-vindo ao avaliador de saude inteligente (HealthTech) ---")
    try:
        # solicita os dados ao usuario
        peso = float(input("Digite o seu peso (em kg, ex:70.5): "))
        altura = float(input("Digite a sua altura (em metros, ex:1.75): "))
        # execução do fluxo de dados
        resultado_imc = calcular_imc(peso, altura)
        status = classificar(resultado_imc)
        recomendacao = gerar_aviso(status)
        print(f"IMC: {resultado_imc:.2f} - Status: {status}")
        print(f"Recomendação: {recomendacao}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números para peso e altura.")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
             

