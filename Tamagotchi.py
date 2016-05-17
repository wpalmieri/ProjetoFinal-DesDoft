import tkinter as tk
import time
from datetime import datetime
from tkinter import messagebox

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
        
#        self.theme = "C:\\Users\\Usuario\\Documents\\Insper\\D.S\\Tamagotchi\\Teste Menu Principal\\Música.mp3"
#        self.sound = mp3play.load("Fire Red Main Theme Extended")
#        self.sound.play() 
                
        self.window1.rowconfigure(0, minsize = 100) #Geometria da página
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
        self.salada = tk.PhotoImage(file = "Salada.png")
        self.magikarp = tk.PhotoImage(file = "Magikarp.png")
        self.rare_candy = tk.PhotoImage(file = "Rare_Candy.png")
        self.super_rod = tk.PhotoImage(file = "Super_Rod.png")
        
        # Buttons        
        self.botao1 = tk.Button(self.window_loja, text = "Voltar", height = 2, width = 6)
        self.botao1.grid(row = 0, column = 0)
        self.botao1.configure(command = self.voltar)
        
        self.label2 = tk.Label(self.window_loja, text = "Loja")
        self.label2.grid(row = 0, column = 1, sticky = "nsew")
        
        self.label3 = tk.Label(self.window_loja)
        self.label3.grid(row = 0, column = 2, sticky = "nsew")
        
        self.botao4 = tk.Button(self.window_loja, image = self.bigode)
        self.botao4.grid(row = 1, column = 0, sticky = "nsew")
        
        self.botao5 = tk.Button(self.window_loja, image = self.oculos)
        self.botao5.grid(row = 1, column = 1, sticky = "nsew")
        
        self.botao6 = tk.Button(self.window_loja, image = self.chapeu)
        self.botao6.grid(row = 1, column = 2, sticky = "nsew")
        
        self.botao7 = tk.Button(self.window_loja, image = self.salada)
        self.botao7.grid(row = 3, column = 0, sticky = "nsew")
        
        self.botao8 = tk.Button(self.window_loja, image = self.carne)
        self.botao8.grid(row = 3, column = 1, sticky = "nsew")
        
        self.botao9 = tk.Button(self.window_loja, image = self.magikarp)
        self.botao9.grid(row = 3, column = 2, sticky = "nsew")
        
        self.botao10 = tk.Button(self.window_loja, image = self.rare_candy)
        self.botao10.grid(row = 5, column = 0, sticky = "nsew")
        
        self.botao11 = tk.Button(self.window_loja, image = self.super_rod)
        self.botao11.grid(row = 5, column = 1, sticky = "nsew")
        
        self.botao12 = tk.Button(self.window_loja, text = "12")
        self.botao12.grid(row = 5, column = 2, sticky = "nsew")
        
        
        # Labels        
        self.label13 = tk.Label(self.window_loja, text = "Bigode - $5")
        self.label13.grid(row = 2, column = 0, sticky = "nsew")
        
        self.label14 = tk.Label(self.window_loja, text = "Oculos - $20")
        self.label14.grid(row = 2, column = 1, sticky = "nsew")
        
        self.label15 = tk.Label(self.window_loja, text = "Chapeu - $40")
        self.label15.grid(row = 2, column = 2, sticky = "nsew")
        
        self.label16 = tk.Label(self.window_loja, text = "Salada - $5")
        self.label16.grid(row = 4, column = 0, sticky = "nsew")
        
        self.label17 = tk.Label(self.window_loja, text = "Carne - $20")
        self.label17.grid(row = 4, column = 1, sticky = "nsew")
        
        self.label18 = tk.Label(self.window_loja, text = "Magikarp - $40")
        self.label18.grid(row = 4, column = 2, sticky = "nsew")
        
        self.label19 = tk.Label(self.window_loja, text = "Rare Candy - $75")
        self.label19.grid(row = 6, column = 0, sticky = "nsew")
        
        self.label20 = tk.Label(self.window_loja, text = "Super Rod - $50")
        self.label20.grid(row = 6, column = 1, sticky = "nsew")
        
        self.window_loja.after(0, self.update_money)
                
    def update_money(self):
        self.dinheiros = self.janela_principal.jogo.dinheiro
        self.label3.configure(text = "Dinheiros:\n {0}".format(self.dinheiros))
        self.window_loja.after(10000, self.update_money)
        print(self.dinheiros)
        
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
        
        self.canvas = tk.Canvas(self.window_tamagotchi, width = 192, height = 192)
        self.canvas.configure(bg = "white", highlightthickness = 0)
        self.canvas.grid(row = 2 , column = 0, columnspan = 3)
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
        
        # Atributos do Tamagotchi
        self.hunger = self.last_hunger
        self.clean = self.last_clean
        self.sleep = self.last_sleep
        self.days = self.last_day
        self.xp = self.last_xp
        self.dinheiro = self.last_money
        
        # Geometria da página
        self.window_tamagotchi.rowconfigure(0, minsize = 50)
        self.window_tamagotchi.rowconfigure(1, minsize = 50)
        self.window_tamagotchi.rowconfigure(2, minsize = 250)
        self.window_tamagotchi.rowconfigure(3, minsize = 100)
        
        self.window_tamagotchi.columnconfigure(0, minsize = 100)
        self.window_tamagotchi.columnconfigure(1, minsize = 100)
        self.window_tamagotchi.columnconfigure(2, minsize = 100)
        
        # Labels
        self.label_xp = tk.Label(self.window_tamagotchi)
        self.label_xp.configure(background = 'white')
        self.label_xp.grid(row = 0, column = 0)
        
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
        self.button_feed.grid(row = 3, column = 0, sticky = "nsew")
        self.button_feed.configure(command = self.update_hunger, background = 'white')
        
        self.icone_limpar = tk.PhotoImage(file = "banho_icone.png")
        self.button_clean = tk.Button(self.window_tamagotchi, image = self.icone_limpar, height = 1, width = 5)
        self.button_clean.grid(row = 3, column = 1, sticky = "nsew")
        self.button_clean.configure(command = self.update_clean, background = 'white')      
        
        self.icone_dormir = tk.PhotoImage(file = "dormir_icone.png")
        self.button_sleep = tk.Button(self.window_tamagotchi, image = self.icone_dormir, height = 1, width = 5)
        self.button_sleep.grid(row = 3, column = 2, sticky = "nsew")
        self.button_sleep.configure(command = self.update_sleep, background = 'white')
        
        self.botao_loja = tk.Button(self.window_tamagotchi, text = "Loja", height = 1, width = 6)
        self.botao_loja.grid(row = 0, column = 2)
        self.botao_loja.configure(command = self.acessa_loja)
        

    def reset(self,p):
        self.p = p
        self.hunger = 101
        self.clean = 101
        self.sleep = 101
        self.days = 0
        self.xp = 0
        self.dinheiro = 0
        
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
        
        if self.hunger >= 90:
            
            self.hunger = 101
            
        elif self.hunger >= 100:
            
            return None
            
        else:
            
            self.hunger += 10
            self.xp += 2
        
    
    def update_clean(self):
        
        if self.clean >= 90:
            
            self.clean = 101
            
        elif self.clean >= 100:
            
            return None
            
        else:
            
            self.clean += 10
            self.xp += 2
    
        
    def update_sleep(self):
        
        if self.sleep >= 90:
            
            self.sleep = 101
            
        elif self.sleep >= 100:
            
            return None
            
        else:
            
            self.sleep = 100
            self.xp += 2
            
                    
    def get_hungry(self):
        
        if self.hunger != 0:
            
            self.hunger -= 1
            
            self.label_fome.configure(text = "Fome:\n{0}".format(self.hunger))
            self.label_xp.configure(text = "XP:\n{0}".format(self.xp))
                
        else:
            self.label_fome.configure(text = "Fome:\n{0}".format(self.hunger))
            self.morto()
            
        self.window_tamagotchi.after(1000, self.get_hungry)
        
        
    def get_sleepy(self):
        
        if self.sleep != 0:
        
            self.sleep -= 1
                
            self.label_sono.configure(text = "Sono:\n{0}".format(self.sleep))
            self.label_xp.configure(text = "XP:\n{0}".format(self.xp))
            
        else:
            self.label_sono.configure(text = "Sono:\n{0}".format(self.sleep))
            self.label_xp.configure(text = "XP:\n{0}".format(self.xp))
            
        self.window_tamagotchi.after(1000, self.get_sleepy)
    
    
    def get_dirty(self):
        
        if self.clean != 0:
        
            self.clean -= 1
            
            self.label_saude.configure(text = "Limpeza:\n{0}".format(self.clean))
            self.label_xp.configure(text = "XP:\n{0}".format(self.xp))
            
        else:
            self.label_saude.configure(text = "Limpeza:\n{0}".format(self.clean))
            self.label_xp.configure(text = "XP:\n{0}".format(self.xp))
           
        self.window_tamagotchi.after(1000, self.get_dirty)
    
    
    def pass_day(self):
        
        self.days += 1
        self.xp += 17
        self.dinheiro += 5
            
        self.label_dia.configure(text = "Dia:\n{0}".format(self.days))
            
        self.window_tamagotchi.after(10000, self.pass_day)

  
# ---------------------------------------------------  
# Consequências:
    
    def morto(self):
        tk.messagebox.showinfo ('Morreu', 'Seu pokemon morreu')
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
        save.write("{0}, {1}, {2}, {3}, {4},{5}, {6}, {7}".format(horario, self.days, self.hunger, 
                   self.clean, self.sleep, self.p, self.xp, self.dinheiro))
        save.close()
        
        
#------------------------------------------------------  
# Animação
     
    def animação(self):
        self.lista = []
        self.listagif = []
        self.listaIn = []
        self.v = self.troca_imagem()
        
        for i in range (1,32):
            if self.v == "squirtle_A":
                self.lista.append(tk.PhotoImage(file ='Squirtle/squirtleA%s.gif'%i))
            elif self.v == "squirtle_F":
                self.lista.append(tk.PhotoImage(file ='Squirtle_F/SquirtleF%s.gif'%i))
            elif self.v == "squirtle_S":
                self.lista.append(tk.PhotoImage(file ='Squirtle_S/SquirtleS%s.gif'%i))
            elif self.v == "squirtle_B":
                self.lista.append(tk.PhotoImage(file ='Squirtle_B/SquirtleB%s.gif'%i))
                
            elif self.v == "wartortle_A":
                self.lista.append(tk.PhotoImage(file ='Squirtle/wartortleA%s.gif'%i))
            elif self.v == "wartortle_F":
                self.lista.append(tk.PhotoImage(file ='Squirtle_F/WartortleF%s.gif'%i))
            elif self.v == "wartortle_S":
                self.lista.append(tk.PhotoImage(file ='Squirtle_S/WartortleS%s.gif'%i))
            elif self.v == "wartortle_B":
                self.lista.append(tk.PhotoImage(file ='Squirtle_B/WartortleB%s.gif'%i))
        
            elif self.v == "blastoise_A":
                self.lista.append(tk.PhotoImage(file ='Squirtle/BlastoiseA%s.gif'%i))
            elif self.v == "blastoise_F":
                self.lista.append(tk.PhotoImage(file ='Squirtle_F/BlastoiseF%s.gif'%i))
            elif self.v == "blastoise_S":
                self.lista.append(tk.PhotoImage(file ='Squirtle_S/BlastoiseF%s.gif'%i))
            elif self.v == "blastoise_B":
                self.lista.append(tk.PhotoImage(file ='Squirtle_B/BlastoiseB%s.gif'%i))        
#-----------------------------------------------------------------------------------
            elif self.v == "charmander_A":
                self.lista.append(tk.PhotoImage(file ='Charmander/charmanderA%s.gif'%i))
            elif self.v == "charmander_F":
                self.lista.append(tk.PhotoImage(file ='Charmander_F/charmanderF%s.gif'%i))
            elif self.v == "charmander_S":
                self.lista.append(tk.PhotoImage(file ='Charmander_S/charmanderS%s.gif'%i))
            elif self.v == "charmander_B":
                self.lista.append(tk.PhotoImage(file ='Charmander_B/charmanderB%s.gif'%i))
                
            elif self.v == "charmeleon_A":
                self.lista.append(tk.PhotoImage(file ='Charmander/charmeleonA%s.gif'%i))
            elif self.v == "charmeleon_F":
                self.lista.append(tk.PhotoImage(file ='Charmander_F/charmeleonF%s.gif'%i))
            elif self.v == "charmeleon_S":
                self.lista.append(tk.PhotoImage(file ='Charmander_S/charmeleonS%s.gif'%i))
            elif self.v == "charmeleon_B":
                self.lista.append(tk.PhotoImage(file ='Charmander_B/charmeleonB%s.gif'%i))
        
            elif self.v == "charizard_A":
                self.lista.append(tk.PhotoImage(file ='Charmander/charizardA%s.gif'%i))
            elif self.v == "charizard_F":
                self.lista.append(tk.PhotoImage(file ='Charmander_F/charizardF%s.gif'%i))
            elif self.v == "charizard_S":
                self.lista.append(tk.PhotoImage(file ='Charmander_S/charizardF%s.gif'%i))
            elif self.v == "charizard_B":
                self.lista.append(tk.PhotoImage(file ='Charmander_B/charizardB%s.gif'%i))         

            elif self.v == "bulbasaur_A":
                self.lista.append(tk.PhotoImage(file ='Bulbasaur/bulbasaurA%s.gif'%i))
            elif self.v == "bulbasaur_F":
                self.lista.append(tk.PhotoImage(file ='Bulbasaur_F/bulbasaurF%s.gif'%i))
            elif self.v == "bulbasaur_S":
                self.lista.append(tk.PhotoImage(file ='Bulbasaur_S/bulbasaurS%s.gif'%i))
            elif self.v == "bulbasaur_B":
                self.lista.append(tk.PhotoImage(file ='Bulbasaur_B/bulbasaurB%s.gif'%i))
                
            elif self.v == "ivysaur_A":
                self.lista.append(tk.PhotoImage(file ='Bulbasaur/ivysaurA%s.gif'%i))
            elif self.v == "ivysaur_F":
                self.lista.append(tk.PhotoImage(file ='Bulbasaur_F/ivysaurF%s.gif'%i))
            elif self.v == "ivysaur_S":
                self.lista.append(tk.PhotoImage(file ='Bulbasaur_S/ivysaurS%s.gif'%i))
            elif self.v == "ivysaur_B":
                self.lista.append(tk.PhotoImage(file ='Bulbasaur/ivysaurB%s.gif'%i))
        
            elif self.v == "venusar_A":
                self.lista.append(tk.PhotoImage(file ='Bulbasaur/venusarA%s.gif'%i))
            elif self.v == "venusar_F":
                self.lista.append(tk.PhotoImage(file ='Bulbasaur_F/venusaurF%s.gif'%i))
            elif self.v == "venusar_S":
                self.lista.append(tk.PhotoImage(file ='Bulbasaur_S/venusaurF%s.gif'%i))
            elif self.v == "venusar_B":
                self.lista.append(tk.PhotoImage(file ='Bulbasaur_B/venusaurB%s.gif'%i)) 
        for z in self.lista[::-1]:
            self.listaIn.append(z)
        for k in self.listaIn:
            self.listagif.append(k)
        for j in self.listagif:
            self.canvas.create_image(192/2,192/2,image = j)
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