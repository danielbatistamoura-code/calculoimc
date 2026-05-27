# app.py - Calculadora de IMC que roda no terminal
# Não depende de nenhum arquivo externo ou servidor web

# Importa o módulo sys para funções de sistema (como fechar o programa)
import sys

# Importa o módulo os para funções do sistema operacional (limpar tela)
import os

# Importa o módulo time para pausas e animações
import time

# Função para limpar a tela do terminal (funciona em diferentes sistemas)
def limpar_tela():
    """
    Limpa a tela do terminal
    os.name: 'nt' para Windows, 'posix' para Linux/Mac
    """
    if os.name == 'nt':  # Sistema Windows
        os.system('cls')  # Comando cls do Windows
    else:  # Linux, Mac, etc.
        os.system('clear')  # Comando clear do Unix

# Função para exibir o cabeçalho da calculadora
def exibir_cabecalho():
    """
    Exibe um cabeçalho estilizado com o título da calculadora
    Usa caracteres especiais para fazer uma borda
    """
    print("=" * 50)  # Imprime 50 caracteres de igual
    print("     CALCULADORA DE ÍNDICE DE MASSA CORPORAL (IMC)")  # Título centralizado
    print("=" * 50)
    print()  # Linha em branco para espaçamento

# Função para mostrar o menu principal e opções
def exibir_menu():
    """
    Exibe as opções disponíveis ao usuário
    Retorna a opção escolhida
    """
    print("\n" + "-" * 40)  # Linha de separação
    print("MENU PRINCIPAL:")
    print("1. Calcular IMC")
    print("2. Ver tabela de referência")
    print("3. Sair")
    print("-" * 40)
    
    # Solicita e retorna a escolha do usuário
    opcao = input("Escolha uma opção (1-3): ")
    return opcao

# Função para exibir a tabela de referência do IMC
def exibir_tabela_referencia():
    """
    Mostra a tabela completa da OMS com faixas de IMC
    """
    limpar_tela()  # Limpa a tela antes de exibir
    exibir_cabecalho()  # Mostra o cabeçalho
    
    print("\nTABELA DE REFERÊNCIA DO IMC (Organização Mundial da Saúde):\n")
    print("-" * 45)
    print("|   Classificação    |    IMC     |   Risco    |")
    print("-" * 45)
    print("| Abaixo do peso     | < 18.5     |   Elevado  |")
    print("| Peso normal        | 18.5 - 24.9|   Baixo    |")
    print("| Sobrepeso          | 25.0 - 29.9|  Aumentado |")
    print("| Obesidade grau I   | 30.0 - 34.9|   Moderado |")
    print("| Obesidade grau II  | 35.0 - 39.9|   Severo   |")
    print("| Obesidade grau III | ≥ 40       |  Muito severo|")
    print("-" * 45)
    
    print("\n📊 O IMC é calculado dividindo o peso (kg) pela altura (m) ao quadrado")
    print("Fórmula: IMC = peso ÷ (altura × altura)")
    
    input("\nPressione ENTER para voltar ao menu...")  # Aguarda usuário pressionar Enter

# Função para validar se a entrada é um número positivo
def validar_numero(valor, tipo):
    """
    Valida se o valor é um número positivo válido
    tipo: "peso" ou "altura" para mensagens específicas
    """
    try:
        # Tenta converter a string para float (número decimal)
        num = float(valor)
        
        # Verifica se o número é positivo e dentro de limites realistas
        if tipo == "peso":
            if num <= 0:
                print("❌ Erro: O peso deve ser maior que zero!")
                return None
            elif num < 10:
                print("⚠️ Atenção: Peso muito baixo. Verifique se digitou corretamente!")
                return None
            elif num > 500:
                print("⚠️ Atenção: Peso muito alto. Verifique se digitou corretamente!")
                return None
        elif tipo == "altura":
            if num <= 0:
                print("❌ Erro: A altura deve ser maior que zero!")
                return None
            elif num < 0.5:
                print("⚠️ Atenção: Altura muito baixa. Verifique se digitou (ex: 1.75 para 1,75m)!")
                return None
            elif num > 2.8:
                print("⚠️ Atenção: Altura muito alta. Verifique se digitou corretamente!")
                return None
        
        return num  # Retorna o número válido
    except ValueError:
        # Se não conseguiu converter para número
        print(f"❌ Erro: '{valor}' não é um número válido!")
        return None

# Função para obter e validar o peso do usuário
def obter_peso():
    """
    Solicita o peso ao usuário e retorna o valor válido
    """
    while True:  # Loop infinito até receber um valor válido
        try:
            # input() sempre retorna string, converte para float
            peso_input = input("Digite seu peso em quilogramas (kg): ")
            peso = validar_numero(peso_input, "peso")
            
            if peso is not None:  # Se a validação passou
                return peso  # Retorna o peso válido
            # Se não passou, o loop continua
        except KeyboardInterrupt:
            # Captura Ctrl+C para sair graciosamente
            print("\n\nOperação cancelada pelo usuário.")
            sys.exit(0)

# Função para obter e validar a altura do usuário
def obter_altura():
    """
    Solicita a altura ao usuário e retorna o valor válido
    """
    while True:  # Loop infinito até receber um valor válido
        try:
            altura_input = input("Digite sua altura em metros (ex: 1.75): ")
            altura = validar_numero(altura_input, "altura")
            
            if altura is not None:  # Se a validação passou
                return altura  # Retorna a altura válida
            # Se não passou, o loop continua
        except KeyboardInterrupt:
            # Captura Ctrl+C para sair graciosamente
            print("\n\nOperação cancelada pelo usuário.")
            sys.exit(0)

# Função que calcula o IMC baseado no peso e altura
def calcular_imc(peso, altura):
    """
    Calcula o IMC usando a fórmula: peso / (altura * altura)
    Retorna o IMC arredondado para 2 casas decimais
    """
    imc = peso / (altura * altura)  # Fórmula do IMC
    return round(imc, 2)  # Arredonda para 2 casas decimais

# Função que determina a classificação baseada no valor do IMC
def classificar_imc(imc):
    """
    Classifica o IMC de acordo com a tabela da OMS
    Retorna a classificação e uma mensagem personalizada
    """
    if imc < 16:
        classificacao = "Magreza grau III"
        mensagem = "⚠️  Situação crítica! Procure um médico urgentemente!"
        cor = "\033[91m"  # Vermelho (código ANSI para cor no terminal)
    elif imc < 17:
        classificacao = "Magreza grau II"
        mensagem = "⚠️  Baixo peso severo. Consulte um nutricionista!"
        cor = "\033[91m"  # Vermelho
    elif imc < 18.5:
        classificacao = "Magreza grau I"
        mensagem = "⚠️  Você está abaixo do peso ideal. Busque orientação profissional!"
        cor = "\033[93m"  # Amarelo
    elif imc < 25:
        classificacao = "Peso normal"
        mensagem = "✅ Parabéns! Você está com o peso ideal. Mantenha hábitos saudáveis!"
        cor = "\033[92m"  # Verde
    elif imc < 30:
        classificacao = "Sobrepeso"
        mensagem = "⚠️  Atenção! Você está com sobrepeso. Considere melhorar hábitos alimentares!"
        cor = "\033[93m"  # Amarelo
    elif imc < 35:
        classificacao = "Obesidade grau I"
        mensagem = "⚠️  Obesidade moderada. Procure um médico e nutricionista!"
        cor = "\033[91m"  # Vermelho
    elif imc < 40:
        classificacao = "Obesidade grau II"
        mensagem = "⚠️  Obesidade severa. É fundamental buscar ajuda médica!"
        cor = "\033[91m"  # Vermelho
    else:
        classificacao = "Obesidade grau III"
        mensagem = "🚨 URGENTE! Obesidade mórbida. Procure atendimento médico imediatamente!"
        cor = "\033[91m"  # Vermelho
    
    return classificacao, mensagem, cor

# Função para exibir o resultado do cálculo com detalhes
def exibir_resultado(peso, altura, imc, classificacao, mensagem, cor):
    """
    Exibe todos os resultados formatados de forma amigável
    """
    print("\n" + "=" * 50)
    print("           RESULTADO DO CÁLCULO")
    print("=" * 50)
    
    # Mostra os dados de entrada
    print(f"\n📊 DADOS INFORMADOS:")
    print(f"   • Peso: {peso} kg")
    print(f"   • Altura: {altura} m")
    
    # Mostra o cálculo do IMC
    print(f"\n🔢 CÁLCULO DO IMC:")
    print(f"   • Fórmula: {peso} ÷ ({altura} × {altura})")
    print(f"   • {peso} ÷ {altura * altura:.2f}")
    print(f"   • Resultado: {imc}")
    
    # Mostra a classificação com cor
    print(f"\n📋 CLASSIFICAÇÃO:")
    # O \033[ é código ANSI para cor no terminal, \033[0m reseta a cor
    print(f"   {cor}• {classificacao} - IMC: {imc}\033[0m")
    
    # Mostra a mensagem personalizada
    print(f"\n💬 {mensagem}")
    
    # Mostra tabela de referência resumida
    print("\n" + "-" * 50)
    print("📌 TABELA DE REFERÊNCIA RÁPIDA:")
    print("   • Abaixo do peso: < 18.5")
    print("   • Peso normal: 18.5 - 24.9")
    print("   • Sobrepeso: 25.0 - 29.9")
    print("   • Obesidade: ≥ 30.0")
    print("-" * 50)

# Função para salvar o resultado em um arquivo de histórico
def salvar_historico(peso, altura, imc, classificacao):
    """
    Salva o cálculo no arquivo historico_imc.txt para consulta futura
    """
    try:
        # Abre o arquivo em modo append (adicionar ao final)
        # Se o arquivo não existir, será criado
        with open("historico_imc.txt", "a", encoding="utf-8") as arquivo:
            # Importa datetime para registrar data e hora
            from datetime import datetime
            agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Formata data/hora
            
            # Escreve uma linha com todos os dados
            arquivo.write(f"[{agora}] Peso: {peso}kg | Altura: {altura}m | ")
            arquivo.write(f"IMC: {imc} | Classificação: {classificacao}\n")
        
        print("\n💾 Resultado salvo no histórico (historico_imc.txt)")
        return True
    except Exception as e:
        # Se houver erro ao salvar, mostra mas não interrompe o programa
        print(f"\n⚠️ Não foi possível salvar o histórico: {e}")
        return False

# Função para mostrar estatísticas do histórico
def mostrar_estatisticas():
    """
    Lê o arquivo de histórico e mostra estatísticas dos cálculos anteriores
    """
    try:
        # Tenta abrir o arquivo de histórico
        with open("historico_imc.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        
        if not linhas:
            print("\n📭 Nenhum histórico encontrado. Faça alguns cálculos primeiro!")
            return
        
        print("\n" + "=" * 50)
        print("        HISTÓRICO DE CÁLCULOS")
        print("=" * 50)
        
        # Mostra os últimos 10 registros
        print("\n📜 ÚLTIMOS 10 REGISTROS:\n")
        for linha in linhas[-10:]:  # Pega as últimas 10 linhas
            print(f"   {linha.strip()}")
        
        print(f"\n📊 Total de registros: {len(linhas)}")
        
    except FileNotFoundError:
        print("\n📭 Nenhum histórico encontrado. Faça alguns cálculos primeiro!")

# Função para animação de carregamento (efeito visual)
def animar_calculando():
    """
    Mostra uma animação simples enquanto "calcula"
    Só para efeito visual
    """
    print("\nCalculando", end="")  # end="" evita pular linha
    for _ in range(3):  # Repete 3 vezes
        time.sleep(0.3)  # Pausa de 0.3 segundos
        print(".", end="")  # Imprime ponto na mesma linha
        time.sleep(0.3)
    print(" Pronto!\n")  # Pula linha após animação

# Função principal que organiza o fluxo do programa
def main():
    """
    Função principal que controla o programa
    """
    # Variável para controlar se o programa deve continuar rodando
    rodando = True
    
    while rodando:  # Loop principal do programa
        limpar_tela()  # Limpa a tela antes de cada iteração
        exibir_cabecalho()  # Mostra o cabeçalho
        
        opcao = exibir_menu()  # Mostra menu e obtém opção
        
        if opcao == "1":
            # Opção de calcular IMC
            limpar_tela()
            exibir_cabecalho()
            
            print("\nVamos calcular seu IMC!")
            print("Digite os dados solicitados abaixo:\n")
            
            # Obtém peso e altura validados
            peso = obter_peso()
            altura = obter_altura()
            
            # Animação de calculando
            animar_calculando()
            
            # Calcula o IMC
            imc = calcular_imc(peso, altura)
            
            # Classifica o IMC
            classificacao, mensagem, cor = classificar_imc(imc)
            
            # Exibe o resultado formatado
            exibir_resultado(peso, altura, imc, classificacao, mensagem, cor)
            
            # Pergunta se quer salvar no histórico
            salvar = input("\n💾 Deseja salvar este resultado no histórico? (s/n): ").lower()
            if salvar == 's' or salvar == 'sim':
                salvar_historico(peso, altura, imc, classificacao)
            
            # Pergunta se quer ver o histórico
            ver_historico = input("\n📜 Deseja ver o histórico de cálculos? (s/n): ").lower()
            if ver_historico == 's' or ver_historico == 'sim':
                mostrar_estatisticas()
            
            input("\nPressione ENTER para continuar...")  # Aguarda ENTER
            
        elif opcao == "2":
            # Opção de ver tabela de referência
            exibir_tabela_referencia()
            
        elif opcao == "3":
            # Opção de sair
            limpar_tela()
            print("\n" + "=" * 50)
            print("      OBRIGADO POR USAR A CALCULADORA DE IMC!")
            print("=" * 50)
            print("\nMantenha hábitos saudáveis e consulte sempre um profissional!")
            print("Até logo! 👋\n")
            rodando = False  # Sai do loop
            time.sleep(1)  # Pequena pausa antes de fechar
            
        else:
            # Opção inválida
            print("\n❌ Opção inválida! Escolha 1, 2 ou 3.")
            time.sleep(1.5)  # Pausa para ler a mensagem
    
    # Fecha o programa
    sys.exit(0)

# Ponto de entrada do programa
# Esta condição verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    try:
        main()  # Executa a função principal
    except KeyboardInterrupt:
        # Captura Ctrl+C a qualquer momento
        print("\n\n\nPrograma interrompido pelo usuário. Até logo! 👋")
        sys.exit(0)