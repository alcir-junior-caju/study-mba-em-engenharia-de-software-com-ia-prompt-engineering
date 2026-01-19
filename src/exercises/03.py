"""Script de exemplo 03 - Lista de Tarefas."""

print("=" * 50)
print("EXERCÍCIO 03: Lista de Tarefas")
print("=" * 50)
print()

tarefas = []

while True:
    print("\n📝 Menu:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print(f"✓ Tarefa '{tarefa}' adicionada!")

    elif opcao == "2":
        print("\n📋 Suas tarefas:")
        if not tarefas:
            print("  (Nenhuma tarefa cadastrada)")
        else:
            for i, tarefa in enumerate(tarefas, 1):
                print(f"  {i}. {tarefa}")

    elif opcao == "3":
        if not tarefas:
            print("✗ Não há tarefas para remover!")
        else:
            print("\n📋 Suas tarefas:")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"  {i}. {tarefa}")

            try:
                indice = int(input("\nDigite o número da tarefa a remover: ")) - 1
                if 0 <= indice < len(tarefas):
                    tarefa_removida = tarefas.pop(indice)
                    print(f"✓ Tarefa '{tarefa_removida}' removida!")
                else:
                    print("✗ Número inválido!")
            except ValueError:
                print("✗ Digite um número válido!")

    elif opcao == "4":
        print("\n👋 Até logo!")
        break

    else:
        print("✗ Opção inválida!")
