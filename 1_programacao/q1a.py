def cifra(text: str, number: int) -> str:
    """
    Função que decifra e cifra um texto usando a cifra de César. 
    Para tal, usa-se o número decimal ASCII de cada letra do texto e desloca-a um número de posições dado pelo parâmetro number.

    Args:
        text (str): Texto a ser decifrado/cifrado.
        number (int): Número de posições que cada letra será deslocada.

    Returns:
        str: Texto decifrado/cifrado.

    Observações:
        O operador % faz com que o resultado da soma não ultrapasse o número de letras do alfabeto e permite a operação cíclica.
        Input deve ser da forma cifra("texto", n) ou "texto", n em que n é um número inteiro.
    """
    result = ""
    for letter in text:
        if letter.isascii() and letter.isalpha() and letter != "ç" and letter != "Ç":
            numberOfLetters = 26
            initLetterCode = ord("a") if letter.islower() else ord("A")
            newLetter = chr(initLetterCode + (ord(letter) + number - initLetterCode) % numberOfLetters)
            result += newLetter
        elif letter == "ç" or letter == "Ç":
            result += letter
        else:
            result += letter
    return result

try:
    input = input("Input: ")
    print("/n")
    print(eval(input))
except:
    print("Erro: Entrada inválida.")