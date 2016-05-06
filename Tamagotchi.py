import tkinter as tk
import time
from datetime import datetime
from tkinter import messagebox

class Tamagotchi:
    
    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry("300x450+100+100")
        self.window.title("Tamagotchi")
        self.window.configure(background = 'white')
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.sair)
        
        self.canvas = tk.Canvas(self.window, width = 192, height = 192)
        self.canvas.grid(row = 2 , column = 0, columnspan = 3)
        self.p = "squirtle"
        
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
        
        # Atributos do Tamagotchi
        self.hunger = self.last_hunger
        self.clean = self.last_clean
        self.sleep = self.last_sleep
        self.days = self.last_day
        
        # Geometria da página
        self.window.rowconfigure(0, minsize = 50)
        self.window.rowconfigure(1, minsize = 50)
        self.window.rowconfigure(2, minsize = 250)
        self.window.rowconfigure(3, minsize = 100)
        
        self.window.columnconfigure(0, minsize = 100)
        self.window.columnconfigure(1, minsize = 100)
        self.window.columnconfigure(2, minsize = 100)
        self.window.columnconfigure(3, minsize = 100)
        
        # Labels
        self.label_dia = tk.Label()
        self.label_dia.configure(background = 'white')
        self.label_dia.grid(row = 0, column = 0, columnspan = 3)
        
        self.label_fome = tk.Label()
        self.label_fome.configure(background = 'white')
        self.label_fome.grid(row = 1, column = 0)
        
        self.label_saude = tk.Label()
        self.label_saude.configure(background = 'white')
        self.label_saude.grid(row = 1, column = 1)
                
        self.label_sono = tk.Label()
        self.label_sono.configure(background = 'white')
        self.label_sono.grid(row = 1, column = 2)
        
        # Botões
        self.icone_comer = tk.PhotoImage(file = "comer_icone.png")
        self.button_feed = tk.Button(self.window, image = self.icone_comer, height = 1, width = 5)
        self.button_feed.grid(row = 3, column = 0, sticky = "nsew")
        self.button_feed.configure(command = self.update_hunger, background = 'white')
        
        self.icone_limpar = tk.PhotoImage(file = "banho_icone.png")
        self.button_clean = tk.Button(self.window, image = self.icone_limpar, height = 1, width = 5)
        self.button_clean.grid(row = 3, column = 1, sticky = "nsew")
        self.button_clean.configure(command = self.update_clean, background = 'white')      
        
        self.icone_dormir = tk.PhotoImage(file = "dormir_icone.png")
        self.button_sleep = tk.Button(self.window, image = self.icone_dormir, height = 1, width = 5)
        self.button_sleep.grid(row = 3, column = 2, sticky = "nsew")
        self.button_sleep.configure(command = self.update_sleep, background = 'white')
        
        self.window.after(0, self.get_hungry)
        self.window.after(0, self.get_sleepy)
        self.window.after(0, self.get_dirty)
        self.window.after(0, self.pass_day)
        self.window.after(0, self.animação)
        
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
        
    
    def update_clean(self):
        
        if self.clean >= 90:
            
            self.clean = 101
            
        elif self.clean >= 100:
            
            return None
            
        else:
            
            self.clean += 10
    
        
    def update_sleep(self):
        
        if self.sleep >= 90:
            
            self.sleep = 101
            
        elif self.sleep >= 100:
            
            return None
            
        else:
            
            self.sleep = 100
                    
#botões    
    def get_hungry(self):
        
        if self.hunger != 0:
            
            self.hunger -= 1
            
            self.label_fome.configure(text = "Fome:\n{0}".format(self.hunger))
                
        else:
            self.label_fome.configure(text = "Fome:\n{0}".format(self.hunger))
            self.morto()
            
            
            
        self.window.after(1000, self.get_hungry)
        
        
    def get_sleepy(self):
        
        if self.sleep != 0:
        
            self.sleep -= 1
                
            self.label_sono.configure(text = "Sono:\n{0}".format(self.sleep))
        else:
            self.label_sono.configure(text = "Sono:\n{0}".format(self.sleep))
            
            
        self.window.after(1000, self.get_sleepy)
    
    
    def get_dirty(self):
        
        if self.clean != 0:
        
            self.clean -= 1
            
            self.label_saude.configure(text = "Limpeza:\n{0}".format(self.clean))
            
        else:
            self.label_saude.configure(text = "Limpeza:\n{0}".format(self.clean))
           
        self.window.after(1000, self.get_dirty)
    
    
    def pass_day(self):
        
        self.days += 1
            
        self.label_dia.configure(text = "Dia:\n{0}".format(self.days))
            
        self.window.after(10000, self.pass_day)
  
  
# ---------------------------------------------------  
# Consequências:
    
    def morto(self):
        tk.messagebox.showinfo ('Morreu', 'seu pokemon morreu')
        self.window.quit()

#    
#    def sujo(self):
#        return f
    
#    def sonolento(self):
#        return s
        
# --------------------------------------------------
# Iniciar e sair     
     
    def iniciar(self):
        self.window.mainloop()
    
    def sair(self):
        
        horario = datetime.now().time()
        
        save = open('Save', 'a')
        save.write("\n{0}, {1}, {2}, {3}, {4}".format(horario, self.days, self.hunger, 
                   self.clean, self.sleep))
        save.close()
        
        self.window.quit()
        
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
                
#            elif self.v == "wartortle_A":
#                self.lista.append(tk.PhotoImage(file ='Squirtle/wartortleA%s.gif'%i))
#            elif self.v == "wartortle_F":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_F/WartortleF%s.gif'%i))
#            elif self.v == "wartortle_S":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_S/WartortleS%s.gif'%i))
#            elif self.v == "wartortle_B":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_B/WartortleB%s.gif'%i))
#        
#            elif self.v == "blastoise_A":
#                self.lista.append(tk.PhotoImage(file ='Squirtle/BlastoiseA%s.gif'%i))
#            elif self.v == "blastoise_F":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_F/BlastoiseF%s.gif'%i))
#            elif self.v == "blastoise_S":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_S/BlastoiseF%s.gif'%i))
#            elif self.v == "blastoise_B":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_B/BlastoiseB%s.gif'%i))        
##-----------------------------------------------------------------------------------
#            elif self.v == "charmander_A":
#                self.lista.append(tk.PhotoImage(file ='Charmander/charmanderA%s.gif'%i))
#            elif self.v == "charmander_F":
#                self.lista.append(tk.PhotoImage(file ='Charmander_F/charmanderF%s.gif'%i))
#            elif self.v == "charmander_S":
#                self.lista.append(tk.PhotoImage(file ='Charmander_S/charmanderS%s.gif'%i))
#            elif self.v == "charmander_B":
#                self.lista.append(tk.PhotoImage(file ='Charmander_B/charmanderB%s.gif'%i))
#                
#            elif self.v == "charmeleon_A":
#                self.lista.append(tk.PhotoImage(file ='Charmeleon/charmeleonA%s.gif'%i))
#            elif self.v == "charmeleon_F":
#                self.lista.append(tk.PhotoImage(file ='Charmeleon_F/charmeleonF%s.gif'%i))
#            elif self.v == "charmeleon_S":
#                self.lista.append(tk.PhotoImage(file ='Charmeleon_S/charmeleonS%s.gif'%i))
#            elif self.v == "charmeleon_B":
#                self.lista.append(tk.PhotoImage(file ='Charmeleon_B/charmeleonB%s.gif'%i))
#        
#            elif self.v == "charizard_A":
#                self.lista.append(tk.PhotoImage(file ='Charizard/charizardA%s.gif'%i))
#            elif self.v == "charizard_F":
#                self.lista.append(tk.PhotoImage(file ='Charizard_F/charizardF%s.gif'%i))
#            elif self.v == "charizard_S":
#                self.lista.append(tk.PhotoImage(file ='Charizard_S/charizardF%s.gif'%i))
#            elif self.v == "charizard_B":
#                self.lista.append(tk.PhotoImage(file ='Charizard_B/charizardB%s.gif'%i))         
#
#            elif self.v == "bulbasaur_A":
#                self.lista.append(tk.PhotoImage(file ='Bulbasaur/bulbasaurA%s.gif'%i))
#            elif self.v == "bulbasaur_F":
#                self.lista.append(tk.PhotoImage(file ='Bulbasaur_F/bulbasaurF%s.gif'%i))
#            elif self.v == "bulbasaur_S":
#                self.lista.append(tk.PhotoImage(file ='Bulbasaur_S/bulbasaurS%s.gif'%i))
#            elif self.v == "bulbasaur_B":
#                self.lista.append(tk.PhotoImage(file ='Bulbasaur_B/bulbasaurB%s.gif'%i))
#                
#            elif self.v == "ivysaur_A":
#                self.lista.append(tk.PhotoImage(file ='Ivysaur/ivysaurA%s.gif'%i))
#            elif self.v == "ivysaur_F":
#                self.lista.append(tk.PhotoImage(file ='Ivysaur_F/ivysaurF%s.gif'%i))
#            elif self.v == "ivysaur_S":
#                self.lista.append(tk.PhotoImage(file ='Ivysaur_S/ivysaurS%s.gif'%i))
#            elif self.v == "ivysaur_B":
#                self.lista.append(tk.PhotoImage(file ='Ivysaur_B/ivysaurB%s.gif'%i))
#        
#            elif self.v == "venusar_A":
#                self.lista.append(tk.PhotoImage(file ='Venusar/venusarA%s.gif'%i))
#            elif self.v == "venusar_F":
#                self.lista.append(tk.PhotoImage(file ='Venusar_F/venusaurF%s.gif'%i))
#            elif self.v == "venusar_S":
#                self.lista.append(tk.PhotoImage(file ='Venusar_S/venusaurF%s.gif'%i))
#            elif self.v == "venusar_B":
#                self.lista.append(tk.PhotoImage(file ='Venusar_B/venusaurB%s.gif'%i)) 
        for z in self.lista[::-1]:
            self.listaIn.append(z)
        for k in self.listaIn:
            self.listagif.append(k)
        for j in self.listagif:
            self.canvas.create_image(192/2,192/2,image = j)
            self.canvas.update()
            time.sleep(0.02)
        self.window.after(0, self.animação)         

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


tamag = Tamagotchi()
tamag.iniciar()