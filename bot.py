def exibir_menu():
    print("\n"+"="*50)
    print("Assistente Virtual - tec Info RDS")
    print("=" * 50)
    print("Digite sua dúvida ou escolha uma opção: ")
    print("📜 'menu' - Ver tópicos disponíveis")
    print("❓ 'ajuda' - Como usar este assistente")
    print("🚪 'sair' - Encerrar atemdimento")

def listar_topicos():
    print("📃 Tópicos disponíveis")
    print("✅ Variáveis e tipos de dados")
    print("✅ Estrutura condicionais (if/else)")
    print("✅ Laços e repetições (for/while)")
    print("✅ Listas e manipulação")
    print("✅ Funções") 
    print("✅ Importar bibliotecas\n")

def buscar_respostas(pergunta):
    respostas = {
        "Variável":{
            "texto": "Variável armazenam informções em Python, basta atribuir um valor: ",
            "exemplo": "Nome = 'João' \nidade = 17\naltura = 1.75"
        },
        "if": {
            "texto": "Condicionais permitem executar código baseado em condições.",
            "exemplo": "\nif x > 10:\n    print('Maior que 10')"
        },
        "for": {
            "texto": "Laços repetem código várias vezes.",
            "exemplo": "\nfor i in range(5):\n    print(i)"
        },
        "Listas": {
            "texto": "Uma lista em Python é uma estrutura de dados que armazena uma coleção de elementos em uma ordem específica. Esses elementos podem ser de tipos diferentes, como números, strings, ou até outras listas.",
            "exemplo": "\nlista = [1, 2, 3, 4, 5]\n     print(lista)"
        },
        "Funções": {
            "texto": "Uma função é um bloco de código que executa uma tarefa específica e pode ser reutilizado várias vezes. Ela ajuda a organizar seu programa, evitar repetição de código e facilitar a manutenção.",
            "exemplo": "\ndef soma(a, b):\n    return a + b"
        },
        "Bibliotecas": {
            "texto": "Uma biblioteca é um conjunto de códigos já prontos (funções, classes, métodos) que você pode usar no seu programa para facilitar tarefas específicas, sem precisar programar tudo do zero.",
            "exemplo": "\nimport math\nprint(math.sqrt(16))"
        }
    }

    #procurar por palavras-chave no objeto respostas
    for chave, conteudo in respostas.itens():
        if chave in pergunta :
            print(f"\n{conteudo['texto']}")
            print(f"\n Exemplo:\n{conteudo['exemplo']}\n")
            return True #encontrou resposta
    return False #não encontrou resposta
