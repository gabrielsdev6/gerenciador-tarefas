tarefas = []

while True:
    print("Bem-vindo ao gerenciador de tarefas1")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        while True:
            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")
            resposta = input("Deseja adicionar outra tarefa? (s/n)")
            if resposta.lower() != "s":
                break
    elif escolha == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("Tarefas cadastradas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
    elif escolha == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa para remover.")
        else:
            print("Tarefas cadastradas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
            try:
                indice = int(input("Digite o numero da tarefa para remover: "))
                tarefas.pop(indice - 1)
                print("Tarefa removida com sucesso!")
            except (ValueError, IndexError):
                print("Número inválido. Tente novamente.")
    elif escolha == "4":
        print("Saindo do gerenciador de tarefas. Até mais!")
        break