import tkinter as tk
import time
from datetime import datetime
import tkinter.messagebox as tkm

class Janela_Principal():
    
    def __init__(self):        
        
        self.window = tk.Tk()
        self.window.geometry("300x450+100+100")
        self.window.title("Tamagotchi")
        self.window.configure(background = 'white')
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.sair)
        
        # Geometria da página
        self.window.rowconfigure(0, minsize = 450)
        self.window.columnconfigure(0, minsize = 300)
        
        # Menu Principal
        self.menu_principal = Menu_Principal(self)
        
        # Escolha dos personagens
        self.esc_personagens = Escolha_Personagem(self)
        
        # Jogo
        self.jogo = Tamagotchi(self)
        
        # Loja
        self.loja = Loja(self)
        
        # Começar mostrando o menu
        self.menu_principal.mostrar()
        
    def sair(self):
        self.jogo.sair()
        self.window.quit()
        
    def mostra_menu_principal(self):
        self.menu_principal.mostrar()
        
    def mostra_tamagotchi(self):
        self.jogo.mostrar()
        
    def mostra_escolher_personagem(self):
        self.esc_personagens.mostrar()
        
    def mostra_loja(self):
        self.loja.mostrar()
        
    def iniciar(self):
        self.window.mainloop()
        
        
class Menu_Principal():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window1 = tk.Frame(self.janela_principal.window)
        self.window1.grid(row = 0, column = 0, sticky = "nsew")

#        Tentativa de colocar uma música no jogo        
#        theme = r"C:\Users\Usuario\Documents\Insper\D.S\Tamagotchi\GitHub\ProjetoFinal-DesSoft\Música\Fire Red Main Theme Extended.mp3"
#        sound = mp3play.load(theme)
#        sound.play() 
        
        # Geometria da página        
        self.window1.rowconfigure(0, minsize = 100)
        self.window1.rowconfigure(1, minsize = 110)
        self.window1.rowconfigure(2, minsize = 120)
        self.window1.rowconfigure(3, minsize = 120)
        
        self.window1.columnconfigure(0, minsize = 300)
        
        self.pokebola = tk.PhotoImage(file = "Pokeball.png")
        self.pokebola_label = tk.Label(self.window1, image = self.pokebola, height = 1, width = 1)
        self.pokebola_label.grid(row = 0, column = 0, sticky = "nsew")
        
        self.titulo_label = tk.Label(self.window1, text = "Seja um Treinador", font = "Bauhaus 24")
        self.titulo_label.grid(row = 1, column = 0)

        self.button_continuar = tk.Button(self.window1, text = "Continuar", height = 5, width = 30)        
        self.button_continuar.grid(row = 2, column = 0)
        self.button_continuar.configure(command = self.continuar)
        
        self.button_novojogo = tk.Button(self.window1, text = "Novo Jogo", height = 5, width = 30)        
        self.button_novojogo.grid(row = 3, column = 0)
        self.button_novojogo.configure(command = self.novo_jogo)
        
    def continuar(self):      
        if self.janela_principal.jogo.p =="x":
            tk.messagebox.showinfo ('Escolha','Você ainda nao escolheu seu pokemon')   
        else:
            self.janela_principal.mostra_tamagotchi()
            self.janela_principal.jogo.comeca_tamagotchi()
    
    def novo_jogo(self):
        self.janela_principal.mostra_escolher_personagem()          
        
    def mostrar(self):
        self.window1.tkraise()
        
        
class Escolha_Personagem():
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window_escolha = tk.Frame(self.janela_principal.window)
        self.window_escolha.grid(row = 0, column = 0, sticky = "nsew")
        
        self.window_escolha.rowconfigure(0, minsize = 90)
        self.window_escolha.rowconfigure(1, minsize = 120)
        self.window_escolha.rowconfigure(2, minsize = 120)
        self.window_escolha.rowconfigure(3, minsize = 120)
        
        self.window_escolha.columnconfigure(0, minsize = 300)
        
        self.titulo_label = tk.Label(self.window_escolha, text = "Escolha seu Pokemon", font = "Bauhaus 20")
        self.titulo_label.grid(row = 0, column = 0, sticky = "nsew")
        
        self.char_imagem = tk.PhotoImage(file = "Charmander.png")
        self.charmander = tk.Button(self.window_escolha, image = self.char_imagem, height = 100, width = 100)
        self.charmander.grid(row = 1, column = 0)
        self.charmander.configure(command = self.escolhe_char)
        
        self.squir_imagem = tk.PhotoImage(file = "Squirtle.png")
        self.squirtle = tk.Button(self.window_escolha, image = self.squir_imagem, height = 100, width = 100)
        self.squirtle.grid(row = 2, column = 0)
        self.squirtle.configure(command = self.escolhe_squir)
        
        self.bulb_imagem = tk.PhotoImage(file = "Bulbasaur.png")
        self.bulbasaur = tk.Button(self.window_escolha, image = self.bulb_imagem, height = 100, width = 100)
        self.bulbasaur.grid(row = 3, column = 0)
        self.bulbasaur.configure(command = self.escolhe_bulb)
        
        
    def escolhe_char(self):
        self.janela_principal.jogo.reset("charmander")
        self.janela_principal.mostra_tamagotchi()
        self.janela_principal.jogo.comeca_tamagotchi()
   
    def escolhe_squir(self):
        self.janela_principal.jogo.reset("squirtle")
        self.janela_principal.mostra_tamagotchi()
        self.janela_principal.jogo.comeca_tamagotchi()
   
    def escolhe_bulb(self):
        self.janela_principal.jogo.reset("bulbasaur")
        self.janela_principal.mostra_tamagotchi()
        self.janela_principal.jogo.comeca_tamagotchi()
    
    def mostrar(self):
        self.window_escolha.tkraise()
        
        
class Loja:
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window_loja = tk.Frame(self.janela_principal.window)
        self.window_loja.grid(row = 0, column = 0, sticky = "nsew")
        
        self.window_loja.rowconfigure(0, minsize = 90)
        self.window_loja.rowconfigure(1, minsize = 100)
        self.window_loja.rowconfigure(2, minsize = 20)
        self.window_loja.rowconfigure(3, minsize = 100)
        self.window_loja.rowconfigure(4, minsize = 20)
        self.window_loja.rowconfigure(5, minsize = 100)
        self.window_loja.rowconfigure(6, minsize = 20)
        
        self.window_loja.columnconfigure(0, minsize = 100)
        self.window_loja.columnconfigure(1, minsize = 100)
        self.window_loja.columnconfigure(2, minsize = 100)
        
        # Imagens       
        self.bigode = tk.PhotoImage(file = "Bigode.png")
        self.oculos = tk.PhotoImage(file = "Oculos.png")
        self.chapeu = tk.PhotoImage(file = "Chapeu.png")
        self.carne = tk.PhotoImage(file = "Carne.png")
        self.cafe = tk.PhotoImage(file = "Cafe.png")
        self.sabao = tk.PhotoImage(file = "Sabao.png")
        self.rare_candy = tk.PhotoImage(file = "Rare_Candy.png")
        self.super_rod = tk.PhotoImage(file = "Super_Rod.png")
        self.insper_img = tk.PhotoImage(file = "Insper.png")
        
        # Buttons        
        self.botao1 = tk.Button(self.window_loja, text = "Voltar", height = 2, width = 6)
        self.botao1.grid(row = 0, column = 0)
        self.botao1.configure(command = self.voltar)
        
        self.label2 = tk.Label(self.window_loja, text = "Loja")
        self.label2.grid(row = 0, column = 1, sticky = "nsew")
        
        self.label_dinheiro = tk.Label(self.window_loja)
        self.label_dinheiro.grid(row = 0, column = 2, sticky = "nsew")
        
        self.botao_bigode = tk.Button(self.window_loja, image = self.bigode)
        self.botao_bigode.grid(row = 1, column = 0, sticky = "nsew")
        self.botao_bigode.config(command = self.compra_bigode)
        
        self.botao_oculos = tk.Button(self.window_loja, image = self.oculos)
        self.botao_oculos.grid(row = 1, column = 1, sticky = "nsew")
        self.botao_oculos.config(command = self.compra_oculos)
        
        self.botao_chapeu = tk.Button(self.window_loja, image = self.chapeu)
        self.botao_chapeu.grid(row = 1, column = 2, sticky = "nsew")
        self.botao_chapeu.config(command = self.compra_chapeu)
        
        self.botao_carne = tk.Button(self.window_loja, image = self.carne)
        self.botao_carne.grid(row = 3, column = 0, sticky = "nsew")
        self.botao_carne.config(command = self.compra_carne)
        
        self.botao_sabao = tk.Button(self.window_loja, image = self.sabao)
        self.botao_sabao.grid(row = 3, column = 1, sticky = "nsew")
        self.botao_sabao.config(command = self.compra_sabao)
        
        self.botao_cafe = tk.Button(self.window_loja, image = self.cafe)
        self.botao_cafe.grid(row = 3, column = 2, sticky = "nsew")
        self.botao_cafe.config(command = self.compra_cafe)
        
        self.botao_rc = tk.Button(self.window_loja, image = self.rare_candy)
        self.botao_rc.grid(row = 5, column = 0, sticky = "nsew")
        self.botao_rc.config(command = self.compra_rc)
        
        self.botao_sr = tk.Button(self.window_loja, image = self.super_rod)
        self.botao_sr.grid(row = 5, column = 1, sticky = "nsew")
        self.botao_sr.config(command = self.compra_sr)
        
        self.botao_poster = tk.Button(self.window_loja, image = self.insper_img)
        self.botao_poster.grid(row = 5, column = 2, sticky = "nsew")
        self.botao_poster.config(command = self.compra_poster)
        
        # Labels        
        self.label_bigode = tk.Label(self.window_loja, text = "Bigode - $500")
        self.label_bigode.grid(row = 2, column = 0, sticky = "nsew")
        
        self.label_oculos = tk.Label(self.window_loja, text = "Óculos - $500")
        self.label_oculos.grid(row = 2, column = 1, sticky = "nsew")
        
        self.label_chapeu = tk.Label(self.window_loja, text = "Chapéu - $500")
        self.label_chapeu.grid(row = 2, column = 2, sticky = "nsew")
        
        self.label_carne = tk.Label(self.window_loja, text = "Alimento - $20")
        self.label_carne.grid(row = 4, column = 0, sticky = "nsew")
        
        self.label_sabao = tk.Label(self.window_loja, text = "Sabão - $20")
        self.label_sabao.grid(row = 4, column = 1, sticky = "nsew")
        
        self.label_cafe = tk.Label(self.window_loja, text = "Café - $20")
        self.label_cafe.grid(row = 4, column = 2, sticky = "nsew")
        
        self.label_rc = tk.Label(self.window_loja, text = "Rare Candy - $775")
        self.label_rc.grid(row = 6, column = 0, sticky = "nsew")
        
        self.label_sr = tk.Label(self.window_loja, text = "Super Rod - $650")
        self.label_sr.grid(row = 6, column = 1, sticky = "nsew")
        
        self.label_poster = tk.Label(self.window_loja, text = "Poster - $200")
        self.label_poster.grid(row = 6, column = 2, sticky = "nsew")
        
        # Iniciar o after
        self.window_loja.after(0, self.update_money)
        
        # Ler o save
        self.arquivo = open("Save", "r")
        self.lista = self.arquivo.readlines()
        self.last_line = self.lista[-1]
        self.arquivo.close()
        
        self.str_split = self.last_line.split(",")
        self.tem_bigode = int(self.str_split[8])
        self.tem_oculos = int(self.str_split[9])
        self.tem_chapeu = int(self.str_split[10])
        self.qtd_carne = int(self.str_split[11])
        self.qtd_sabao = int(self.str_split[12])
        self.qtd_cafe = int(self.str_split[13])
        self.qtd_rc = int(self.str_split[14])
        self.tem_sr = int(self.str_split[15])
        self.tem_poster = int(self.str_split[16])
        
        # Inventário
        self.n_bigode = self.tem_bigode
        self.n_oculos = self.tem_oculos
        self.n_chapeu = self.tem_chapeu
        self.n_carne = self.qtd_carne
        self.n_sabao = self.qtd_sabao
        self.n_cafe = self.qtd_cafe
        self.n_rc = self.qtd_rc
        self.n_sr = self.tem_sr
        self.n_poster = self.tem_poster
        
        if self.tem_bigode == 1:
            self.botao_bigode.configure(state = "disabled")
            
        if self.tem_oculos == 1:
            self.botao_oculos.configure(state = "disabled")
            
        if self.tem_chapeu == 1:
            self.botao_chapeu.configure(state = "disabled")
            
        if self.tem_sr == 1:
            self.botao_sr.configure(state = "disabled")
            
        if self.tem_poster == 1:
            self.botao_poster.configure(state = "disabled")

        
    # Compras
    def compra_bigode(self):
        
        if self.janela_principal.jogo.dinheiro >= 500:
            
            self.janela_principal.jogo.dinheiro -= 500
            self.botao_bigode.configure(state = "disabled")
            self.janela_principal.jogo.button_bigode.configure(state = "active")
            self.n_bigode += 1
            self.update_money()
            print(self.n_bigode)
            
        else:
            
            tkm.showinfo(title = "Dinheiro", message = "Dinheiro Insuficiente!")
            
    
    def compra_oculos(self):
        
        if self.janela_principal.jogo.dinheiro >= 500:
            
            self.janela_principal.jogo.dinheiro -= 500
            self.botao_oculos.configure(state = "disabled")
            self.janela_principal.jogo.button_oculos.configure(state = "active")
            self.n_oculos += 1
            self.update_money()
            print(self.n_oculos)
            
        else:
            
            tkm.showinfo(title = "Dinheiro", message = "Dinheiro Insuficiente!")
            
    
    def compra_chapeu(self):
        
        if self.janela_principal.jogo.dinheiro >= 500:
            
            self.janela_principal.jogo.dinheiro -= 500
            self.botao_chapeu.configure(state = "disabled")
            self.janela_principal.jogo.button_chapeu.configure(state = "active")
            self.n_chapeu += 1
            self.update_money()
            print(self.n_chapeu)
            
        else:
            
            tkm.showinfo(title = "Dinheiro", message = "Dinheiro Insuficiente!")
            
        
    def compra_carne(self):
        
        if self.janela_principal.jogo.dinheiro >= 20:
            
            self.janela_principal.jogo.dinheiro -= 20
            self.n_carne += 1
            self.update_money()
            print(self.n_carne)
            
        else:
            
            tkm.showinfo(title = "Dinheiro", message = "Dinheiro Insuficiente!")


    def compra_sabao(self):
        
        if self.janela_principal.jogo.dinheiro >= 20:
            
            self.janela_principal.jogo.dinheiro -= 20
            self.n_sabao += 1
            self.update_money()
            print(self.n_sabao)
            
        else:
            
            tkm.showinfo(title = "Dinheiro", message = "Dinheiro Insuficiente!")
            
            
    def compra_cafe(self):
        
        if self.janela_principal.jogo.dinheiro >= 20:
            
            self.janela_principal.jogo.dinheiro -= 20
            self.n_cafe += 1
            self.update_money()
            print(self.n_cafe)
            
        else:
            
            tkm.showinfo(title = "Dinheiro", message = "Dinheiro Insuficiente!")
            
            
    def compra_rc(self):
        
        if self.janela_principal.jogo.dinheiro >= 775:
            
            self.janela_principal.jogo.dinheiro -= 775
            self.janela_principal.jogo.button_rc.configure(state = "active")
            self.n_rc += 1
            self.update_money()
            print(self.n_rc)
            
        else:
            
            tkm.showinfo(title = "Dinheiro", message = "Dinheiro Insuficiente!")
            
            
    def compra_sr(self):
        
        if self.janela_principal.jogo.dinheiro >= 650:
            
            self.janela_principal.jogo.dinheiro -= 650
            self.botao_sr.configure(state = "disabled")
            self.janela_principal.jogo.button_sr.configure(state = "active")
            self.n_sr += 1
            self.update_money()
            print(self.n_sr)
            
        else:
            
            tkm.showinfo(title = "Dinheiro", message = "Dinheiro Insuficiente!")
            
            
    def compra_poster(self):
        
        if self.janela_principal.jogo.dinheiro >= 200:
            
            self.janela_principal.jogo.dinheiro -= 200
            self.botao_poster.configure (state = "disabled")
            self.janela_principal.jogo.button_poster.configure(state = "active")
            self.n_poster += 1
            self.update_money()
            
        else:
            
            tkm.showinfo(title = "Dinheiro", message = "Dinheiro Insuficiente!")
    
    # Ganhar dinheiro por dia                
    def update_money(self):
        self.label_dinheiro.configure(text = "Dinheiros:\n {0}"
        .format(self.janela_principal.jogo.dinheiro))
        
    def mostrar(self):
        self.window_loja.tkraise()
        
    def voltar(self):
        self.janela_principal.mostra_tamagotchi()

        
class Tamagotchi:
    
    def __init__(self, janela_principal):
        
        self.janela_principal = janela_principal
        self.window_tamagotchi = tk.Frame(self.janela_principal.window)
        self.window_tamagotchi.grid(row = 0, column = 0, sticky = "nsew")
        self.window_tamagotchi.configure(bg = "white")
        
        self.le_todas_as_imagens()
        
        self.canvas = tk.Canvas(self.window_tamagotchi, width = 192, height = 192)
        self.canvas.configure(bg = "white", highlightthickness = 0)
        self.canvas.grid(row = 2, rowspan = 3, column = 0, columnspan = 3)
#        self.p = "squirtle"
        
        # Pegando últimos status
        self.arquivo = open("Save", "r")
        self.lista = self.arquivo.readlines()
        self.last_line = self.lista[-1]
        self.arquivo.close()
            
        self.str_split = self.last_line.split(",")
        self.last_timetable = self.str_split[0]
        self.last_day = int(self.str_split[1])
        self.last_hunger = int(self.str_split[2])
        self.last_clean = int(self.str_split[3])
        self.last_sleep = int(self.str_split[4])
        self.p = (self.str_split[5])
        self.last_xp = int(self.str_split[6])
        self.last_money = int(self.str_split[7])
        self.last_level = int(self.str_split[17])
        
        self.tem_bigode = int(self.str_split[8])
        self.tem_oculos = int(self.str_split[9])
        self.tem_chapeu = int(self.str_split[10])
        self.qtd_rc = int(self.str_split[14])
        self.tem_sr = int(self.str_split[15])
        self.tem_poster = int(self.str_split[16])
        
        # Atributos do Tamagotchi
        self.hunger = self.last_hunger
        self.clean = self.last_clean
        self.sleep = self.last_sleep
        self.days = self.last_day
        self.xp = self.last_xp
        self.dinheiro = self.last_money
        self.level = self.last_level
        
        # Geometria da página
        self.window_tamagotchi.rowconfigure(0, minsize = 50)
        self.window_tamagotchi.rowconfigure(1, minsize = 50)
        self.window_tamagotchi.rowconfigure(2, minsize = 84)
        self.window_tamagotchi.rowconfigure(3, minsize = 84)
        self.window_tamagotchi.rowconfigure(4, minsize = 82)
        self.window_tamagotchi.rowconfigure(5, minsize = 100)
        
        self.window_tamagotchi.columnconfigure(0, minsize = 100)
        self.window_tamagotchi.columnconfigure(1, minsize = 100)
        self.window_tamagotchi.columnconfigure(2, minsize = 100)
        
        # Labels
        self.label_level = tk.Label(self.window_tamagotchi)
        self.label_level.configure(background = 'white')
        self.label_level.grid(row = 0, column = 0)
        
        self.label_dia = tk.Label(self.window_tamagotchi)
        self.label_dia.configure(background = 'white')
        self.label_dia.grid(row = 0, column = 0, columnspan = 3)
        
        self.label_fome = tk.Label(self.window_tamagotchi)
        self.label_fome.configure(background = 'white')
        self.label_fome.grid(row = 1, column = 0)
        
        self.label_saude = tk.Label(self.window_tamagotchi)
        self.label_saude.configure(background = 'white')
        self.label_saude.grid(row = 1, column = 1)
                
        self.label_sono = tk.Label(self.window_tamagotchi)
        self.label_sono.configure(background = 'white')
        self.label_sono.grid(row = 1, column = 2)
        
        # Botões
        self.icone_comer = tk.PhotoImage(file = "comer_icone.png")
        self.button_feed = tk.Button(self.window_tamagotchi, image = self.icone_comer, height = 1, width = 5)
        self.button_feed.grid(row = 5, column = 0, sticky = "nsew")
        self.button_feed.configure(command = self.update_hunger, background = 'white')
        
        self.icone_limpar = tk.PhotoImage(file = "banho_icone.png")
        self.button_clean = tk.Button(self.window_tamagotchi, image = self.icone_limpar, height = 1, width = 5)
        self.button_clean.grid(row = 5, column = 1, sticky = "nsew")
        self.button_clean.configure(command = self.update_clean, background = 'white')      
        
        self.icone_dormir = tk.PhotoImage(file = "dormir_icone.png")
        self.button_sleep = tk.Button(self.window_tamagotchi, image = self.icone_dormir, height = 1, width = 5)
        self.button_sleep.grid(row = 5, column = 2, sticky = "nsew")
        self.button_sleep.configure(command = self.update_sleep, background = 'white')
        
        self.botao_loja = tk.Button(self.window_tamagotchi, text = "Loja", height = 1, width = 6)
        self.botao_loja.grid(row = 0, column = 2)
        self.botao_loja.configure(command = self.acessa_loja)
        
        self.bigode_img = tk.PhotoImage(file = "bigode_2.png")
        self.button_bigode = tk.Button(self.window_tamagotchi, height = 32, width = 32)
        self.button_bigode.grid(row = 2, column = 0, sticky = "w")
        if self.tem_bigode == 1:
            self.button_bigode.configure(image = self.bigode_img, state = "active")
        else:
            self.button_bigode.configure(image = self.bigode_img, state = "disabled")
                
        self.oculos_img = tk.PhotoImage(file = "oculos_2.png")        
        self.button_oculos = tk.Button(self.window_tamagotchi, height = 32, width = 32)
        self.button_oculos.grid(row = 3, column = 0, sticky = "w")
        if self.tem_oculos == 1:
            self.button_oculos.configure(image = self.oculos_img, state = "active")
        else:
            self.button_oculos.configure(image = self.oculos_img, state = "disabled")
        
        self.chapeu_img = tk.PhotoImage(file = "chapeu_2.png")
        self.button_chapeu = tk.Button(self.window_tamagotchi, height = 32, width = 32)
        self.button_chapeu.grid(row = 4, column = 0, sticky = "w")
        if self.tem_chapeu == 1:
            self.button_chapeu.configure(image = self.chapeu_img, state = "active")
        else:
            self.button_chapeu.configure(image = self.chapeu_img, state = "disabled")
        
        self.rc_img = tk.PhotoImage(file = "Rare_Candy_2.png")
        self.button_rc = tk.Button(self.window_tamagotchi, height = 32, width = 32)
        self.button_rc.grid(row = 2, column = 2, sticky = "e")
        self.button_rc.config(command = self.update_rc)
        if self.qtd_rc >= 1:
            self.button_rc.configure(image = self.rc_img, state = "active")
        else:
            self.button_rc.configure(image = self.rc_img, state = "disabled")
        
        self.sr_img = tk.PhotoImage(file = "Super_Rod_2.png")
        self.button_sr = tk.Button(self.window_tamagotchi, height = 32, width = 32)
        self.button_sr.grid(row = 3, column = 2, sticky = "e")
        if self.tem_sr == 1:
            self.button_sr.configure(image = self.sr_img, state = "active")
        else:
            self.button_sr.configure(image = self.sr_img, state = "disabled")

        self.poster_img = tk.PhotoImage(file = "insper_2.png")
        self.button_poster = tk.Button(self.window_tamagotchi, height = 32, width = 32)
        self.button_poster.grid(row = 4, column = 2, sticky = "e")
        if self.tem_poster == 1:
            self.button_poster.configure(image = self.poster_img, state = "active")
        else:
            self.button_poster.configure(image = self.poster_img, state = "disabled")

    def reset(self,p):
        self.p = p
        self.hunger = 101
        self.clean = 101
        self.sleep = 101
        self.days = 0
        self.xp = 0
        self.dinheiro = 95
        self.level = 0
        
        self.janela_principal.loja.n_bigode = 0
        self.janela_principal.loja.n_oculos = 0
        self.janela_principal.loja.n_chapeu = 0
        self.janela_principal.loja.n_carne = 5
        self.janela_principal.loja.n_sabao = 5
        self.janela_principal.loja.n_cafe = 5
        self.janela_principal.loja.n_rc = 0
        self.janela_principal.loja.n_sr = 0
        self.janela_principal.loja.n_poster = 0
        
        self.janela_principal.loja.botao_bigode.configure(state = "active")
        self.janela_principal.loja.botao_oculos.configure(state = "active")
        self.janela_principal.loja.botao_chapeu.configure(state = "active")

        self.janela_principal.loja.botao_sr.configure(state = "active")
#        self.janela_principal.loja.botao_poster.configure(state = "active")


    def base_arquivo_imagens(self, tipo):
        s = tipo.split("_")
        if s[0] == "squirtle":
            num_imagens = 31
        elif s[0] == "wartortle":
            num_imagens = 33
        elif s[0] == "blastoise":
            num_imagens = 81            
        elif s[0] == "charmander":
            num_imagens = 39
        elif s[0] == "charmeleon":
            num_imagens = 64           
        elif s[0] == "charizard":
            num_imagens = 51           
        elif s[0] == "bulbasaur":
            num_imagens = 43           
        elif s[0] == "ivysaur":
            num_imagens = 51           
        elif s[0] == "venusaur":
            num_imagens = 31 
        # XXXXX etc. terminar
            
        if tipo == "squirtle_A":
            base = 'Squirtle/squirtleA'
        elif tipo == "squirtle_F":
            base = 'Squirtle_F/SquirtleF'
        elif tipo == "squirtle_S":
            base = 'Squirtle_S/SquirtleS'
        elif tipo == "squirtle_B":
            base = 'Squirtle_B/SquirtleB'
#        else:
#            # XXXXX terminar.
#            base = 'Squirtle/squirtleA'
#            num_imagens = 31
            
        elif tipo == "wartortle_A":
            base = 'Squirtle/wartortleA'
        elif tipo == "wartortle_F":
            base = 'Squirtle_F/WartortleF'
        elif tipo == "wartortle_S":
            base = 'Squirtle_S/WartortleS'
        elif tipo == "wartortle_B":
            base = 'Squirtle_B/WartortleB'
    
        elif tipo == "blastoise_A":
            base = 'Squirtle/BlastoiseA'
        elif tipo == "blastoise_F":
            base = 'Squirtle_F/BlastoiseF'
        elif tipo == "blastoise_S":
            base = 'Squirtle_S/BlastoiseS'
        elif tipo == "blastoise_B":
            base = 'Squirtle_B/BlastoiseB'        

        elif tipo == "charmander_A":
            base = 'Charmander/charmanderA'
        elif tipo == "charmander_F":
            base = 'Charmander_F/charmanderF'
        elif tipo == "charmander_S":
            base = 'Charmander_S/charmanderS'
        elif tipo == "charmander_B":
            base = 'Charmander_B/charmanderB'
            
        elif tipo == "charmeleon_A":
            base = 'Charmander/charmeleonA'
        elif tipo == "charmeleon_F":
            base = 'Charmander_F/charmeleonF'
        elif tipo == "charmeleon_S":
            base = 'Charmander_S/charmeleonS'
        elif tipo == "charmeleon_B":
            base = 'Charmander_B/charmeleonB'
    
        elif tipo == "charizard_A":
            base = 'Charmander/charizardA'
        elif tipo == "charizard_F":
            base = 'Charmander_F/charizardF'
        elif tipo == "charizard_S":
            base = 'Charmander_S/charizardS'
        elif tipo == "charizard_B":
            base = 'Charmander_B/charizardB'         

        elif tipo == "bulbasaur_A":
            base = 'Bulbasaur/bulbasaurA'
        elif tipo == "bulbasaur_F":
            base = 'Bulbasaur_F/bulbasaurF'
        elif tipo == "bulbasaur_S":
            base = 'Bulbasaur_S/bulbasaurS'
        elif tipo == "bulbasaur_B":
            base = 'Bulbasaur_B/bulbasaurB'
            
        elif tipo == "ivysaur_A":
            base = 'Bulbasaur/ivysaurA'
        elif tipo == "ivysaur_F":
            base = 'Bulbasaur_F/ivysaurF'
        elif tipo == "ivysaur_S":
            base = 'Bulbasaur_S/ivysaurS'
        elif tipo == "ivysaur_B":
            base = 'Bulbasaur_B/ivysaurB'
    
#        elif tipo == "venusar_A":
#            base = 'Bulbasaur/venusarA'
#        elif tipo == "venusar_F":
#            base = 'Bulbasaur_F/venusaurF'
#        elif tipo == "venusar_S":
#            base = 'Bulbasaur_S/venusaurF'
#        elif tipo == "venusar_B":
#            base = 'Bulbasaur_B/venusaurB' 

        return base, num_imagens        
        
    def le_imagens(self, base, num_imagens):
        lista_imagens = []
        for i in range(1, (num_imagens + 1)):
            lista_imagens.append(tk.PhotoImage(file ='{0}{1}.gif'.format(base, i)))
        lista_imagens = lista_imagens[::-1]
        return lista_imagens
        
    def le_todas_as_imagens(self):
        tipos = [
            "squirtle_A",
            "squirtle_F",
            "squirtle_S",
            "squirtle_B",
            "wartortle_A",
            "wartortle_F",
            "wartortle_S",
            "wartortle_B",
            "blastoise_A",
            "blastoise_F",
            "blastoise_S",
            "blastoise_B",
            "charmander_A",
            "charmander_F",
            "charmander_S",
            "charmander_B",
            "charmeleon_A",
            "charmeleon_F",
            "charmeleon_S",
            "charmeleon_B",
            "charizard_A",
            "charizard_F",
            "charizard_S",
            "charizard_B",
            "bulbasaur_A",
            "bulbasaur_F",
            "bulbasaur_S",
            "bulbasaur_B",
            "ivysaur_A",
            "ivysaur_F",
            "ivysaur_S",
            "ivysaur_B"]
#            "venusar_A",
#            "venusar_F",
#            "venusar_S",
#            "venusar_B"]
        
        self.imagens = {}
        for tipo in tipos:
            base, num_imagens = self.base_arquivo_imagens(tipo)
            self.imagens[tipo] = self.le_imagens(base, num_imagens)
        
    def comeca_tamagotchi(self):        
        self.window_tamagotchi.after(0, self.get_hungry)
        self.window_tamagotchi.after(0, self.get_sleepy)
        self.window_tamagotchi.after(0, self.get_dirty)
        self.window_tamagotchi.after(0, self.pass_day)
        self.window_tamagotchi.after(0, self.animação)
       
# ---------------------------------------------------
# Tempo
        
    def tempo_ao_desligar(self):
        
        # Quando desligar:
#        desligou = time.time()
#        
#        return desligou
        pass
    
    def tempo_ao_ligar(self):
        
        # Quando ligar:
#        ligou = time.time()
#        tkm.showinfo(title = "Em quanto você esteve fora...", message = "...")
#        
#        return ligou
        pass

# ---------------------------------------------------
# Updates:      
    
    def update_hunger(self):
        
        if self.janela_principal.loja.n_carne > 0:    
        
            if self.hunger >= 90:
                
                self.hunger = 101
                
            elif self.hunger >= 100:
                
                return None
                
            else:
                
                self.hunger += 10
                self.xp += 2
            
            self.janela_principal.loja.n_carne -= 1
                
        else:
            
            tkm.showinfo(title = "Alimento", message = "Você não tem comida!")
        
    
    def update_clean(self):
        
        if self.janela_principal.loja.n_sabao > 0:
        
            if self.clean >= 90:
                
                self.clean = 101
                
            elif self.clean >= 100:
                
                return None
                
            else:
                
                self.clean += 10
                self.xp += 2
                
            self.janela_principal.loja.n_sabao -= 1
            
        else:
            
            tkm.showinfo(title = "Limpeza", message = "Você não tem sabão!")
    
    def dormindo(self):
        self.sleep = 100
        self.button_feed.configure(state = "normal")
        self.button_clean.configure(state = "normal")
        self.button_sleep.configure(state = "normal")        
        
        
    def update_sleep(self):
        if self.janela_principal.loja.n_cafe > 0:
        
            if self.sleep > 80:
                return None

            elif self.sleep >= 60:
               self.button_feed.configure(state = "disabled")
               self.button_clean.configure(state = "disabled")
               self.button_sleep.configure(state = "disabled")
               self.xp += 2
               self.window_tamagotchi.after(10000, self.dormindo)

            
            elif self.sleep >= 20:
               self.button_feed.configure(state = "disabled")
               self.button_clean.configure(state = "disabled")
               self.button_sleep.configure(state = "disabled") 
               self.xp += 2
               self.window_tamagotchi.after(50000, self.dormindo)

        
            elif self.sleep >= 1:
               self.button_feed.configure(state = "disabled")
               self.button_clean.configure(state = "disabled")
               self.button_sleep.configure(state = "disabled")
               self.xp += 2
               self.window_tamagotchi.after(100000, self.dormindo)

        
            else :
               self.button_feed.configure(state = "disabled")
               self.button_clean.configure(state = "disabled")
               self.button_sleep.configure(state = "disabled")
               self.xp += 2
               self.window_tamagotchi.after(120000, self.dormindo)

            self.janela_principal.loja.n_cafe -= 1
            
        else:
            
            tkm.showinfo(title = "Café", message = "Você não tem café suficiente!")


    def update_rc(self):
       
        if self.janela_principal.loja.n_rc > 0:
            
            print(self.xp)
            self.xp += 100
            self.janela_principal.loja.n_rc -= 1
            print(self.xp)
            
        else:
            tkm.showinfo(title = "Rare Candy", message = "Você não tem Rare Candy")
                                
    def get_hungry(self):
        
        if self.hunger != 0:
            
            self.hunger -= 1
            
            self.label_fome.configure(text = "Fome:\n{0}".format(self.hunger))
            self.label_level.configure(text = "Level:\n{0}".format(self.xp//50))
                
        else:
            self.label_fome.configure(text = "Fome:\n{0}".format(self.hunger))
            self.morto()
            
        self.window_tamagotchi.after(1000, self.get_hungry)
        
        
    def get_sleepy(self):
        
        if self.sleep != 0:
        
            self.sleep -= 1
                
            self.label_sono.configure(text = "Sono:\n{0}".format(self.sleep))
            self.label_level.configure(text = "Level:\n{0}".format(self.xp//50))
            
        else:
            self.label_sono.configure(text = "Sono:\n{0}".format(self.sleep))
            self.label_level.configure(text = "Level:\n{0}".format(self.xp//50))
            
        self.window_tamagotchi.after(1000, self.get_sleepy)
    
    
    def get_dirty(self):
        
        if self.clean != 0:
        
            self.clean -= 1
            
            self.label_saude.configure(text = "Limpeza:\n{0}".format(self.clean))
            self.label_level.configure(text = "Level:\n{0}".format(self.xp//50))
            
        else:
            self.label_saude.configure(text = "Limpeza:\n{0}".format(self.clean))
            self.label_level.configure(text = "Level:\n{0}".format(self.xp//50))
           
        self.window_tamagotchi.after(1000, self.get_dirty)
    
    
    def pass_day(self):
        
        self.days += 1
        self.xp += 17
        self.dinheiro += 5
            
        self.label_dia.configure(text = "Dia:\n{0}".format(self.days))
        
        self.janela_principal.loja.update_money()
            
        self.window_tamagotchi.after(10000, self.pass_day)

  
# ---------------------------------------------------  
# Consequências:
    
    def morto(self):
        tk.messagebox.showinfo ('Morreu', 'Seu pokemon morreu')
        self.reset("x")
        self.sair()
        self.window_tamagotchi.quit()

#    def sujo(self):
#        return f
    
#    def sonolento(self):
#        return s
        
# --------------------------------------------------
# Iniciar e sair 
        
    def acessa_loja(self):
        self.janela_principal.mostra_loja()
     
    def mostrar(self):       
        self.window_tamagotchi.tkraise()
        
    def sair(self):
        
        horario = datetime.now().time()
        
        save = open('Save', 'w')
        save.write("{0}, {1}, {2}, {3}, {4},{5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}".format
        (horario, self.days, self.hunger, self.clean, self.sleep, self.p, self.xp, self.dinheiro,
                   self.janela_principal.loja.n_bigode, self.janela_principal.loja.n_oculos,
                   self.janela_principal.loja.n_chapeu, self.janela_principal.loja.n_carne,
                   self.janela_principal.loja.n_sabao, self.janela_principal.loja.n_cafe,
                   self.janela_principal.loja.n_rc, self.janela_principal.loja.n_sr,
                   self.janela_principal.loja.n_poster, self.level))
                   
        save.close()
        
        
#------------------------------------------------------  
# Animação
    def evolução(self):
        if self.p == "charmeleon" and self.xp >= 500:
            tkm.showinfo(title = "Evolução", message = "Seu Pokémon evoluiu!")
            self.p = "charizard"
        elif self.p == "charmander" and self.xp >= 300:
            tkm.showinfo(title = "Evolução", message = "Seu Pokémon evoluiu!")
            self.p = "charmeleon"
        elif self.p == "ivysaur" and self.xp >= 500:
            tkm.showinfo(title = "Evolução", message = "Seu Pokémon evoluiu!")
            self.p = "venusaur"
        elif self.p == "bulbasaur" and self.xp >= 300:
            tkm.showinfo(title = "Evolução", message = "Seu Pokémon evoluiu!")
            self.p = "ivysaur"
        elif self.p == "wartortle" and self.xp >= 500:
            tkm.showinfo(title = "Evolução", message = "Seu Pokémon evoluiu!")
            self.p = "blastoise"
        elif self.p == "squirtle" and self.xp >= 300:
            tkm.showinfo(title = "Evolução", message = "Seu Pokémon evoluiu!")
            self.p = "wartortle"
    
        
     
    def animação(self):
        self.evolução()
        
        v = self.troca_imagem()
        
        self.canvas.delete(tk.ALL)

        for j in self.imagens[v]:
            self.canvas.create_image(192//2, 192//2, image = j)
            self.canvas.update()
            time.sleep(0.02)
        
        self.window_tamagotchi.after(0, self.animação)

    def troca_imagem(self):

        if self.p == "squirtle":
            
            if self.sleep <= 30:
                return "squirtle_S"
        
            elif self.hunger <= 30:
                return  "squirtle_F"

            elif self.clean <= 30 :
                return  "squirtle_B"
                
            else:
                return "squirtle_A"
        
        elif self.p == "charmander":
            
            if self.sleep <= 30:
                return  "charmander_S"
        
            elif self.hunger <= 30:
                return  "charmander_F"

            elif self.clean <= 30 :
                return  "charmander_B"
                
            else:
                return "charmander_A"
        
        elif self.p == "bulbasaur":
            
            if self.sleep <= 30:
                return "bulbasaur_S"
        
            elif self.hunger <= 30:
                return "bulbasaur_F"

            elif self.clean <= 30 :
                return "bulbasaur_B"
                
            else:
                return "bulbasaur_A"

        elif self.p == "wartortle":
            
            if self.sleep <= 30:
                return "wartortle_S"
        
            elif self.hunger <= 30:
                return  "wartortle_F"

            elif self.clean <= 30 :
                return  "wartortle_B"
                
            else:
                return "wartortle_A"
        
        elif self.p == "charmeleon":
            
            if self.sleep <= 30:
                return  "charmeleon_S"
        
            elif self.hunger <= 30:
                return  "charmeleon_F"

            elif self.clean <= 30 :
                return  "charmeleon_B"
                
            else:
                return "charmeleon_A"
        
        elif self.p == "ivysaur":
            
            if self.sleep <= 30:
                return "ivysaur_S"
        
            elif self.hunger <= 30:
                return "ivysaur_F"

            elif self.clean <= 30 :
                return "ivysaur_B"
                
            else:
                return "ivysaur_A"                

        elif self.p == "blastoise":
            
            if self.sleep <= 30:
                return "blastoise_S"
        
            elif self.hunger <= 30:
                return  "blastoise_F"

            elif self.clean <= 30 :
                return  "blastoise_B"
                
            else:
                return "blastoise_A"
        
        elif self.p == "charizard":
            
            if self.sleep <= 30:
                return  "charizard_S"
        
            elif self.hunger <= 30:
                return  "charizard_F"

            elif self.clean <= 30 :
                return  "charizard_B"
                
            else:
                return "charizard_A"
        
        elif self.p == "venusaur":
            
            if self.sleep <= 30:
                return "venusaur_S"
        
            elif self.hunger <= 30:
                return "venusaur_F"

            elif self.clean <= 30 :
                return "venusaur_B"
                
            else:
                return "venusaur_A"     
                
app = Janela_Principal()
app.iniciar()