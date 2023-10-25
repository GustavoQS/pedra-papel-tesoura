from tkinter import *
import random

rodada = 1  # rodada atual
vitorias = 0    # vitórias do player
bot_vitorias = 0    # vitórias do bot
opcoes = ['pedra', 'papel', 'tesoura']
titulo = ("Arial", 18, "bold")
cores = ['white', 'red', 'green']


# verifica quem venceu a rodada
def verificar():
    global rodada, vitorias, bot_vitorias, gui_rodada, gui_status, vc, bot

    # se o bot e player escolheram a mesma opção
    if e_vc == e_bot:
        rodada += 1
        gui_rodada = Label(text=f"Rodada {rodada}", bg=cores[0], font=titulo).grid(row=0, column=0, sticky=S)   # indicador rodada (interface)
        gui_status = Label(text=f"Empate!", bg=cores[0], width=15, height=1, font=titulo).grid(row=2, column=1, pady=50)    # indicador quem venceu (interface)
    # se o bot ganhou a rodada
    elif e_bot == 'pedra' and e_vc == 'tesoura' or e_bot == 'papel' and e_vc == 'pedra' or e_bot == 'tesoura' and e_vc == 'papel':
        bot_vitorias += 1
        rodada += 1
        gui_rodada = Label(text=f"Rodada {rodada}", bg=cores[0], font=titulo).grid(row=0, column=0, sticky=S)   # indicador rodada (interface)
        gui_status = Label(text=f"Você perdeu!", bg=cores[0], fg=cores[1], width=15, height=1, font=titulo).grid(row=2, column=1)   # indicador quem venceu (interface)
        bot = Label(text=f"Bot {bot_vitorias} pts", bg=cores[0], font=titulo).grid(row=3, column=0)     # altera os pontos do bot
    # se o usuário ganhou a rodada
    elif e_bot == 'papel' and e_vc == 'tesoura' or e_bot == 'tesoura' and e_vc == 'pedra' or e_bot == 'pedra' and e_vc == 'papel':
        vitorias += 1
        rodada += 1
        gui_rodada = Label(text=f"Rodada {rodada}", background=cores[0], font=titulo).grid(row=0, column=0, sticky=S)   # indicador rodada (interface)
        gui_status = Label(text=f"Você ganhou!", bg=cores[0], fg=cores[2], width=15, height=1, font=titulo).grid(row=2, column=1)   # indicador quem venceu (interface)
        vc = Label(text=f"Você {vitorias} pts", bg=cores[0], font=titulo).grid(row=3, column=2)     # altera os pontos do player


# atribui escolha "pedra" para o jogador
def pedra():
    global e_vc, e_bot, gui_bot

    e_bot = random.choice(opcoes)   # define uma escolha "para o bot" de forma aleatória
    gui_bot = Label(image=imgs[e_bot], bg=cores[0]).grid(row=1, column=1)   # altera a imagem do bot

    e_vc = 'pedra'
    verificar()
    return e_vc, e_bot


# atribui escolha "papel" para o jogador
def papel():
    global e_vc, e_bot, gui_bot

    e_bot = random.choice(opcoes)    # define uma escolha "para o bot" de forma aleatória
    gui_bot = Label(image=imgs[e_bot], bg=cores[0]).grid(row=1, column=1)   # altera a imagem do bot

    e_vc = 'papel'
    verificar()
    return e_vc, e_bot


# atribui escolha "tesoura" para o jogador
def tesoura():
    global e_vc, e_bot, gui_bot

    e_bot = random.choice(opcoes)    # define uma escolha "para o bot" de forma aleatória
    gui_bot = Label(image=imgs[e_bot], bg=cores[0]).grid(row=1, column=1)   # altera a imagem do bot

    e_vc = 'tesoura'
    verificar()
    return e_vc, e_bot


# inicia a interface
if __name__ == '__main__':

    window = Tk()
    window.title("Jogo pedra papel tesoura")
    window.configure(bg=cores[0])

    window.overrideredirect(True)

    # tamanho da janela
    w = 825
    h = 850

    # posição da janela na tela do usuário
    x = 500
    y = 100

    # define tamanho e local da janela na tela do usuário
    window.geometry(f"{w}x{h}+{x}+{y}")
    window.resizable(False, False)

    # window.config(padx=10, pady=100)
    window.columnconfigure([0, 1, 2], minsize=200)
    window.rowconfigure(0, minsize=50)
    window.rowconfigure([1, 2, 3], minsize=140)

    # gui_img = Label(image=python_image)
    # gui_img.grid(row=0, column=2)

    # imagens
    global imgs
    imgs = {
        'bot': PhotoImage(file='./imagens/bot.png'),
        'pedra': PhotoImage(file='./imagens/bot_pedra.png'),
        'papel': PhotoImage(file='./imagens/bot_papel.png'),
        'tesoura': PhotoImage(file='./imagens/bot_tesoura.png'),
        'icone' : PhotoImage(file='./imagens/icone.png'),
        'sair' : PhotoImage(file='./imagens/sair.png')
    }

    # rodada atual
    global gui_rodada
    gui_rodada = Label(text=f"Rodada {rodada}", bg=cores[0], font=titulo).grid(row=0, column=0, sticky=S)

    # botao sair
    sair = Button(window, image=imgs['sair'], borderwidth = 0, bg=cores[0], command=window.destroy)
    sair.grid(row=0, column=2, sticky=E)
    window.iconphoto(False, imgs['icone'])

    # imagem do bot
    gui_bot = Label(image=imgs['bot'], bg=cores[0]).grid(row=1, column=1)

    # status da partida (indica se usuário ganhou, perdeu ou empatou)
    gui_status = Label(text="Vamos jogar!", bg=cores[0], font=titulo).grid(row=2, column=1)

    # texto "vs"
    gui_pontos = Label(text=f"vs", bg=cores[0], font=titulo).grid(row=3, column=1)
    # pontos do jogador
    vc = Label(text=f"Você {vitorias} pts", bg=cores[0], font=titulo).grid(row=3, column=2)
    # pontos do bot
    bot = Label(text=f"Bot {bot_vitorias} pts", bg=cores[0], font=titulo).grid(row=3, column=0)

    # imagem pedra
    img_pedra = PhotoImage(file='./imagens/pedra.png')
    pedra = Button(image=img_pedra, borderwidth = 0, bg=cores[0], command=pedra).grid(row=4, column=0)  # botao pedra

    # imagem papel
    img_papel = PhotoImage(file='./imagens/papel.png')
    papel = Button(image=img_papel, borderwidth = 0, bg=cores[0], command=papel).grid(row=4, column=1) # botao papel

    # imagem tesoura
    img_tesoura = PhotoImage(file='./imagens/tesoura.png')
    tesoura = Button(image=img_tesoura, borderwidth = 0, bg=cores[0], command=tesoura).grid(row=4, column=2) # botao tesoura

    window.mainloop()
