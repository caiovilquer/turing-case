def organiza_listas(numberOfProjects, episodes, minimumTime):
    """
    Recebe uma lista de episódios e retorna uma lista com os episódios organizados.
    Um episódio é considerado correto se contém o número mínimo de minutos.
    Caso o episódio não seja correto, a função deve retornar a string "ERRO".

    Args:
        numberOfProjects (int): Número de projetos.
        episodes (list): Lista de episódios.
        minimumTime (int): Número mínimo de minutos que cada projeto deve ter.

    Returns:
        tuple: Dicionário com os projetos organizados e uma string indicando se os projetos estão ordenados ("sim" ou "nao").
    """
    
    projects = projectsCasing(numberOfProjects, episodes)
    projects = checkProjectsOrder(projects)
    projects = checkProjectsTime(projects, minimumTime)
    if all(projects[x]== [] for x in range (1, numberOfProjects)):
        status = "nao"
    else:
        status = "sim"
    return projects, status

def projectsCasing(numberOfProjects, episodes):
    """
    Recebe o número de projetos e uma lista de episódios e retorna um dicionário com os projetos organizados.

    Args:
        numberOfProjects (int): Número de projetos.
        episodes (list): Lista de episódios.

    Returns:
        dict: Dicionário com os projetos organizados.
    """
    
    projects = {}
    for i in range(1, numberOfProjects + 1):
        projects[i] = []
    for episode in episodes:
        projects[episode[0]].append(episode)
    return projects

def sortedTest(sequence):
    """
    Recebe uma lista de episódios e retorna True se a lista estiver ordenada e False caso contrário.

    Args:
        sequence (list): Lista de episódios.

    Returns:
        bool: True se a lista estiver ordenada, False caso contrário.

    Observações:
        A função funciona em O(n) pois não precisa ordenar a lista original.
    """
    
    return all(sequence[i] <= sequence[i + 1] for i in range(len(sequence) - 1))

def checkProjectsTime(projects, minimumTime):
    """
    Recebe um dicionário com os projetos e um número mínimo de minutos e checa se os projetos possuem o número mínimo de minutos.

    Args:
        projects (dict): Dicionário com os projetos.
        minimumTime (int): Número mínimo de minutos.

    Returns:
        dict: Dicionário com os projetos que possuem o número mínimo de minutos.
    """
    
    for key in projects:
        time = 0
        for episode in projects[key]:
            time += episode[2]
        if time < minimumTime:
            projects[key] = []
    return projects

def checkProjectsOrder(projects):
    """
    Recebe um dicionário com os projetos e checa se os episódios estão ordenados.

    Args:
        projects (dict): Dicionário com os projetos.

    Returns:
        tuple: Dicionário com os projetos ordenados e uma string indicando se os projetos estão ordenados ("sim" ou "nao").
    """
    
    for key in projects:
        sequence = []
        for episode in projects[key]:
            sequence.append(episode[1])
        if not sortedTest(sequence):
            projects = {key: [] for key in projects}
            return projects
    return projects

try:
    input = input("Input:")
    print("\n")
    result, status = (eval(input))
    print(f"Output: ({status}, ", end="")
    for key in result:
        print(f"{result[key]}, ")
    print(")")
except:
    print("Erro: Entrada inválida.")
