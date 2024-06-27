import random

class SimuladorMemoria:
    def __init__(self, tamanhoMemoriaVirtual, tamanhoMemoriaFisica, tamanhoPagina):
        self.tamanhoMemoriaVirtual = tamanhoMemoriaVirtual
        self.tamanhoMemoriaFisica = tamanhoMemoriaFisica
        self.tamanhoPagina = tamanhoPagina

        # Define o número de páginas virtuais e molduras físicas com o operador de divisão inteira
        self.numPaginasVirtuais = tamanhoMemoriaVirtual // tamanhoPagina
        self.numMoldurasFisicas = tamanhoMemoriaFisica // tamanhoPagina

        self.tabelaPaginas = [-1] * self.numPaginasVirtuais  # Inicializa com -1 (livre)
        self.memoriaFisica = [0] * self.numMoldurasFisicas   # Inicializa com 0 (livre)

        print(f"\nSimulador inicializado com {self.numPaginasVirtuais} páginas virtuais e {self.numMoldurasFisicas} molduras físicas.")
        self.mostrarTabelaPaginas()
        self.mostrarMemoriaFisica()

    def obterEnderecoFisico(self, enderecoVirtual):

        # no da página = divisão inteira do endereço virtual pelo tamanho da página
        numeroPagina = enderecoVirtual // self.tamanhoPagina

        # deslocamento = resto da divisão do endereço virtual pelo tamanho da página
        deslocamento = enderecoVirtual % self.tamanhoPagina

        print(f"\nProcessando endereço virtual {enderecoVirtual}: página {numeroPagina}, deslocamento {deslocamento}")

        # busca moldura na tabela de páginas
        numeroMoldura = self.tabelaPaginas[numeroPagina]
        
        if numeroMoldura == -1:
            # verifica se há moldura livre na memória física
            if 0 in self.memoriaFisica:
                numeroMoldura = self.memoriaFisica.index(0)

                # mapeia a página para a moldura e marca a moldura como ocupada
                self.tabelaPaginas[numeroPagina] = numeroMoldura
                self.memoriaFisica[numeroMoldura] = 1

                print(f"Página {numeroPagina} mapeada para moldura {numeroMoldura}.")
                self.mostrarTabelaPaginas()
                self.mostrarMemoriaFisica()

            else:
                print("Erro: Memória física cheia")
                return None

        # endereco físico = (número da moldura * tamanho da página) + deslocamento
        enderecoFisico = numeroMoldura * self.tamanhoPagina + deslocamento
        print(f"Endereço virtual {enderecoVirtual} mapeado para endereço físico {enderecoFisico}.")
        return enderecoFisico

    def simular(self, enderecosVirtuais):
        # inicia vetor de endereços físicos
        enderecosFisicos = []

        # para cada endereço virtual, obtém o endereço físico correspondente e adiciona à lista
        for enderecoVirtual in enderecosVirtuais:
            enderecoFisico = self.obterEnderecoFisico(enderecoVirtual)
            if enderecoFisico is not None:
                enderecosFisicos.append(enderecoFisico)
        return enderecosFisicos

    def mostrarTabelaPaginas(self):
        print("Tabela de Páginas:")
        print(self.tabelaPaginas)
        print("Representação visual:")
        visualizacao = ['0'] * self.numPaginasVirtuais
        for i, moldura in enumerate(self.tabelaPaginas):
            if moldura != -1:
                visualizacao[i] = '1'
        print(f"[{' '.join(visualizacao)}]")

    def mostrarMemoriaFisica(self):
        print("Memória Física:")
        print(self.memoriaFisica)
        print("Representação visual:")
        visualizacao = ['0'] * self.numMoldurasFisicas
        for i, ocupado in enumerate(self.memoriaFisica):
            if ocupado == 1:
                visualizacao[i] = '1'
        print(f"[{' '.join(visualizacao)}]")

def obterInputUsuario():
    while True:
        try:
            tamanhoMemoriaVirtual = int(input("Digite o tamanho da memória virtual (em bits, potência de 2): "))
            tamanhoMemoriaFisica = int(input("Digite o tamanho da memória física (em bits, potência de 2): "))
            tamanhoPagina = int(input("Digite o tamanho da página (em bits, potência de 2): "))

            if tamanhoMemoriaVirtual <= 0 or tamanhoMemoriaFisica <= 0 or tamanhoPagina <= 0:
                raise ValueError("Os tamanhos devem ser maiores que zero.")

            if (tamanhoMemoriaVirtual % tamanhoPagina != 0) or (tamanhoMemoriaFisica % tamanhoPagina != 0):
                raise ValueError("Tamanho da página deve ser uma potência de 2 que divide igualmente os tamanhos de memória.")

            return tamanhoMemoriaVirtual, tamanhoMemoriaFisica, tamanhoPagina

        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, tente novamente.")

# coleta dos parâmetros
tamanhoMemoriaVirtual, tamanhoMemoriaFisica, tamanhoPagina = obterInputUsuario()

# criação do simulador com os parâmetros coletados
simulador = SimuladorMemoria(tamanhoMemoriaVirtual, tamanhoMemoriaFisica, tamanhoPagina)

# Gerando de endereços virtuais aleatórios para simulação
enderecosVirtuais = [random.randint(0, tamanhoMemoriaVirtual - 1) for _ in range(10)]
print(f"\nEndereços virtuais gerados: {enderecosVirtuais}")

# iniciando a simulação
enderecosFisicos = simulador.simular(enderecosVirtuais)

# Exibição dos resultados
print("\nEndereços Físicos gerados durante a simulação:", enderecosFisicos)
print("\nTabela de Páginas Final:")
simulador.mostrarTabelaPaginas()
print("\nMemória Física Final:")
simulador.mostrarMemoriaFisica()
