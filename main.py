import random

class SimuladorMemoria:
    def __init__(self, tamanhoMemoriaVirtual, tamanhoMemoriaFisica, tamanhoPagina):
        self.tamanhoMemoriaVirtual = tamanhoMemoriaVirtual
        self.tamanhoMemoriaFisica = tamanhoMemoriaFisica
        self.tamanhoPagina = tamanhoPagina

        self.numPaginasVirtuais = tamanhoMemoriaVirtual // tamanhoPagina
        self.numMoldurasFisicas = tamanhoMemoriaFisica // tamanhoPagina

        self.tabelaPaginas = [-1] * self.numPaginasVirtuais  # Inicializa com -1 (livre)
        self.memoriaFisica = [0] * self.numMoldurasFisicas   # Inicializa com 0 (livre)

        print(f"\nSimulador inicializado com {self.numPaginasVirtuais} páginas virtuais e {self.numMoldurasFisicas} molduras físicas.")
        self.mostrarTabelaPaginas()
        self.mostrarMemoriaFisica()

    def obterEnderecoFisico(self, enderecoVirtual):
        numeroPagina = enderecoVirtual // self.tamanhoPagina
        deslocamento = enderecoVirtual % self.tamanhoPagina

        print(f"\nProcessando endereço virtual {enderecoVirtual}: página {numeroPagina}, deslocamento {deslocamento}")

        numeroMoldura = self.tabelaPaginas[numeroPagina]
        
        if numeroMoldura == -1:
            if 0 in self.memoriaFisica:
                numeroMoldura = self.memoriaFisica.index(0)
                self.tabelaPaginas[numeroPagina] = numeroMoldura
                self.memoriaFisica[numeroMoldura] = 1
                print(f"Página {numeroPagina} mapeada para moldura {numeroMoldura}.")
                self.mostrarTabelaPaginas()
                self.mostrarMemoriaFisica()
            else:
                print("Erro: Memória física cheia")
                return None

        enderecoFisico = numeroMoldura * self.tamanhoPagina + deslocamento
        print(f"Endereço virtual {enderecoVirtual} mapeado para endereço físico {enderecoFisico}.")
        return enderecoFisico

    def simular(self, enderecosVirtuais):
        enderecosFisicos = []
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

# Obter parâmetros do usuário
tamanhoMemoriaVirtual, tamanhoMemoriaFisica, tamanhoPagina = obterInputUsuario()

# Inicialização do simulador
simulador = SimuladorMemoria(tamanhoMemoriaVirtual, tamanhoMemoriaFisica, tamanhoPagina)

# Geração de endereços virtuais aleatórios para simulação
enderecosVirtuais = [random.randint(0, tamanhoMemoriaVirtual - 1) for _ in range(10)]
print(f"\nEndereços virtuais gerados: {enderecosVirtuais}")

# Simulação
enderecosFisicos = simulador.simular(enderecosVirtuais)

# Exibição dos resultados
print("\nEndereços Físicos gerados durante a simulação:", enderecosFisicos)
print("\nTabela de Páginas Final:")
simulador.mostrarTabelaPaginas()
print("\nMemória Física Final:")
simulador.mostrarMemoriaFisica()
