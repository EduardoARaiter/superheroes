class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.proximo = None

class AgendaHeroes:
    def __init__(self):
        self.tabela = [None] * 26

    def calcular_indice(self, letra):
        return ord(letra.upper()) - ord('A')

    def adicionar_contato(self, nome, telefone):
        indice = self.calcular_indice(nome[0])
        novo_contato = Contato(nome, telefone)

        if self.tabela[indice] is None:
            self.tabela[indice] = novo_contato
        else:
            atual = self.tabela[indice]
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_contato

    def buscar_contato(self, nome):
        indice = self.calcular_indice(nome[0])
        atual = self.tabela[indice]

        while atual is not None:
            if atual.nome == nome:
                return atual.telefone
            atual = atual.proximo

        return None

    def listar_contatos_por_letra(self, letra):
        indice = self.calcular_indice(letra)
        contatos = []

        atual = self.tabela[indice]
        while atual is not None:
            contatos.append((atual.nome, atual.telefone))
            atual = atual.proximo

        return contatos

    def remover_contato(self, nome):
        indice = self.calcular_indice(nome[0])
        atual = self.tabela[indice]
        anterior = None

        while atual is not None:
            if atual.nome == nome:
                if anterior is None:
                    self.tabela[indice] = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo

        return False

if __name__ == "__main__":
    agenda = AgendaHeroes()

    print("Bem-vindo ao Sistema da Agenda do Clube Secreto de Heróis!")

    while True:
        print("\nMenu:")
        print("1. Adicionar Super-Herói")
        print("2. Buscar Super-Herói")
        print("3. Mostrar Todos os Super-Heróis pela Letra")
        print("4. Remover Super-Herói")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do super-herói: ")
            telefone = input("Digite o telefone: ")
            agenda.adicionar_contato(nome, telefone)
            print("Super-Herói adicionado com sucesso.")
        elif escolha == '2':
            nome = input("Digite o nome do super-herói: ")
            telefone = agenda.buscar_contato(nome)
            if telefone:
                print(f"Telefone: {telefone}")
            else:
                print("Super-Herói não encontrado.")
        elif escolha == '3':
            letra = input("Digite a letra inicial: ")
            contatos = agenda.listar_contatos_por_letra(letra)
            if contatos:
                for nome, telefone in contatos:
                    print(f"Nome: {nome}, Telefone: {telefone}")
            else:
                print("Nenhum super-herói encontrado para esta letra.")
        elif escolha == '4':
            nome = input("Digite o nome do super-herói a ser removido: ")
            if agenda.remover_contato(nome):
                print("Super-Herói removido com sucesso.")
            else:
                print("Super-Herói não encontrado.")
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
