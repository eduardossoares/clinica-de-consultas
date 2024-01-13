import datetime

pacientes = []
consultas = []

def cadastrar_paciente():
    nome = input("Digite o nome do paciente: ")
    telefone = input("Digite o telefone do paciente: ")

    if any(p['telefone'] == telefone for p in pacientes):
        print("Paciente já cadastrado.")
    else:
        pacientes.append({'nome': nome, 'telefone': telefone})
        print("Paciente cadastrado com sucesso!")

def marcar_consulta():
    if not pacientes:
        print("Não existem pacientes cadastrados.")
        return

    nome = input("Digite o nome do paciente: ")
    paciente = next((p for p in pacientes if p['nome'] == nome), None)

    if paciente is None:
        print("Paciente não encontrado.")
        return

    data_hora_str = input("Digite a data e hora da consulta (formato: dd/mm/yyyy hh:mm): ")
    try:
        data_hora = datetime.datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M")
    except ValueError:
        print("Data ou hora inválida.")
        return

    if data_hora <= datetime.datetime.now():
        print("Não é possível agendar consultas retroativas.")
        return

    if any(c['data_hora'] == data_hora for c in consultas):
        print("Horário indisponível para consulta.")
    else:
        consultas.append({'paciente': paciente, 'data_hora': data_hora})
        print("Consulta marcada com sucesso!")

def cancelar_consulta():
    if not consultas:
        print("Não existem consultas agendadas.")
        return

    for i, c in enumerate(consultas):
        print(f"{i + 1}. {c['paciente']['nome']} - {c['data_hora'].strftime('%d/%m/%Y %H:%M')}")

    try:
        consulta_numero = int(input("Escolha o número da consulta que deseja cancelar: ")) - 1
        consulta = consultas[consulta_numero]

        print(f"Consulta marcada para {consulta['data_hora'].strftime('%d/%m/%Y %H:%M')} será cancelada.")
        confirmacao = input("Deseja realmente cancelar? (S/N): ")

        if confirmacao.lower() == "s":
            consultas.remove(consulta)
            print("Consulta cancelada com sucesso!")
    except (ValueError, IndexError):
        print("Número de consulta inválido.")

while True:
    print("\n----- MENU PRINCIPAL -----")
    print("1. Cadastrar paciente")
    print("2. Marcar consulta")
    print("3. Cancelar consulta")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        marcar_consulta()
    elif opcao == "3":
        cancelar_consulta()
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
