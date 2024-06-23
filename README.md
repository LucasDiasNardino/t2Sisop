# Simulador de Memória Paginada

Este é um simulador básico de memória paginada implementado em Python. O código simula o processo de mapeamento de endereços virtuais para endereços físicos usando tabelas de páginas e memória física paginada.

## Funcionamento

### Classes e Métodos

- **SimuladorMemoria**: Classe principal que inicializa o simulador com os parâmetros da memória virtual, física e o tamanho da página. Ela contém métodos para mapear endereços virtuais em físicos (`obterEnderecoFisico`), simular uma sequência de endereços virtuais (`simular`), e mostrar o estado atual da tabela de páginas e memória física (`mostrarTabelaPaginas` e `mostrarMemoriaFisica`).

- **obterEnderecoFisico**: Método que recebe um endereço virtual e realiza o mapeamento para um endereço físico, utilizando uma tabela de páginas e alocando espaço na memória física conforme necessário.

- **simular**: Método que simula uma sequência de endereços virtuais gerados aleatoriamente, utilizando o método `obterEnderecoFisico` para mapeá-los e retornar uma lista de endereços físicos resultantes.

### Representação Visual

- **mostrarTabelaPaginas**: Método que exibe a tabela de páginas como uma lista de números inteiros, onde cada número representa a moldura física associada a uma página virtual. Além disso, exibe uma representação visual entre colchetes `[ ]`, indicando se a página está mapeada (`1`) ou não (`0`).

- **mostrarMemoriaFisica**: Método que exibe a memória física como uma lista de `0`s e `1`s, onde cada posição representa se a moldura correspondente está ocupada (`1`) ou livre (`0`). Também exibe uma representação visual entre colchetes `[ ]`.

## Exemplo de Uso

Para utilizar o simulador, o usuário deve fornecer os seguintes parâmetros:

- Tamanho da memória virtual (em bits, potência de 2).
- Tamanho da memória física (em bits, potência de 2).
- Tamanho da página (em bits, potência de 2).

### Entradas de Exemplo

Aqui estão alguns exemplos de entradas que podem ser utilizadas para testar o simulador:

1. **Exemplo 1**:
   - Tamanho da memória virtual: 1024 bits (2^10)
   - Tamanho da memória física: 512 bits (2^9)
   - Tamanho da página: 64 bits (2^6)

2. **Exemplo 2**:
   - Tamanho da memória virtual: 2048 bits (2^11)
   - Tamanho da memória física: 1024 bits (2^10)
   - Tamanho da página: 128 bits (2^7)

## Como Executar

1. Clone o repositório para sua máquina local.
2. Execute o arquivo `simulador_memoria_paginada.py`.
3. Siga as instruções para inserir os parâmetros de memória virtual, física e tamanho da página.
4. Observe a saída que mostra a sequência de endereços físicos gerados, a tabela de páginas e o estado da memória física ao longo da simulação.
