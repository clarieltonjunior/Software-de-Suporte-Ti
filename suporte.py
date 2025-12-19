import time
import webbrowser
from base_problemas import problemas_simples, problemas_avancados

LINK_PAGAMENTO = "www.google.com"

def limpar():
    print("\n" * 50)

def menu():
    print("===== SUPORTE DIGITAL =====")
    print("1 - Problemas simples")
    print("2 - Problemas avançados (vai ao técnico digital R$17,99)")
    print("3 - Falar direto com técnico digital (WhatsApp R$17,99)")
    print("4 - Sair")
    return input("Escolha: ")

def listar_problemas(dic):
    print("\nProblemas disponíveis:")
    for i, p in enumerate(dic.keys(), start=1):
        print(f"{i} - {p}")

def escolher_problema(dic):
    listar_problemas(dic)
    escolha = input("\nNúmero: ")

    try:
        escolha = int(escolha)
        chave = list(dic.keys())[escolha - 1]
        return chave
    except:
        return None

def pagamento():
    print("\n💳 Para falar diretamente com o tecnico é necessario pagar R$ 17,99.")
    pagar = input("Abrir pagamento? (s/n): ")

    if pagar == "s":
        webbrowser.open(LINK_PAGAMENTO)
        print("Aguardando confirmação...")
        time.sleep(3)
        return True
    return False

def falar_com_tecnico(problema):
    print("\n📲 Atendimento digital – preciso dos seus dados.")
    nome = input("Seu nome: ")
    tel = input("Telefone/WhatsApp: ")

    with open("chamados.txt", "a") as arq:
        arq.write(f"Nome: {nome} | Telefone: {tel} | Problema: {problema}\n")

    print("\nChamado aberto com sucesso!")
    print("👉 Fale com o técnico digital:")
    print("https://wa.me/47996621559")
    time.sleep(30)

def iniciar():
    while True:
        limpar()
        opcao = menu()

        # SIMPLES
        if opcao == "1":
            problema = escolher_problema(problemas_simples)

            if problema is None:
                print("Opção inválida!")
                time.sleep(1)
                continue

            print("\nSolução recomendada:")
            print(problemas_simples[problema])

            ajuda = input("\nAjudou? (s/n): ")

            if ajuda == "n":
                if pagamento():
                    falar_com_tecnico(problema)

            input("\nENTER para voltar...")

        # AVANÇADOS
        elif opcao == "2":
            problema = escolher_problema(problemas_avancados)

            if problema is None:
                print("Opção inválida!")
                time.sleep(1)
                continue

            if pagamento():
                falar_com_tecnico(problema)

        # CONTATO DIRETO
        elif opcao == "3":
            if pagamento():
                falar_com_tecnico("contato direto")

        elif opcao == "4":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")
            time.sleep(1)

iniciar()
