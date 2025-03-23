import ast

def corrige_emails(emails):
    """
    Recebe uma lista de emails e retorna uma lista com os emails corrigidos.
    Um email é considerado correto se contém a string "@usp.br" em algum lugar.
    Caso o email não seja correto, a função deve retornar a string "ERRO".
    :param emails: lista de emails
    :return: lista de emails corrigidos
    """
    emailsFix = []
    for email in emails:
        emailHalf = len(email) // 2
        emailLeft = email[:emailHalf]
        emailRight = email[emailHalf:]
        emailUnion = emailLeft[::-1] + emailRight[::-1]
        if "@usp.br" in emailUnion: emailsFix.append(emailUnion)  
        else: emailsFix.append("ERRO")           
    return emailsFix

try:
    input = input("Input: ")
    print("\n")
    print(eval(input))
except:
    print("Erro: Entrada inválida.")
