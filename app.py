# app.py - Calculadora de IMC que roda no terminal
# Não depende de nenhum arquivo externo ou servidor web

# ============================================================================
# IMPORTAÇÃO DE MÓDULOS
# ============================================================================

# Importa o módulo sys para funções de sistema (como fechar o programa)
# sys.exit() permite encerrar o programa de forma controlada
import sys

# Importa o módulo os para funções do sistema operacional (limpar tela)
# os.system() executa comandos do terminal como 'cls' ou 'clear'
import os

# Importa o módulo time para pausas e animações
# time.sleep() cria delays (pausas) na execução do programa
import time

# ============================================================================
# FUNÇÕES DE UTILIDADE (SISTEMA E INTERFACE)
# ============================================================================

# Função para limpar a tela do terminal (funciona em diferentes sistemas)
def limpar_tela():
    """
    Limpa a tela do terminal
    os.name: 'nt' para Windows, 'posix' para Linux/Mac
    
    Esta função verifica qual sistema operacional está rodando
    e usa o comando apropriado para limpar a tela.
    """
    # Verifica se o sistema é Windows (NT - Windows NT/2000/XP/Vista/7/8/10/11)
    if os.name == 'nt':  # Sistema Windows
        # 'cls' é o comando do Windows para Clear Screen (limpar tela)
        os.system('cls')
    else:  # Linux, Mac, BSD e outros sistemas Unix-like
        # 'clear' é o comando do Unix/Linux para limpar tela
        os.system('clear')


# Função para exibir o cabeçalho da calculadora
def exibir_cabecalho():
    """
    Exibe um cabeçalho estilizado com o título da calculadora
    Usa caracteres especiais para fazer uma borda
    
    O cabeçalho é exibido no início de cada tela principal
    para manter a consistência visual do programa.
    """
    # = repetido 50 vezes cria uma linha dupla de separação
    print("=" * 50)
    # Título centralizado com espaços para ficar bonito visualmente
    print("     CALCULADORA DE ÍNDICE DE MASSA CORPORAL (IMC)")
    # Linha dupla de fechamento
    print("=" * 50)
    # Linha em branco para espaçamento (pula uma linha)
    print()


# ============================================================================
# FUNÇÕES DO MENU E NAVEGAÇÃO
# ============================================================================

# Função para mostrar o menu principal e opções
def exibir_menu():
    """
    Exibe as opções disponíveis ao usuário
    Retorna a opção escolhida pelo usuário como string
    
    Returns:
        str: A opção escolhida ('1', '2' ou '3')
    """
    # \n é caractere de nova linha, - repetido 40 vezes cria uma linha pontilhada
    print("\n" + "-" * 40)
    print("MENU PRINCIPAL:")
    # Cada print exibe uma opção diferente do menu
    print("1. Calcular IMC")
    print("2. Ver tabela de referência")
    print("3. Sair")
    print("-" * 40)
    
    # Solicita ao usuário que digite uma opção
    # input() sempre retorna uma string (texto)
    opcao = input("Escolha uma opção (1-3): ")
    # Retorna a opção para ser processada pela função main()
    return opcao


# Função para exibir a tabela de referência do IMC
def exibir_tabela_referencia():
    """
    Mostra a tabela completa da Organização Mundial da Saúde (OMS)
    com todas as faixas de IMC e seus respectivos riscos à saúde.
    
    A tabela serve como referência para o usuário entender
    onde seu IMC se encaixa e quais os riscos associados.
    """
    # Limpa a tela antes de exibir a tabela (evita poluição visual)
    limpar_tela()
    # Mostra o cabeçalho padrão do programa
    exibir_cabecalho()
    
    # Pula uma linha e mostra o título da tabela
    print("\nTABELA DE REFERÊNCIA DO IMC (Organização Mundial da Saúde):\n")
    
    # Linha superior da tabela (45 caracteres de hífen)
    print("-" * 45)
    # Cabeçalho da tabela com 3 colunas: Classificação, IMC e Risco
    print("|   Classificação    |    IMC     |   Risco    |")
    # Linha separadora após o cabeçalho
    print("-" * 45)
    
    # Cada linha da tabela com os valores de IMC e classificações
    # Os espaços servem para alinhar as colunas visualmente
    print("| Abaixo do peso     | < 18.5     |   Elevado  |")
    print("| Peso normal        | 18.5 - 24.9|   Baixo    |")
    print("| Sobrepeso          | 25.0 - 29.9|  Aumentado |")
    print("| Obesidade grau I   | 30.0 - 34.9|   Moderado |")
    print("| Obesidade grau II  | 35.0 - 39.9|   Severo   |")
    print("| Obesidade grau III | ≥ 40       |  Muito severo|")
    # Linha inferior da tabela
    print("-" * 45)
    
    # Explica a fórmula do IMC para o usuário
    print("\n📊 O IMC é calculado dividindo o peso (kg) pela altura (m) ao quadrado")
    print("Fórmula: IMC = peso ÷ (altura × altura)")
    
    # Aguarda o usuário pressionar ENTER antes de voltar ao menu
    # Isso permite que o usuário leia a tabela sem pressa
    input("\nPressione ENTER para voltar ao menu...")


# ============================================================================
# FUNÇÕES DE VALIDAÇÃO DE DADOS
# ============================================================================

# Função para validar se a entrada é um número positivo
def validar_numero(valor, tipo):
    """
    Valida se o valor fornecido é um número positivo válido e dentro de limites realistas
    
    Args:
        valor (str): O valor digitado pelo usuário (em formato texto)
        tipo (str): O tipo de dado sendo validado ("peso" ou "altura")
    
    Returns:
        float or None: Retorna o número convertido para float se válido,
                      ou None se inválido
    
    Esta função é fundamental para evitar erros no programa,
    pois garante que apenas dados válidos sejam processados.
    """
    try:
        # Tenta converter a string (texto) para float (número decimal)
        # Exemplo: "75.5" vira 75.5, "1.75" vira 1.75
        num = float(valor)
        
        # Verifica se o número é positivo e dentro de limites realistas
        if tipo == "peso":
            # Verifica se o peso é maior que zero
            if num <= 0:
                print("❌ Erro: O peso deve ser maior que zero!")
                return None
            # Verifica se o peso não é irrealisticamente baixo (menos de 10kg)
            elif num < 10:
                print("⚠️ Atenção: Peso muito baixo. Verifique se digitou corretamente!")
                return None
            # Verifica se o peso não é irrealisticamente alto (mais de 500kg)
            elif num > 500:
                print("⚠️ Atenção: Peso muito alto. Verifique se digitou corretamente!")
                return None
                
        elif tipo == "altura":
            # Verifica se a altura é maior que zero
            if num <= 0:
                print("❌ Erro: A altura deve ser maior que zero!")
                return None
            # Verifica se a altura não é irrealisticamente baixa (menos de 0.5m = 50cm)
            elif num < 0.5:
                print("⚠️ Atenção: Altura muito baixa. Verifique se digitou (ex: 1.75 para 1,75m)!")
                return None
            # Verifica se a altura não é irrealisticamente alta (mais de 2.8m)
            elif num > 2.8:
                print("⚠️ Atenção: Altura muito alta. Verifique se digitou corretamente!")
                return None
        
        # Se passou por todas as validações, retorna o número válido
        return num
        
    except ValueError:
        # Se não conseguiu converter para número (ex: usuário digitou "abc")
        # Exibe mensagem de erro específica
        print(f"❌ Erro: '{valor}' não é um número válido!")
        return None


# Função para obter e validar o peso do usuário
def obter_peso():
    """
    Solicita o peso ao usuário e retorna o valor válido
    
    Returns:
        float: O peso válido informado pelo usuário
    
    Esta função usa um loop infinito (while True) que só termina
    quando o usuário fornece um peso válido. Isso garante que o
    programa não prossiga com dados inválidos.
    """
    # Loop infinito - só sai quando receber um valor válido
    while True:
        try:
            # Solicita o peso ao usuário (input retorna string)
            peso_input = input("Digite seu peso em quilogramas (kg): ")
            # Chama a função de validação para verificar se o peso é válido
            peso = validar_numero(peso_input, "peso")
            
            # Se o peso NÃO for None (ou seja, é válido)
            if peso is not None:
                # Retorna o peso e sai da função (o loop termina)
                return peso
            # Se peso is None, a validação falhou e o loop continua
            # O usuário terá que digitar novamente
            
        except KeyboardInterrupt:
            # Captura a tecla Ctrl+C (interrupção do teclado)
            # Isso permite o usuário cancelar a operação de forma graciosa
            print("\n\nOperação cancelada pelo usuário.")
            # Encerra o programa completamente com código de saída 0 (sucesso)
            sys.exit(0)


# Função para obter e validar a altura do usuário
def obter_altura():
    """
    Solicita a altura ao usuário e retorna o valor válido
    
    Returns:
        float: A altura válida informada pelo usuário (em metros)
    
    Similar à função obter_peso(), mas para altura.
    """
    # Loop infinito até receber uma altura válida
    while True:
        try:
            # Solicita a altura ao usuário com exemplo de formato
            altura_input = input("Digite sua altura em metros (ex: 1.75): ")
            # Chama a função de validação para verificar se a altura é válida
            altura = validar_numero(altura_input, "altura")
            
            # Se a altura NÃO for None (ou seja, é válida)
            if altura is not None:
                # Retorna a altura e sai da função
                return altura
            # Se altura is None, a validação falhou e o loop continua
            
        except KeyboardInterrupt:
            # Captura Ctrl+C para sair graciosamente
            print("\n\nOperação cancelada pelo usuário.")
            sys.exit(0)


# ============================================================================
# FUNÇÕES DE CÁLCULO E CLASSIFICAÇÃO
# ============================================================================

# Função que calcula o IMC baseado no peso e altura
def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC)
    
    Args:
        peso (float): Peso em quilogramas (kg)
        altura (float): Altura em metros (m)
    
    Returns:
        float: IMC calculado e arredondado para 2 casas decimais
    
    Fórmula do IMC: peso / (altura * altura)
    O arredondamento para 2 casas decimais torna o resultado mais legível.
    """
    # Calcula o IMC usando a fórmula padrão
    # altura * altura é o mesmo que altura ** 2 (altura ao quadrado)
    imc = peso / (altura * altura)
    # round() arredonda o número para a quantidade especificada de casas decimais
    return round(imc, 2)


# Função que determina a classificação baseada no valor do IMC
def classificar_imc(imc):
    """
    Classifica o IMC de acordo com a tabela da Organização Mundial da Saúde (OMS)
    
    Args:
        imc (float): O valor do IMC calculado
    
    Returns:
        tuple: (classificacao, mensagem, cor)
            - classificacao (str): Nome da faixa de IMC (ex: "Peso normal")
            - mensagem (str): Recomendação personalizada para o usuário
            - cor (str): Código de cor ANSI para exibição no terminal
    
    As cores ANSI são usadas para destacar visualmente o resultado:
    - Códigos começam com \033[ e terminam com m
    - \033[92m = Verde (peso normal)
    - \033[93m = Amarelo (atenção)
    - \033[91m = Vermelho (crítico)
    - \033[0m = Reseta a cor (volta ao padrão)
    """
    # IMC menor que 16 - Magreza Grau III (crítico)
    if imc < 16:
        classificacao = "Magreza grau III"
        mensagem = "⚠️  Situação crítica! Procure um médico urgentemente!"
        cor = "\033[91m"  # Código ANSI para vermelho
    # IMC entre 16 e 16.9 - Magreza Grau II
    elif imc < 17:
        classificacao = "Magreza grau II"
        mensagem = "⚠️  Baixo peso severo. Consulte um nutricionista!"
        cor = "\033[91m"  # Vermelho
    # IMC entre 17 e 18.49 - Magreza Grau I
    elif imc < 18.5:
        classificacao = "Magreza grau I"
        mensagem = "⚠️  Você está abaixo do peso ideal. Busque orientação profissional!"
        cor = "\033[93m"  # Amarelo (atenção)
    # IMC entre 18.5 e 24.9 - Peso Normal (ideal)
    elif imc < 25:
        classificacao = "Peso normal"
        mensagem = "✅ Parabéns! Você está com o peso ideal. Mantenha hábitos saudáveis!"
        cor = "\033[92m"  # Verde (positivo)
    # IMC entre 25 e 29.9 - Sobrepeso
    elif imc < 30:
        classificacao = "Sobrepeso"
        mensagem = "⚠️  Atenção! Você está com sobrepeso. Considere melhorar hábitos alimentares!"
        cor = "\033[93m"  # Amarelo (atenção)
    # IMC entre 30 e 34.9 - Obesidade Grau I
    elif imc < 35:
        classificacao = "Obesidade grau I"
        mensagem = "⚠️  Obesidade moderada. Procure um médico e nutricionista!"
        cor = "\033[91m"  # Vermelho
    # IMC entre 35 e 39.9 - Obesidade Grau II
    elif imc < 40:
        classificacao = "Obesidade grau II"
        mensagem = "⚠️  Obesidade severa. É fundamental buscar ajuda médica!"
        cor = "\033[91m"  # Vermelho
    # IMC maior ou igual a 40 - Obesidade Grau III (mórbida)
    else:
        classificacao = "Obesidade grau III"
        mensagem = "🚨 URGENTE! Obesidade mórbida. Procure atendimento médico imediatamente!"
        cor = "\033[91m"  # Vermelho
    
    # Retorna os três valores como uma tupla
    return classificacao, mensagem, cor


# ============================================================================
# FUNÇÕES DE EXIBIÇÃO DE RESULTADOS
# ============================================================================

# Função para exibir o resultado do cálculo com detalhes
def exibir_resultado(peso, altura, imc, classificacao, mensagem, cor):
    """
    Exibe todos os resultados formatados de forma amigável e colorida
    
    Args:
        peso (float): Peso informado pelo usuário
        altura (float): Altura informada pelo usuário
        imc (float): IMC calculado
        classificacao (str): Classificação do IMC
        mensagem (str): Mensagem personalizada
        cor (str): Código de cor ANSI para destacar a classificação
    """
    # Linha dupla de destaque para o resultado
    print("\n" + "=" * 50)
    print("           RESULTADO DO CÁLCULO")
    print("=" * 50)
    
    # Mostra os dados de entrada (o que o usuário informou)
    print(f"\n📊 DADOS INFORMADOS:")
    # \n é nova linha, • é um bullet point para listagem
    print(f"   • Peso: {peso} kg")
    print(f"   • Altura: {altura} m")
    
    # Mostra o cálculo do IMC passo a passo (para educar o usuário)
    print(f"\n🔢 CÁLCULO DO IMC:")
    # Mostra a fórmula com os valores reais
    print(f"   • Fórmula: {peso} ÷ ({altura} × {altura})")
    # Calcula e mostra a altura ao quadrado (para transparência)
    # {altura * altura:.2f} formata com 2 casas decimais
    print(f"   • {peso} ÷ {altura * altura:.2f}")
    # Mostra o resultado final
    print(f"   • Resultado: {imc}")
    
    # Mostra a classificação com cor no terminal
    print(f"\n📋 CLASSIFICAÇÃO:")
    # Os códigos \033[ e \033[0m aplicam e resetam a cor
    # Isso faz o texto da classificação aparecer colorido
    print(f"   {cor}• {classificacao} - IMC: {imc}\033[0m")
    
    # Mostra a mensagem personalizada baseada na classificação
    print(f"\n💬 {mensagem}")
    
    # Mostra tabela de referência resumida para contexto
    print("\n" + "-" * 50)
    print("📌 TABELA DE REFERÊNCIA RÁPIDA:")
    print("   • Abaixo do peso: < 18.5")
    print("   • Peso normal: 18.5 - 24.9")
    print("   • Sobrepeso: 25.0 - 29.9")
    print("   • Obesidade: ≥ 30.0")
    print("-" * 50)


# ============================================================================
# FUNÇÕES DE PERSISTÊNCIA (HISTÓRICO E ESTATÍSTICAS)
# ============================================================================

# Função para salvar o resultado em um arquivo de histórico
def salvar_historico(peso, altura, imc, classificacao):
    """
    Salva o cálculo no arquivo historico_imc.txt para consulta futura
    
    Args:
        peso (float): Peso informado
        altura (float): Altura informada
        imc (float): IMC calculado
        classificacao (str): Classificação do IMC
    
    Returns:
        bool: True se salvou com sucesso, False se houve erro
    
    O arquivo de histórico permite que o usuário acompanhe
    sua evolução ao longo do tempo.
    """
    try:
        # Abre o arquivo em modo append (adicionar ao final)
        # 'a' = append - adiciona conteúdo sem apagar o existente
        # encoding='utf-8' suporta caracteres especiais (emoji, acentos)
        with open("historico_imc.txt", "a", encoding="utf-8") as arquivo:
            # Importa datetime dentro da função (só quando necessário)
            # Isso é mais eficiente que importar no topo se a função for raramente usada
            from datetime import datetime
            
            # Obtém data e hora atual e formata como string
            # %d = dia (01-31), %m = mês (01-12), %Y = ano (2024)
            # %H = hora (00-23), %M = minuto (00-59), %S = segundo (00-59)
            agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            # Escreve uma linha formatada com todos os dados no arquivo
            # \n no final cria uma nova linha para o próximo registro
            arquivo.write(f"[{agora}] Peso: {peso}kg | Altura: {altura}m | ")
            arquivo.write(f"IMC: {imc} | Classificação: {classificacao}\n")
        
        # Mensagem de sucesso para o usuário
        print("\n💾 Resultado salvo no histórico (historico_imc.txt)")
        return True  # Retorna True indicando sucesso
        
    except Exception as e:
        # Se houver qualquer erro (permissão de arquivo, disco cheio, etc.)
        # Mostra mensagem mas não interrompe o programa
        print(f"\n⚠️ Não foi possível salvar o histórico: {e}")
        return False  # Retorna False indicando falha


# Função para mostrar estatísticas do histórico
def mostrar_estatisticas():
    """
    Lê o arquivo de histórico e mostra estatísticas dos cálculos anteriores
    (quantidade de registros e últimos 10 cálculos)
    """
    try:
        # Tenta abrir o arquivo de histórico em modo leitura ('r')
        with open("historico_imc.txt", "r", encoding="utf-8") as arquivo:
            # readlines() lê todas as linhas do arquivo e retorna uma lista
            # Cada elemento da lista é uma linha do arquivo (como string)
            linhas = arquivo.readlines()
        
        # Verifica se o arquivo está vazio (nenhum registro)
        if not linhas:
            print("\n📭 Nenhum histórico encontrado. Faça alguns cálculos primeiro!")
            return  # Sai da função sem fazer mais nada
        
        # Cabeçalho da seção de histórico
        print("\n" + "=" * 50)
        print("        HISTÓRICO DE CÁLCULOS")
        print("=" * 50)
        
        # Mostra os últimos 10 registros (ou menos se tiver menos que 10)
        print("\n📜 ÚLTIMOS 10 REGISTROS:\n")
        # linhas[-10:] é slice (fatia) que pega do índice -10 até o final
        # Ou seja, as últimas 10 linhas da lista
        for linha in linhas[-10:]:  # Itera sobre cada uma das últimas 10 linhas
            # strip() remove espaços extras e quebras de linha no início e fim
            print(f"   {linha.strip()}")
        
        # Mostra total de registros (len() retorna o tamanho da lista)
        print(f"\n📊 Total de registros: {len(linhas)}")
        
    except FileNotFoundError:
        # Se o arquivo não existe (primeira execução do programa)
        print("\n📭 Nenhum histórico encontrado. Faça alguns cálculos primeiro!")


# ============================================================================
# FUNÇÕES DE EFEITOS VISUAIS (ANIMAÇÕES)
# ============================================================================

# Função para animação de carregamento (efeito visual)
def animar_calculando():
    """
    Mostra uma animação simples enquanto "calcula"
    Só para efeito visual (melhora a experiência do usuário)
    
    A animação cria a ilusão de que o programa está processando,
    tornando a experiência mais agradável.
    """
    # end="" faz o print NÃO pular linha após imprimir
    # Isso permite adicionar os pontos na mesma linha
    print("\nCalculando", end="")
    
    # range(3) cria uma sequência [0, 1, 2] - repete 3 vezes
    for _ in range(3):  # O _ é usado quando não precisamos do valor da iteração
        # time.sleep(0.3) pausa a execução por 0.3 segundos
        time.sleep(0.3)  # Pausa de 0.3 segundos entre cada ponto
        # end="" novamente para não pular linha
        print(".", end="")  # Imprime um ponto na mesma linha
        # Mais uma pausa de 0.3 segundos
        time.sleep(0.3)
    
    # Após os 3 pontos, imprime " Pronto!" e pula a linha (\n)
    print(" Pronto!\n")


# ============================================================================
# FUNÇÃO PRINCIPAL (CONTROLE DO PROGRAMA)
# ============================================================================

# Função principal que organiza o fluxo do programa
def main():
    """
    Função principal que controla o fluxo de execução do programa
    
    Esta função é o "cérebro" do programa - ela decide qual ação
    executar baseada na opção escolhida pelo usuário no menu.
    
    O fluxo é:
    1. Mostra menu
    2. Aguarda escolha do usuário
    3. Executa ação correspondente
    4. Volta ao passo 1 (exceto se escolher sair)
    """
    # Variável booleana para controlar se o programa deve continuar rodando
    # True = programa ativo, False = programa deve encerrar
    rodando = True
    
    # Loop principal do programa - só termina quando rodando for False
    while rodando:
        # Limpa a tela antes de cada exibição do menu
        # Isso mantém a interface limpa e organizada
        limpar_tela()
        # Mostra o cabeçalho padrão em cada tela
        exibir_cabecalho()
        
        # Exibe o menu e armazena a opção escolhida
        opcao = exibir_menu()
        
        # ============================================================
        # OPÇÃO 1: CALCULAR IMC
        # ============================================================
        if opcao == "1":
            # Limpa a tela para uma experiência mais limpa
            limpar_tela()
            # Mostra o cabeçalho novamente
            exibir_cabecalho()
            
            # Mensagem de boas-vindas ao cálculo
            print("\nVamos calcular seu IMC!")
            print("Digite os dados solicitados abaixo:\n")
            
            # Obtém o peso e altura (com validação automática)
            # As funções obter_peso() e obter_altura() só retornam
            # quando recebem valores válidos
            peso = obter_peso()
            altura = obter_altura()
            
            # Efeito visual de "processamento"
            animar_calculando()
            
            # Calcula o IMC chamando a função específica
            imc = calcular_imc(peso, altura)
            
            # Obtém a classificação, mensagem e cor baseadas no IMC
            # A função retorna uma tupla com 3 valores
            classificacao, mensagem, cor = classificar_imc(imc)
            
            # Exibe todos os resultados formatados
            exibir_resultado(peso, altura, imc, classificacao, mensagem, cor)
            
            # Pergunta se o usuário quer salvar no histórico
            # .lower() converte a resposta para minúscula (S/s -> s, N/n -> n)
            salvar = input("\n💾 Deseja salvar este resultado no histórico? (s/n): ").lower()
            # Verifica se a resposta começa com 's' (sim)
            if salvar == 's' or salvar == 'sim':
                salvar_historico(peso, altura, imc, classificacao)
            
            # Pergunta se o usuário quer ver o histórico
            ver_historico = input("\n📜 Deseja ver o histórico de cálculos? (s/n): ").lower()
            if ver_historico == 's' or ver_historico == 'sim':
                mostrar_estatisticas()
            
            # Aguarda o usuário pressionar ENTER antes de voltar ao menu
            # Isso dá tempo para ler os resultados
            input("\nPressione ENTER para continuar...")
        
        # ============================================================
        # OPÇÃO 2: VER TABELA DE REFERÊNCIA
        # ============================================================
        elif opcao == "2":
            # Chama a função que exibe a tabela completa da OMS
            exibir_tabela_referencia()
            # A função exibir_tabela_referencia() já tem seu próprio
            # input() para pausar, então não precisamos de outro
        
        # ============================================================
        # OPÇÃO 3: SAIR DO PROGRAMA
        # ============================================================
        elif opcao == "3":
            # Limpa a tela antes de exibir a mensagem de despedida
            limpar_tela()
            # Mensagem de despedida formatada
            print("\n" + "=" * 50)
            print("      OBRIGADO POR USAR A CALCULADORA DE IMC!")
            print("=" * 50)
            print("\nMantenha hábitos saudáveis e consulte sempre um profissional!")
            print("Até logo! 👋\n")
            
            # Altera a variável de controle para False
            # Isso fará o loop while terminar
            rodando = False
            # Pequena pausa (1 segundo) antes de fechar
            # Dá tempo de ler a mensagem de despedida
            time.sleep(1)
        
        # ============================================================
        # OPÇÃO INVÁLIDA
        # ============================================================
        else:
            # Usuário digitou algo diferente de 1, 2 ou 3
            print("\n❌ Opção inválida! Escolha 1, 2 ou 3.")
            # Pausa de 1.5 segundos para ler a mensagem
            time.sleep(1.5)
            # O loop continua (rodando continua True) e o menu é exibido novamente
    
    # Quando sair do loop (rodando = False), encerra o programa
    # sys.exit(0) encerra o programa com código 0 (indica encerramento normal/sem erros)
    sys.exit(0)


# ============================================================================
# PONTO DE ENTRADA DO PROGRAMA
# ============================================================================

# Esta condição verifica se o script está sendo executado diretamente
# (e não importado como módulo por outro programa)
# __name__ é uma variável especial do Python
# Quando o script é executado diretamente, __name__ vale "__main__"
# Quando é importado, __name__ vale o nome do módulo (ex: "app")
if __name__ == "__main__":
    try:
        # Tenta executar a função principal
        main()
    except KeyboardInterrupt:
        # Captura Ctrl+C a qualquer momento durante a execução
        # Isso garante que o programa seja encerrado de forma graciosa
        # mesmo que o usuário interrompa fora do menu principal
        print("\n\n\nPrograma interrompido pelo usuário. Até logo! 👋")
        # Encerra o programa
        sys.exit(0)
