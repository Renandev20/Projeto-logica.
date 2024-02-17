import pygame
import random
import tkinter as tk
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

# Substitua 'YOUR_OPENAI_API_KEY' pela sua chave real da API OpenAI

audio = sr.Recognizer()
maquina = pyttsx3.init()

def saudacao():
    hora_atual = datetime.datetime.now().hour

    if 5 <= hora_atual < 12:
        return "Bom dia!,nossos da empresa GP e fazemos programas em Python."
    elif 12 <= hora_atual < 18:
        return "Boa tarde!, nossos da empresa GP e fazemos programas em Python."
    else:
        return "Boa noite!, nossos da empresa GP e fazemos programas em Python."

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'pedro' in comando:
                comando = comando.replace('pedro', '')
                maquina.say(comando)
                maquina.runAndWait()
    except:
        print('Microfone não está ok')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são ' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()

def Tela():
    class Calculadora:
        import tkinter as tk

        class Tela():
            def __init__(self):
                self.tela = tk.Tk()
                self.tela.title("Calculadora")
                self.tela.resizable(width=False, height=False)
                self.Res = ""
                self.Valores = 0
                self.WIDTH = 10
                self.HEIGHT = 3
                self.Fonte = "Arial 14 bold"

                def atualizar(auxBt):
                    self.Res += auxBt
                    self.auxResultado.set(self.Res)

                def calcular():
                    Digitos = []
                    oper = []
                    num = []
                    print(self.Res)
                    for i in self.Res:
                        if i.isdigit():
                            Digitos.append(i)
                        else:
                            oper.append(i)
                            Digitos.append("*")
                    NumStr = "".join(Digitos)
                    NumStr = NumStr.split("*")
                    for j in NumStr:
                        num.append(j)

                    # operações
                    if oper[0] == "+":
                        ResTotal = int(num[0]) + int(num[1])
                    if oper[0] == "-":
                        ResTotal = int(num[0]) - int(num[1])
                    if oper[0] == "x":
                        ResTotal = int(num[0]) * int(num[1])
                    if oper[0] == "/":
                        ResTotal = round(int(num[0]) / int(num[1]), 1)

                    self.auxResultado.set(str(ResTotal))

                    print(Digitos)
                    print(NumStr)
                    print(oper)
                    self.Res = []

                def limpar():
                    self.Res = ""
                    self.auxResultado.set("---")

                self.auxResultado = tk.StringVar()
                self.auxResultado.set("---")
                self.lbResultado = tk.Label(self.tela, textvariable=self.auxResultado, font="Verdana 12 bold",
                                            borderwidth=5)
                self.lbResultado.grid(row=0, columnspan=3)

                # (C) botão para limpar
                self.btLimpar = tk.Button(self.tela, text="C", width=self.WIDTH, height=self.HEIGHT, font=self.Fonte,
                                          bg="red", command=lambda: limpar())
                self.btLimpar.grid(row=1, column=3, padx=2, pady=2)

                # Botão 0
                self.auxBt0 = tk.StringVar()
                self.auxBt0.set(0)
                self.bt01 = tk.Button(self.tela, textvariable=self.auxBt0, width=self.WIDTH, height=self.HEIGHT,
                                      font=self.Fonte, command=lambda: atualizar(self.auxBt0.get()))
                self.bt01.grid(row=1, column=0, padx=2, pady=2)

                # Botão 1
                self.auxBt1 = tk.StringVar()
                self.auxBt1.set(1)
                self.bt1 = tk.Button(self.tela, textvariable=self.auxBt1, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt1.get()))
                self.bt1.grid(row=1, column=1, padx=2, pady=2)

                # Botão 2
                self.auxBt2 = tk.StringVar()
                self.auxBt2.set(2)
                self.bt2 = tk.Button(self.tela, textvariable=self.auxBt2, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt2.get()))
                self.bt2.grid(row=1, column=2, padx=2, pady=2)

                # Botão 3
                self.auxBt3 = tk.StringVar()
                self.auxBt3.set(3)
                self.bt4 = tk.Button(self.tela, textvariable=self.auxBt3, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt3.get()))
                self.bt4.grid(row=2, column=0, padx=2, pady=2)

                # Botão 4
                self.auxBt4 = tk.StringVar()
                self.auxBt4.set(4)
                self.bt4 = tk.Button(self.tela, textvariable=self.auxBt4, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt4.get()))
                self.bt4.grid(row=2, column=1, padx=2, pady=2)

                # Botão 5
                self.auxBt5 = tk.StringVar()
                self.auxBt5.set(5)
                self.bt5 = tk.Button(self.tela, textvariable=self.auxBt5, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt5.get()))
                self.bt5.grid(row=2, column=2, padx=2, pady=2)

                # Botão 6
                self.auxBt6 = tk.StringVar()
                self.auxBt6.set(6)
                self.bt6 = tk.Button(self.tela, textvariable=self.auxBt6, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt6.get()))
                self.bt6.grid(row=3, column=0, padx=2, pady=2)

                # Botão 7
                self.auxBt7 = tk.StringVar()
                self.auxBt7.set(7)
                self.bt7 = tk.Button(self.tela, textvariable=self.auxBt7, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt7.get()))
                self.bt7.grid(row=3, column=1, padx=2, pady=2)

                # Botão 8
                self.auxBt8 = tk.StringVar()
                self.auxBt8.set(8)
                self.bt8 = tk.Button(self.tela, textvariable=self.auxBt8, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt8.get()))
                self.bt8.grid(row=3, column=2, padx=2, pady=2)

                # Botão 9
                self.auxBt9 = tk.StringVar()
                self.auxBt9.set(9)
                self.bt9 = tk.Button(self.tela, textvariable=self.auxBt9, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt9.get()))
                self.bt9.grid(row=4, column=0, padx=2, pady=2)

                # operador -
                self.auxBtMenos = tk.StringVar()
                self.auxBtMenos.set("-")
                self.btMenos = tk.Button(self.tela, textvariable=self.auxBtMenos, width=self.WIDTH, height=self.HEIGHT,
                                         font=self.Fonte, bg="light blue",
                                         command=lambda: atualizar(self.auxBtMenos.get()))
                self.btMenos.grid(row=4, column=1, padx=2, pady=2)

                # operador +
                self.auxBtMais = tk.StringVar()
                self.auxBtMais.set("+")
                self.btMais = tk.Button(self.tela, textvariable=self.auxBtMais, width=self.WIDTH, height=self.HEIGHT,
                                        font=self.Fonte, bg="light blue",
                                        command=lambda: atualizar(self.auxBtMais.get()))
                self.btMais.grid(row=4, column=2, padx=2, pady=2)

                # operador /
                self.auxBtDiv = tk.StringVar()
                self.auxBtDiv.set("/")
                self.btDiv = tk.Button(self.tela, textvariable=self.auxBtDiv, width=self.WIDTH, height=self.HEIGHT,
                                       font=self.Fonte, bg="light blue", command=lambda: atualizar(self.auxBtDiv.get()))
                self.btDiv.grid(row=5, column=0, padx=2, pady=2)

                # operador x
                self.auxBtMul = tk.StringVar()
                self.auxBtMul.set("x")
                self.btMul = tk.Button(self.tela, textvariable=self.auxBtMul, width=self.WIDTH, height=self.HEIGHT,
                                       font=self.Fonte, bg="light blue", command=lambda: atualizar(self.auxBtMul.get()))
                self.btMul.grid(row=5, column=1, padx=2, pady=2)

                # igual
                self.auxBtIgual = tk.StringVar()
                self.auxBtIgual.set("=")
                self.btIgual = tk.Button(self.tela, textvariable=self.auxBtIgual, width=self.WIDTH, height=self.HEIGHT,
                                         font=self.Fonte, bg="gray", command=lambda: calcular())
                self.btIgual.grid(row=5, column=2, padx=2, pady=2)

                self.tela.mainloop()

        Tela()

    Tela()

def jogo_cobrinha():
    # configurações iniciais
    import pygame
    import random

    pygame.init()

    pygame.display.set_caption("Jogo Snake Python")

    largura, altura = 1200, 800

    tela = pygame.display.set_mode((largura, altura))

    relogio = pygame.time.Clock()

    # cores RGB
    preta = (0, 0, 0)
    branca = (255, 255, 255)
    vermelha = (255, 0, 0)
    verde = (0, 255, 0)

    # parâmetros da cobrinha
    tamanho_quadrado = 20
    velocidade_jogo = 15

    def gerar_comida():
        comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(
            tamanho_quadrado)
        comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(
            tamanho_quadrado)
        return comida_x, comida_y

    def desenhar_comida(tamanho, comida_x, comida_y):
        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

    def desenhar_cobra(tamanho, pixels):
        for pixel in pixels:
            pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

    def desenhar_pontuacao(pontuacao):
        fonte = pygame.font.SysFont("Helvetica", 35)
        texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
        tela.blit(texto, [1, 1])

    def selecionar_velocidade(tecla):
        velocidade_x, velocidade_y = 0, 0
        if tecla == pygame.K_DOWN:
            velocidade_y = tamanho_quadrado
        elif tecla == pygame.K_UP:
            velocidade_y = -tamanho_quadrado
        elif tecla == pygame.K_RIGHT:
            velocidade_x = tamanho_quadrado
        elif tecla == pygame.K_LEFT:
            velocidade_x = -tamanho_quadrado
        return velocidade_x, velocidade_y

    def rodar_jogo():
        fim_jogo = False
        x, y = largura / 2, altura / 2
        velocidade_x, velocidade_y = 0, 0
        tamanho_cobra = 1
        pixels = []
        comida_x, comida_y = gerar_comida()

        while not fim_jogo:
            tela.fill(preta)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                elif evento.type == pygame.KEYDOWN:
                    velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

            # desenhar_comida
            desenhar_comida(tamanho_quadrado, comida_x, comida_y)

            # atualizar a posição da cobra
            if x < 0 or x >= largura or y < 0 or y >= altura:
                fim_jogo = True

            x += velocidade_x
            y += velocidade_y

            # desenhar_cobra
            pixels.append([x, y])
            if len(pixels) > tamanho_cobra:
                del pixels[0]

            # se a cobra bateu no próprio corpo
            for pixel in pixels[:-1]:
                if pixel == [x, y]:
                    fim_jogo = True

            desenhar_cobra(tamanho_quadrado, pixels)

            # desenhar_pontos
            desenhar_pontuacao(tamanho_cobra - 1)

            # atualização da tela
            pygame.display.update()

            # criar uma nova comida
            if x == comida_x and y == comida_y:
                tamanho_cobra += 1
                comida_x, comida_y = gerar_comida()

            relogio.tick(velocidade_jogo)




def simulador_brasileirao():
    import random

    class Jogador:
        def __init__(self, numero, posicao, nome, clube, valor, categoria):
            self.numero = numero
            self.posicao = posicao
            self.nome = nome
            self.clube = clube
            self.valor = valor
            self.categoria = categoria

        def exibir_informacoes(self):
            print(
                f"{self.numero}. {self.posicao}: {self.nome} ({self.clube}) - € {self.valor} milhões ({self.categoria})")

    class Time:
        def __init__(self, nome, orcamento):
            self.nome = nome
            self.orcamento = orcamento
            self.jogadores = []
            self.chance_campeao = 0
            self.pontos = 0

        def exibir_informacoes(self):
            print(
                f"{self.nome.ljust(20)}\t€ {self.orcamento} milhões\tChance de Campeão: {self.chance_campeao}%\tPontos: {self.pontos}")

    class Campeonato:
        def __init__(self, times):
            self.times = times
            self.partidas = self.gerar_partidas()

        def exibir_times(self):
            print("Times no Brasileirão:")
            for i, time in enumerate(self.times, 1):
                print(f"{i}. {time.nome}")

        def escolher_time(self, escolha):
            return self.times[escolha - 1] if 1 <= escolha <= len(self.times) else None

        def contratar_jogador(self, time, jogador):
            if jogador.valor <= time.orcamento:
                if time.orcamento - jogador.valor >= 0:
                    time.jogadores.append(jogador)
                    time.orcamento -= jogador.valor
                    print(f"{time.nome} contratou {jogador.nome} por € {jogador.valor} milhões. ({jogador.categoria})")
                    if jogador.categoria == "Craque":
                        time.chance_campeao += 10
                    elif jogador.categoria == "Bom":
                        time.chance_campeao += 5
                    else:
                        time.chance_campeao += 3
                else:
                    print(f"{time.nome} não pode contratar {jogador.nome}. Orçamento estourado.")
            else:
                print(f"{time.nome} não tem orçamento suficiente para contratar {jogador.nome}.")

        def gerar_partidas(self):
            partidas = []
            for i in range(len(self.times)):
                for j in range(i + 1, len(self.times)):
                    partidas.append((self.times[i], self.times[j]))
                    partidas.append((self.times[j], self.times[i]))
            return partidas

        def simular_partidas(self):
            for rodada, partida in enumerate(self.partidas, 1):
                time1, time2 = partida
                resultado = random.choice(["Vitória", "Empate", "Derrota"])
                if resultado == "Vitória":
                    time1.pontos += 3
                elif resultado == "Empate":
                    time1.pontos += 1
                    time2.pontos += 1
                else:
                    time2.pontos += 3

                print(f"Rodada {rodada}: {time1.nome} {resultado} contra {time2.nome}")

        def classificar_times(self):
            times_ordenados = sorted(self.times, key=lambda x: x.pontos, reverse=True)
            classificacao = []

            for i, time in enumerate(times_ordenados, 1):
                classificacao.append(f"{i}. {time.nome}: {time.pontos} pontos")

                if i <= 4:
                    classificacao.append(f"{time.nome} se classificou para a Libertadores!")
                elif 5 <= i <= 8:
                    classificacao.append(f"{time.nome} se classificou para a Sul-Americana.")
                elif i == len(self.times):
                    classificacao.append(f"{time.nome} foi rebaixado para a Série B.")

            return "\n".join(classificacao)

        def exibir_tabela(self):
            print("\nTabela Final do Campeonato:")
            print("Posição\tTime\t\t\t\tPontos")
            times_ordenados = sorted(self.times, key=lambda x: x.pontos, reverse=True)
            for i, time in enumerate(times_ordenados, 1):
                print(f"{i}\t\t{time.exibir_informacoes()}")

            # Adiciona a classificação ao final das partidas
            print(self.classificar_times())

    def criar_jogadores():
        jogadores = [
            Jogador(1, "Goleiro", "Alisson", "Liverpool", 1.5, "Craque"),
            Jogador(2, "Lateral-direito", "João Cancelo", "Manchester City", 1.2, "Craque"),
            Jogador(3, "Zagueiro", "Virgil van Dijk", "Liverpool", 2.0, "Craque"),
            Jogador(4, "Meia", "Kevin De Bruyne", "Manchester City", 2.5, "Craque"),
            Jogador(5, "Goleiro", "Hugo Lloris", "Tottenham", 1.3, "Bom"),
            Jogador(6, "Lateral-esquerdo", "Alex Grimaldo", "Benfica", 1.0, "Bom"),
            Jogador(7, "Volante", "Declan Rice", "West Ham", 0.8, "Bom"),
            Jogador(8, "Atacante", "Kylian Mbappé", "Paris Saint-Germain", 3.0, "Craque"),
            Jogador(9, "Goleiro", "Kepa Arrizabalaga", "Chelsea", 1.7, "Bom"),
            Jogador(10, "Lateral-direito", "Diogo Dalot", "Manchester United", 0.9, "Bom"),
            Jogador(11, "Zagueiro", "Raphaël Varane", "Manchester United", 2.2, "Craque"),
            Jogador(12, "Atacante", "Ousmane Dembélé", "Barcelona", 1.6, "Bom"),
        ]
        return jogadores

    def criar_times_brasileirao():
        times_brasileirao = [
            Time("Palmeiras", 24.11),
            Time("Atlético Mineiro", 9),
            Time("Botafogo", 8.2),
            Time("Athletico Paranaense", 7),
            Time("Fluminense", 6.4),
            Time("Cuiabá", 5.3),
            Time("Red Bull Bragantino", 4.8),
            Time("Corinthians", 100.9),
            Time("São Paulo", 3.8),
            Time("Ceará", 3.6),
            Time("Fortaleza", 2.9),
            Time("América Mineiro", 2.8),
            Time("Santos", 2.5),
            Time("Internacional", 2.1),
            Time("Juventude", 1.6),
            Time("Avaí", 1.5),
            Time("Goiás", 1.3),
            Time("Grêmio", 0.6),
            Time("Cruzeiro", 0.2),
            Time("Flamengo", -1.8),
            Time("Vasco da Gama", -6.79),
        ]
        return times_brasileirao

    def main():
        jogadores = criar_jogadores()
        times_brasileirao = criar_times_brasileirao()
        campeonato_brasileirao = Campeonato(times_brasileirao)

        campeonato_brasileirao.exibir_times()
        escolha_time_usuario = int(input("Escolha um time do Brasileirão (digite o número): "))
        time_selecionado = campeonato_brasileirao.escolher_time(escolha_time_usuario)

        if time_selecionado:
            print(f"\nVocê escolheu o time {time_selecionado.nome}.")
            print(f"Orçamento do time: € {time_selecionado.orcamento} milhões")

            while True:
                if time_selecionado.orcamento <= 0:
                    print(
                        f"Orçamento do time {time_selecionado.nome} estourado. Não é possível contratar mais jogadores.")
                    break

                print("\nJogadores disponíveis:")
                jogadores_disponiveis = [jogador for jogador in jogadores if jogador not in time_selecionado.jogadores]
                for jogador in jogadores_disponiveis:
                    jogador.exibir_informacoes()

                escolha_jogador_usuario = int(
                    input("\nEscolha um jogador para contratar (digite o número, 0 para sair): "))

                if escolha_jogador_usuario == 0:
                    break

                if 1 <= escolha_jogador_usuario <= len(jogadores_disponiveis):
                    jogador_selecionado = jogadores_disponiveis[escolha_jogador_usuario - 1]
                    campeonato_brasileirao.contratar_jogador(time_selecionado, jogador_selecionado)
                else:
                    print("Escolha de jogador inválida. Por favor, escolha um jogador válido.")

            # Simular 32 partidas

            # Exibir tabela após as partidas
            campeonato_brasileirao.exibir_tabela()

            # Exibir posição do time escolhido e se ele ganhou o campeonato
            posicao_time_escolhido = times_brasileirao.index(time_selecionado) + 1
            print(f"\nPosição do {time_selecionado.nome} no Campeonato: {posicao_time_escolhido}")
            if posicao_time_escolhido == 1:
                print(f"{time_selecionado.nome} é o campeão do Campeonato Brasileiro!")
            elif posicao_time_escolhido == 1 or posicao_time_escolhido == 2 or posicao_time_escolhido == 3 or posicao_time_escolhido == 4 or posicao_time_escolhido == 5 or posicao_time_escolhido == 6:
                print(
                    f"o {time_selecionado.nome} esteve na {posicao_time_escolhido} posição e foi classificado na libertadores  ")
            elif posicao_time_escolhido == 7 or posicao_time_escolhido == 8 or posicao_time_escolhido == 9 or posicao_time_escolhido == 10 or posicao_time_escolhido == 11 or posicao_time_escolhido == 12:
                print(
                    f"{time_selecionado.nome} esteve na {posicao_time_escolhido} posição e foi classificado para a sula-americana")
            elif posicao_time_escolhido == 21 or posicao_time_escolhido == 20 or posicao_time_escolhido == 19 or posicao_time_escolhido == 18:
                print(
                    f"infelizmente seu time esteve na {posicao_time_escolhido} e foi rebaixado ele vai jogar a serei b proximo ano")
            else:

                print(f"{time_selecionado.nome} não foi o campeão do Campeonato Brasileiro.")

        else:
            print("Escolha de time inválida. Por favor, escolha um time válido.")

    if __name__ == "__main__":
        main()


import pygame
import random
import tkinter as tk
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

# Substitua 'YOUR_OPENAI_API_KEY' pela sua chave real da API OpenAI

audio = sr.Recognizer()
maquina = pyttsx3.init()

def saudacao():
    hora_atual = datetime.datetime.now().hour

    if 5 <= hora_atual < 12:
        return "Bom dia!,nossos da empresa GP e fazemos programas em Python."
    elif 12 <= hora_atual < 18:
        return "Boa tarde!, nossos da empresa GP e fazemos programas em Python."
    else:
        return "Boa noite!, nossos da empresa GP e fazemos programas em Python."

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'pedro' in comando:
                comando = comando.replace('pedro', '')
                maquina.say(comando)
                maquina.runAndWait()
    except:
        print('Microfone não está ok')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são ' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()

def Tela():
    class Calculadora:
        import tkinter as tk

        class Tela():
            def __init__(self):
                self.tela = tk.Tk()
                self.tela.title("Calculadora")
                self.tela.resizable(width=False, height=False)
                self.Res = ""
                self.Valores = 0
                self.WIDTH = 10
                self.HEIGHT = 3
                self.Fonte = "Arial 14 bold"

                def atualizar(auxBt):
                    self.Res += auxBt
                    self.auxResultado.set(self.Res)

                def calcular():
                    Digitos = []
                    oper = []
                    num = []
                    print(self.Res)
                    for i in self.Res:
                        if i.isdigit():
                            Digitos.append(i)
                        else:
                            oper.append(i)
                            Digitos.append("*")
                    NumStr = "".join(Digitos)
                    NumStr = NumStr.split("*")
                    for j in NumStr:
                        num.append(j)

                    # operações
                    if oper[0] == "+":
                        ResTotal = int(num[0]) + int(num[1])
                    if oper[0] == "-":
                        ResTotal = int(num[0]) - int(num[1])
                    if oper[0] == "x":
                        ResTotal = int(num[0]) * int(num[1])
                    if oper[0] == "/":
                        ResTotal = round(int(num[0]) / int(num[1]), 1)

                    self.auxResultado.set(str(ResTotal))

                    print(Digitos)
                    print(NumStr)
                    print(oper)
                    self.Res = []

                def limpar():
                    self.Res = ""
                    self.auxResultado.set("---")

                self.auxResultado = tk.StringVar()
                self.auxResultado.set("---")
                self.lbResultado = tk.Label(self.tela, textvariable=self.auxResultado, font="Verdana 12 bold",
                                            borderwidth=5)
                self.lbResultado.grid(row=0, columnspan=3)

                # (C) botão para limpar
                self.btLimpar = tk.Button(self.tela, text="C", width=self.WIDTH, height=self.HEIGHT, font=self.Fonte,
                                          bg="red", command=lambda: limpar())
                self.btLimpar.grid(row=1, column=3, padx=2, pady=2)

                # Botão 0
                self.auxBt0 = tk.StringVar()
                self.auxBt0.set(0)
                self.bt01 = tk.Button(self.tela, textvariable=self.auxBt0, width=self.WIDTH, height=self.HEIGHT,
                                      font=self.Fonte, command=lambda: atualizar(self.auxBt0.get()))
                self.bt01.grid(row=1, column=0, padx=2, pady=2)

                # Botão 1
                self.auxBt1 = tk.StringVar()
                self.auxBt1.set(1)
                self.bt1 = tk.Button(self.tela, textvariable=self.auxBt1, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt1.get()))
                self.bt1.grid(row=1, column=1, padx=2, pady=2)

                # Botão 2
                self.auxBt2 = tk.StringVar()
                self.auxBt2.set(2)
                self.bt2 = tk.Button(self.tela, textvariable=self.auxBt2, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt2.get()))
                self.bt2.grid(row=1, column=2, padx=2, pady=2)

                # Botão 3
                self.auxBt3 = tk.StringVar()
                self.auxBt3.set(3)
                self.bt4 = tk.Button(self.tela, textvariable=self.auxBt3, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt3.get()))
                self.bt4.grid(row=2, column=0, padx=2, pady=2)

                # Botão 4
                self.auxBt4 = tk.StringVar()
                self.auxBt4.set(4)
                self.bt4 = tk.Button(self.tela, textvariable=self.auxBt4, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt4.get()))
                self.bt4.grid(row=2, column=1, padx=2, pady=2)

                # Botão 5
                self.auxBt5 = tk.StringVar()
                self.auxBt5.set(5)
                self.bt5 = tk.Button(self.tela, textvariable=self.auxBt5, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt5.get()))
                self.bt5.grid(row=2, column=2, padx=2, pady=2)

                # Botão 6
                self.auxBt6 = tk.StringVar()
                self.auxBt6.set(6)
                self.bt6 = tk.Button(self.tela, textvariable=self.auxBt6, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt6.get()))
                self.bt6.grid(row=3, column=0, padx=2, pady=2)

                # Botão 7
                self.auxBt7 = tk.StringVar()
                self.auxBt7.set(7)
                self.bt7 = tk.Button(self.tela, textvariable=self.auxBt7, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt7.get()))
                self.bt7.grid(row=3, column=1, padx=2, pady=2)

                # Botão 8
                self.auxBt8 = tk.StringVar()
                self.auxBt8.set(8)
                self.bt8 = tk.Button(self.tela, textvariable=self.auxBt8, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt8.get()))
                self.bt8.grid(row=3, column=2, padx=2, pady=2)

                # Botão 9
                self.auxBt9 = tk.StringVar()
                self.auxBt9.set(9)
                self.bt9 = tk.Button(self.tela, textvariable=self.auxBt9, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt9.get()))
                self.bt9.grid(row=4, column=0, padx=2, pady=2)

                # operador -
                self.auxBtMenos = tk.StringVar()
                self.auxBtMenos.set("-")
                self.btMenos = tk.Button(self.tela, textvariable=self.auxBtMenos, width=self.WIDTH, height=self.HEIGHT,
                                         font=self.Fonte, bg="light blue",
                                         command=lambda: atualizar(self.auxBtMenos.get()))
                self.btMenos.grid(row=4, column=1, padx=2, pady=2)

                # operador +
                self.auxBtMais = tk.StringVar()
                self.auxBtMais.set("+")
                self.btMais = tk.Button(self.tela, textvariable=self.auxBtMais, width=self.WIDTH, height=self.HEIGHT,
                                        font=self.Fonte, bg="light blue",
                                        command=lambda: atualizar(self.auxBtMais.get()))
                self.btMais.grid(row=4, column=2, padx=2, pady=2)

                # operador /
                self.auxBtDiv = tk.StringVar()
                self.auxBtDiv.set("/")
                self.btDiv = tk.Button(self.tela, textvariable=self.auxBtDiv, width=self.WIDTH, height=self.HEIGHT,
                                       font=self.Fonte, bg="light blue", command=lambda: atualizar(self.auxBtDiv.get()))
                self.btDiv.grid(row=5, column=0, padx=2, pady=2)

                # operador x
                self.auxBtMul = tk.StringVar()
                self.auxBtMul.set("x")
                self.btMul = tk.Button(self.tela, textvariable=self.auxBtMul, width=self.WIDTH, height=self.HEIGHT,
                                       font=self.Fonte, bg="light blue", command=lambda: atualizar(self.auxBtMul.get()))
                self.btMul.grid(row=5, column=1, padx=2, pady=2)

                # igual
                self.auxBtIgual = tk.StringVar()
                self.auxBtIgual.set("=")
                self.btIgual = tk.Button(self.tela, textvariable=self.auxBtIgual, width=self.WIDTH, height=self.HEIGHT,
                                         font=self.Fonte, bg="gray", command=lambda: calcular())
                self.btIgual.grid(row=5, column=2, padx=2, pady=2)

                self.tela.mainloop()

        Tela()

    Tela()

def jogo_cobrinha():
    # configurações iniciais
    import pygame
    import random

    pygame.init()

    pygame.display.set_caption("Jogo Snake Python")

    largura, altura = 1200, 800

    tela = pygame.display.set_mode((largura, altura))

    relogio = pygame.time.Clock()

    # cores RGB
    preta = (0, 0, 0)
    branca = (255, 255, 255)
    vermelha = (255, 0, 0)
    verde = (0, 255, 0)

    # parâmetros da cobrinha
    tamanho_quadrado = 20
    velocidade_jogo = 15

    def gerar_comida():
        comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(
            tamanho_quadrado)
        comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(
            tamanho_quadrado)
        return comida_x, comida_y

    def desenhar_comida(tamanho, comida_x, comida_y):
        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

    def desenhar_cobra(tamanho, pixels):
        for pixel in pixels:
            pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

    def desenhar_pontuacao(pontuacao):
        fonte = pygame.font.SysFont("Helvetica", 35)
        texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
        tela.blit(texto, [1, 1])

    def selecionar_velocidade(tecla):
        velocidade_x, velocidade_y = 0, 0
        if tecla == pygame.K_DOWN:
            velocidade_y = tamanho_quadrado
        elif tecla == pygame.K_UP:
            velocidade_y = -tamanho_quadrado
        elif tecla == pygame.K_RIGHT:
            velocidade_x = tamanho_quadrado
        elif tecla == pygame.K_LEFT:
            velocidade_x = -tamanho_quadrado
        return velocidade_x, velocidade_y

    def rodar_jogo():
        fim_jogo = False
        x, y = largura / 2, altura / 2
        velocidade_x, velocidade_y = 0, 0
        tamanho_cobra = 1
        pixels = []
        comida_x, comida_y = gerar_comida()

        while not fim_jogo:
            tela.fill(preta)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                elif evento.type == pygame.KEYDOWN:
                    velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

            # desenhar_comida
            desenhar_comida(tamanho_quadrado, comida_x, comida_y)

            # atualizar a posição da cobra
            if x < 0 or x >= largura or y < 0 or y >= altura:
                fim_jogo = True

            x += velocidade_x
            y += velocidade_y

            # desenhar_cobra
            pixels.append([x, y])
            if len(pixels) > tamanho_cobra:
                del pixels[0]

            # se a cobra bateu no próprio corpo
            for pixel in pixels[:-1]:
                if pixel == [x, y]:
                    fim_jogo = True

            desenhar_cobra(tamanho_quadrado, pixels)

            # desenhar_pontos
            desenhar_pontuacao(tamanho_cobra - 1)

            # atualização da tela
            pygame.display.update()

            # criar uma nova comida
            if x == comida_x and y == comida_y:
                tamanho_cobra += 1
                comida_x, comida_y = gerar_comida()

            relogio.tick(velocidade_jogo)

    rodar_jogo()


def simulador_brasileirao():
    import random

    class Jogador:
        def __init__(self, numero, posicao, nome, clube, valor, categoria):
            self.numero = numero
            self.posicao = posicao
            self.nome = nome
            self.clube = clube
            self.valor = valor
            self.categoria = categoria

        def exibir_informacoes(self):
            print(
                f"{self.numero}. {self.posicao}: {self.nome} ({self.clube}) - € {self.valor} milhões ({self.categoria})")

    class Time:
        def __init__(self, nome, orcamento):
            self.nome = nome
            self.orcamento = orcamento
            self.jogadores = []
            self.chance_campeao = 0
            self.pontos = 0

        def exibir_informacoes(self):
            print(
                f"{self.nome.ljust(20)}\t€ {self.orcamento} milhões\tChance de Campeão: {self.chance_campeao}%\tPontos: {self.pontos}")

    class Campeonato:
        def __init__(self, times):
            self.times = times
            self.partidas = self.gerar_partidas()

        def exibir_times(self):
            print("Times no Brasileirão:")
            for i, time in enumerate(self.times, 1):
                print(f"{i}. {time.nome}")

        def escolher_time(self, escolha):
            return self.times[escolha - 1] if 1 <= escolha <= len(self.times) else None

        def contratar_jogador(self, time, jogador):
            if jogador.valor <= time.orcamento:
                if time.orcamento - jogador.valor >= 0:
                    time.jogadores.append(jogador)
                    time.orcamento -= jogador.valor
                    print(f"{time.nome} contratou {jogador.nome} por € {jogador.valor} milhões. ({jogador.categoria})")
                    if jogador.categoria == "Craque":
                        time.chance_campeao += 10
                    elif jogador.categoria == "Bom":
                        time.chance_campeao += 5
                    else:
                        time.chance_campeao += 3
                else:
                    print(f"{time.nome} não pode contratar {jogador.nome}. Orçamento estourado.")
            else:
                print(f"{time.nome} não tem orçamento suficiente para contratar {jogador.nome}.")

        def gerar_partidas(self):
            partidas = []
            for i in range(len(self.times)):
                for j in range(i + 1, len(self.times)):
                    partidas.append((self.times[i], self.times[j]))
                    partidas.append((self.times[j], self.times[i]))
            return partidas

        def simular_partidas(self):
            for rodada, partida in enumerate(self.partidas, 1):
                time1, time2 = partida
                resultado = random.choice(["Vitória", "Empate", "Derrota"])
                if resultado == "Vitória":
                    time1.pontos += 3
                elif resultado == "Empate":
                    time1.pontos += 1
                    time2.pontos += 1
                else:
                    time2.pontos += 3

                print(f"Rodada {rodada}: {time1.nome} {resultado} contra {time2.nome}")

        def classificar_times(self):
            times_ordenados = sorted(self.times, key=lambda x: x.pontos, reverse=True)
            classificacao = []

            for i, time in enumerate(times_ordenados, 1):
                classificacao.append(f"{i}. {time.nome}: {time.pontos} pontos")

                if i <= 4:
                    classificacao.append(f"{time.nome} se classificou para a Libertadores!")
                elif 5 <= i <= 8:
                    classificacao.append(f"{time.nome} se classificou para a Sul-Americana.")
                elif i == len(self.times):
                    classificacao.append(f"{time.nome} foi rebaixado para a Série B.")

            return "\n".join(classificacao)

        def exibir_tabela(self):
            print("\nTabela Final do Campeonato:")
            print("Posição\tTime\t\t\t\tPontos")
            times_ordenados = sorted(self.times, key=lambda x: x.pontos, reverse=True)
            for i, time in enumerate(times_ordenados, 1):
                print(f"{i}\t\t{time.exibir_informacoes()}")

            # Adiciona a classificação ao final das partidas
            print(self.classificar_times())

    def criar_jogadores():
        jogadores = [
            Jogador(1, "Goleiro", "Alisson", "Liverpool", 1.5, "Craque"),
            Jogador(2, "Lateral-direito", "João Cancelo", "Manchester City", 1.2, "Craque"),
            Jogador(3, "Zagueiro", "Virgil van Dijk", "Liverpool", 2.0, "Craque"),
            Jogador(4, "Meia", "Kevin De Bruyne", "Manchester City", 2.5, "Craque"),
            Jogador(5, "Goleiro", "Hugo Lloris", "Tottenham", 1.3, "Bom"),
            Jogador(6, "Lateral-esquerdo", "Alex Grimaldo", "Benfica", 1.0, "Bom"),
            Jogador(7, "Volante", "Declan Rice", "West Ham", 0.8, "Bom"),
            Jogador(8, "Atacante", "Kylian Mbappé", "Paris Saint-Germain", 3.0, "Craque"),
            Jogador(9, "Goleiro", "Kepa Arrizabalaga", "Chelsea", 1.7, "Bom"),
            Jogador(10, "Lateral-direito", "Diogo Dalot", "Manchester United", 0.9, "Bom"),
            Jogador(11, "Zagueiro", "Raphaël Varane", "Manchester United", 2.2, "Craque"),
            Jogador(12, "Atacante", "Ousmane Dembélé", "Barcelona", 1.6, "Bom"),
        ]
        return jogadores

    def criar_times_brasileirao():
        times_brasileirao = [
            Time("Palmeiras", 24.11),
            Time("Atlético Mineiro", 9),
            Time("Botafogo", 8.2),
            Time("Athletico Paranaense", 7),
            Time("Fluminense", 6.4),
            Time("Cuiabá", 5.3),
            Time("Red Bull Bragantino", 4.8),
            Time("Corinthians", 100.9),
            Time("São Paulo", 3.8),
            Time("Ceará", 3.6),
            Time("Fortaleza", 2.9),
            Time("América Mineiro", 2.8),
            Time("Santos", 2.5),
            Time("Internacional", 2.1),
            Time("Juventude", 1.6),
            Time("Avaí", 1.5),
            Time("Goiás", 1.3),
            Time("Grêmio", 0.6),
            Time("Cruzeiro", 0.2),
            Time("Flamengo", -1.8),
            Time("Vasco da Gama", -6.79),
        ]
        return times_brasileirao

    def main():
        jogadores = criar_jogadores()
        times_brasileirao = criar_times_brasileirao()
        campeonato_brasileirao = Campeonato(times_brasileirao)

        campeonato_brasileirao.exibir_times()
        escolha_time_usuario = int(input("Escolha um time do Brasileirão (digite o número): "))
        time_selecionado = campeonato_brasileirao.escolher_time(escolha_time_usuario)

        if time_selecionado:
            print(f"\nVocê escolheu o time {time_selecionado.nome}.")
            print(f"Orçamento do time: € {time_selecionado.orcamento} milhões")

            while True:
                if time_selecionado.orcamento <= 0:
                    print(
                        f"Orçamento do time {time_selecionado.nome} estourado. Não é possível contratar mais jogadores.")
                    break

                print("\nJogadores disponíveis:")
                jogadores_disponiveis = [jogador for jogador in jogadores if jogador not in time_selecionado.jogadores]
                for jogador in jogadores_disponiveis:
                    jogador.exibir_informacoes()

                escolha_jogador_usuario = int(
                    input("\nEscolha um jogador para contratar (digite o número, 0 para sair): "))

                if escolha_jogador_usuario == 0:
                    break

                if 1 <= escolha_jogador_usuario <= len(jogadores_disponiveis):
                    jogador_selecionado = jogadores_disponiveis[escolha_jogador_usuario - 1]
                    campeonato_brasileirao.contratar_jogador(time_selecionado, jogador_selecionado)
                else:
                    print("Escolha de jogador inválida. Por favor, escolha um jogador válido.")

            # Simular 32 partidas

            # Exibir tabela após as partidas
            campeonato_brasileirao.exibir_tabela()

            # Exibir posição do time escolhido e se ele ganhou o campeonato
            posicao_time_escolhido = times_brasileirao.index(time_selecionado) + 1
            print(f"\nPosição do {time_selecionado.nome} no Campeonato: {posicao_time_escolhido}")
            if posicao_time_escolhido == 1:
                print(f"{time_selecionado.nome} é o campeão do Campeonato Brasileiro!")
            elif posicao_time_escolhido == 1 or posicao_time_escolhido == 2 or posicao_time_escolhido == 3 or posicao_time_escolhido == 4 or posicao_time_escolhido == 5 or posicao_time_escolhido == 6:
                print(
                    f"o {time_selecionado.nome} esteve na {posicao_time_escolhido} posição e foi classificado na libertadores  ")
            elif posicao_time_escolhido == 7 or posicao_time_escolhido == 8 or posicao_time_escolhido == 9 or posicao_time_escolhido == 10 or posicao_time_escolhido == 11 or posicao_time_escolhido == 12:
                print(
                    f"{time_selecionado.nome} esteve na {posicao_time_escolhido} posição e foi classificado para a sula-americana")
            elif posicao_time_escolhido == 21 or posicao_time_escolhido == 20 or posicao_time_escolhido == 19 or posicao_time_escolhido == 18:
                print(
                    f"infelizmente seu time esteve na {posicao_time_escolhido} e foi rebaixado ele vai jogar a serei b proximo ano")
            else:

                print(f"{time_selecionado.nome} não foi o campeão do Campeonato Brasileiro.")

        else:
            print("Escolha de time inválida. Por favor, escolha um time válido.")

    if __name__ == "__main__":
        main()


mensagem_saudacao = saudacao()
print(mensagem_saudacao)

menu = int(input("Este é nosso menu:: \n pressione [1] para uma calculadora. \n pressione [2] para jogo da cobrinha. \n pressione [3] para conversa com a nossa IA Pedro. \n pressione [4] para um simulador do Brasileirão."))
match menu:

  case 1:
       Tela()
  case 2:
        jogo_cobrinha()
  case 3:
       comando_voz_usuario()
  case  4:
         simulador_brasileirao()
  case _:
    print("Opção inválida. Por favor, escolha uma opção válida.")
