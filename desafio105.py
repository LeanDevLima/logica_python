def notas(*notas, situacao=False):
    """
    Analisa notas de alunos e retorna informações detalhadas em um dicionário.

    :param notas: Uma ou mais notas dos alunos (aceita vários valores).
    :param situacao: (opcional) Indica se deve incluir a situação da turma.
    :return: Um dicionário com as seguintes informações:
        - Quantidade de notas
        - Maior nota
        - Menor nota
        - Média da turma
        - Situação (se solicitado)
    """
    resultado = {}
    resultado['Quantidade'] = len(notas)
    resultado['Maior nota'] = max(notas) if notas else None
    resultado['Menor nota'] = min(notas) if notas else None
    resultado['Média'] = sum(notas) / len(notas) if notas else 0
    
    if situacao:
        if resultado['Média'] >= 7:
            resultado['Situação'] = 'Boa'
        elif 5 <= resultado['Média'] < 7:
            resultado['Situação'] = 'Razoável'
        else:
            resultado['Situação'] = 'Ruim'
    
    return resultado


# Programa principal
dados = notas(5.5, 7.8, 6.2, situacao=True)
print(dados)
