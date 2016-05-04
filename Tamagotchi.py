<<<<<<< HEAD

###http://stackoverflow.com/questions/13215215/python-tkinter-animation###

import tkinter as tk
import time
import tkinter.messagebox as tkm

class Tamagotchi:
    
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.geometry("300x450+100+100")
        self.window.title("Tamagotchi")
        self.window.resizable(False,False)
        self.window.protocol("WM_DELETE_WINDOW", self.sair)
        
        self.canvas = tk.Canvas(self.window,width=192,height=192)
        self.canvas.grid(row = 2 ,column = 0,columnspan = 3)
        self.v = "squirtle_S"
        self.app()
        
        

        
        # Geometria da página
        self.window.rowconfigure(0, minsize = 50)
        self.window.rowconfigure(1, minsize = 50)
        self.window.rowconfigure(2, minsize = 250)
        self.window.rowconfigure(3, minsize = 100)
        
        self.window.columnconfigure(0, minsize = 100)
        self.window.columnconfigure(1, minsize = 100)
        self.window.columnconfigure(2, minsize = 100)

        
        # Labels
        self.label_dia = tk.Label()
        self.label_dia.configure(text = "Dias de vida:\n {0}" .format(self.update_day()))
        self.label_dia.grid(row = 0, column = 0, columnspan = 4)
        
        self.label_fome = tk.Label()
        self.label_fome.configure(text = "Fome:\n100")
        self.label_fome.grid(row = 1, column = 0)
        
        self.label_saude = tk.Label()
        self.label_saude.configure(text = "Limpeza:\n100")
        self.label_saude.grid(row = 1, column = 1)
        
        
        self.label_sono = tk.Label()
        self.label_sono.configure(text = "Sono:\n100")
        self.label_sono.grid(row = 1, column = 2)
        
        # Imagem
#        self.imagem = tk.PhotoImage(file = "raikou.gif")
#        self.label_imagem = tk.Label()
#        self.label_imagem.configure(image = self.imagem)
#        self.label_imagem.grid(row = 2, column = 0, columnspan = 4)
        
        # Botões
        self.button_feed = tk.Button(self.window, text = "Alimentar", height = 1, width = 5)
        self.button_feed.grid(row = 3, column = 0, sticky = "nsew")
        self.button_feed.configure(command = self.update_hunger)
        
        self.button_clean = tk.Button(self.window, text = "Limpar", height = 1, width = 5)
        self.button_clean.grid(row = 3, column = 1, sticky = "nsew")
        self.button_clean.configure(command = self.update_clean)
        
        
        self.button_sleep = tk.Button(self.window, text = "Dormir", height = 1, width = 5)
        self.button_sleep.grid(row = 3, column = 2, sticky = "nsew")
        self.button_sleep.configure(command = self.update_sleep)
        
        # Atributos do Tamagotchi
        self.hunger = 100
        self.clean = 100
        self.fun = 100
        self.sleep = 100
        self.days = 0
        
# ---------------------------------------------------
# Tempo
        
    def tempo_ao_desligar(self):
        
        # Quando desligar:
        desligou = time.time()
        
        return desligou
    
    def tempo_ao_ligar(self):
        
        # Quando ligar:
        ligou = time.time()
        tkm.showinfo(title = "Em quanto você esteve fora...", message = "...")
        
        return ligou

# ---------------------------------------------------
# Updates:
    
    def image(self):
        pass
    
    
    def update_day(self):
#        day = 0
#        for i in range (0,1000):
#             day = i
#        self.after(1000, self.update_day)
#        return day
        pass
    

    def update_hunger(self):
        pass
    
    
    def update_clean(self):
        pass
    
    
    def update_fun(self):
        pass
    
    
    def update_sleep(self):
        pass
  
  
# ---------------------------------------------------  
# Consequências:
    
    def vivo_morto(self):
        
        if self.hunger <= 0:
            pass
    
    
    def sick(self):
        
        if self.clean <= 0:
            pass
        
    
    def pass_out(self):
        
        if self.sleep <= 0:
            pass
        
        
    def bored(self):
        
        if self.fun <= 20:
            pass
        
        
# --------------------------------------------------
# Iniciar     
     
    def iniciar(self):
        self.window.mainloop()
    
    def sair(self):
        print("oi, estou saindo")
        self.window.quit()
     
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):
#                if v == "charmander_A":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charmander_F":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charmander_S":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charmander_B":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)               
            
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):                
#                elif v == "charmeleon_A":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charmeleon_F":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charmeleon_S":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charmeleon_B":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)               
            
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):
#                elif v == "charizard_A":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charizard_F":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charizard_S":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charizard_B":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)   
                
            
    def animação_squirtle(self):
        self.lista = []
        self.listagif = []
        v = self.v
        
        for i in range (1,32):
            if v == "squirtle_A":
                self.lista.append(tk.PhotoImage(file ='Squirtle/squirtleA%s.gif'%i))
            elif v == "squirtle_F":
                self.lista.append(tk.PhotoImage(file ='Squirtle_F/SquirtleF%s.gif'%i))
            elif v == "squirtle_S":
                self.lista.append(tk.PhotoImage(file ='Squirtle_S/SquirtleS%s.gif'%i))
            elif v == "squirtle_B":
                self.lista.append(tk.PhotoImage(file ='Squirtle_B/SquirtleB%s.gif'%i))
        for k in self.lista:
            self.listagif.append(k)
        for j in self.listagif:
            self.canvas.create_image(192/2,192/2,image = j)
            self.canvas.update()
            time.sleep(0.02)
        self.window.after(0, self.animação_squirtle)

                    
#    def animação_wartortle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):
#                if v == "wartortle_A":
#                    self.lista.append(tk.PhotoImage(file ='Squirtle/wartortleA%s.gif'%i))
#                elif v == "wartortle_F":
#                    self.lista.append(tk.PhotoImage(file ='Squirtle_F/WartortleF%s.gif'%i))
#                elif v == "wartortle_S":
#                    self.lista.append(tk.PhotoImage(file ='Squirtle_S/WartortleS%s.gif'%i))
#                elif v == "wartortle_B":
#                    self.lista.append(tk.PhotoImage(file ='Squirtle_B/WartortleB%s.gif'%i))
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)   
#                    
#    def animação_blastoise(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        
#        for i in range (1,32):
#            if v == "blastoise_A":
#                self.lista.append(tk.PhotoImage(file ='Squirtle/BlastoiseA%s.gif'%i))
#            elif v == "blastoise_F":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_F/BlastoiseF%s.gif'%i))
#            elif v == "blastoise_S":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_S/BlastoiseF%s.gif'%i))
#            elif v == "blastoise_B":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_B/BlastoiseB%s.gif'%i))
#        for k in self.lista:
#            self.listagif.append(k)
#        for j in self.listagif:
#            self.canvas.create_image(192/2,192/2,image = j)
#            self.canvas.update()
#            time.sleep(0.02)   
#                    
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):                    
#                elif v == "bulbasaur_A":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "bulbasaur_F":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "bulbasaur_S":    
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "bulbasaur_B":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)   
                
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):
#                elif v == "ivysaur_A":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "ivysaur_F":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "ivysaur_S":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "ivysaur_B":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)   
                
                
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):
#                elif v == "venusaur_A":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "venusaur_F":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "venusaur_S":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "venusaur_B":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)
    def app(self):
        self.window.after(0, self.animação_squirtle)           
     
tamag = Tamagotchi()
tamag.iniciar()
=======
###http://stackoverflow.com/questions/13215215/python-tkinter-animation###

import tkinter as tk
import time
import tkinter.messagebox as tkm

class Tamagotchi:
    
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.geometry("300x450+100+100")
        self.window.title("Tamagotchi")
        #self.window.resizable(False,False)
        #self.window.protocol("WM_DELETE_WINDOW", self.sair)
        
#        self.canvas = tk.Canvas(self.window,width=192,height=192)
#        self.canvas.grid(row = 2 ,column = 0,columnspan = 3)
#        self.v = "squirtle_S"
#        self.app()
        
        # Atributos do Tamagotchi
        self.hunger = 101
        self.clean = 101
        self.fun = 101
        self.sleep = 101
        self.days = 0
        
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
        self.label_dia.grid(row = 0, column = 0, columnspan = 3)
        
        self.label_fome = tk.Label()
        self.label_fome.grid(row = 1, column = 0)
        
        self.label_saude = tk.Label()
        self.label_saude.grid(row = 1, column = 1)
                
        self.label_sono = tk.Label()
        self.label_sono.grid(row = 1, column = 2)
        
        # Imagem
#        self.imagem = tk.PhotoImage(file = "raikou.gif")
#        self.label_imagem = tk.Label()
#        self.label_imagem.configure(image = self.imagem)
#        self.label_imagem.grid(row = 2, column = 0, columnspan = 4)
        
        # Botões
        self.button_feed = tk.Button(self.window, text = "Alimentar", height = 1, width = 5)
        self.button_feed.grid(row = 3, column = 0, sticky = "nsew")
        self.button_feed.configure(command = self.update_hunger)
        
        self.button_clean = tk.Button(self.window, text = "Limpar", height = 1, width = 5)
        self.button_clean.grid(row = 3, column = 1, sticky = "nsew")
        self.button_clean.configure(command = self.update_clean)      
        
        self.button_sleep = tk.Button(self.window, text = "Dormir", height = 1, width = 5)
        self.button_sleep.grid(row = 3, column = 2, sticky = "nsew")
        self.button_sleep.configure(command = self.update_sleep)
        
        self.window.after(0, self.get_hungry)
        self.window.after(0, self.get_sleepy)
        self.window.after(0, self.get_dirty)
        self.window.after(0, self.pass_day)
        
# ---------------------------------------------------
# Tempo
        
    def tempo_ao_desligar(self):
        
        # Quando desligar:
        desligou = time.time()
        
        return desligou
    
    def tempo_ao_ligar(self):
        
        # Quando ligar:
        ligou = time.time()
        tkm.showinfo(title = "Em quanto você esteve fora...", message = "...")
        
        return ligou

# ---------------------------------------------------
# Updates:
    
    def image(self):
        pass
    
    
    def update_hunger(self):
        
        if self.hunger >= 90:
            
            self.hunger = 101
            
        elif self.hunger >= 100 or self.hunger <= 0:
            
            return None
            
        else:
            
            self.hunger += 10
        
    
    def update_clean(self):
        
        if self.clean >= 90:
            
            self.clean = 101
            
        elif self.clean >= 100 or self.clean <= 0:
            
            return None
            
        else:
            
            self.clean += 10
    
    
    def update_fun(self):
        pass
    
    
    def update_sleep(self):
        
        if self.sleep >= 90:
            
            self.sleep = 101
            
        elif self.sleep >= 100 or self.sleep <= 0:
            
            return None
            
        else:
            
            self.sleep += 10
                    
    
    def get_hungry(self):
            
        self.hunger -= 1
            
        self.label_fome.configure(text = "Fome:\n{0}".format(self.hunger))
            
        self.window.after(1000, self.get_hungry)
        
        
    def get_sleepy(self):
        
        self.sleep -= 1
            
        self.label_sono.configure(text = "Sono:\n{0}".format(self.sleep))
            
        self.window.after(1000, self.get_sleepy)
    
    
    def get_dirty(self):
        
        self.clean -= 1
            
        self.label_saude.configure(text = "Limpeza:\n{0}".format(self.clean))
            
        self.window.after(1000, self.get_dirty)
    
    
    def pass_day(self):
        
        self.days += 1
            
        self.label_dia.configure(text = "Dia:\n{0}".format(self.days))
            
        self.window.after(10000, self.pass_day)
  
  
# ---------------------------------------------------  
# Consequências:
    
    def vivo_morto(self):
        
        if self.hunger <= 0:
            pass
    
    
    def sick(self):
        
        if self.clean <= 0:
            pass
        
    
    def pass_out(self):
        
        if self.sleep <= 0:
            pass
        
        
    def bored(self):
        
        if self.fun <= 20:
            pass
        
        
# --------------------------------------------------
# Iniciar     
     
    def iniciar(self):
        self.window.mainloop()
    
    def sair(self):
        print("oi, estou saindo")
        self.window.quit()
     
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):
#                if v == "charmander_A":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charmander_F":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charmander_S":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charmander_B":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)               
            
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):                
#                elif v == "charmeleon_A":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charmeleon_F":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charmeleon_S":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charmeleon_B":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)               
            
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):
#                elif v == "charizard_A":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charizard_F":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charizard_S":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "charizard_B":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)   
                
            
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        
#        for i in range (1,32):
#            if v == "squirtle_A":
#                self.lista.append(tk.PhotoImage(file ='Squirtle/squirtleA%s.gif'%i))
#            elif v == "squirtle_F":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_F/SquirtleF%s.gif'%i))
#            elif v == "squirtle_S":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_S/SquirtleS%s.gif'%i))
#            elif v == "squirtle_B":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_B/SquirtleB%s.gif'%i))
#        for k in self.lista:
#            self.listagif.append(k)
#        for j in self.listagif:
#            self.canvas.create_image(192/2,192/2,image = j)
#            self.canvas.update()
#            time.sleep(0.02)
#        self.window.after(0, self.animação_squirtle)

                    
#    def animação_wartortle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):
#                if v == "wartortle_A":
#                    self.lista.append(tk.PhotoImage(file ='Squirtle/wartortleA%s.gif'%i))
#                elif v == "wartortle_F":
#                    self.lista.append(tk.PhotoImage(file ='Squirtle_F/WartortleF%s.gif'%i))
#                elif v == "wartortle_S":
#                    self.lista.append(tk.PhotoImage(file ='Squirtle_S/WartortleS%s.gif'%i))
#                elif v == "wartortle_B":
#                    self.lista.append(tk.PhotoImage(file ='Squirtle_B/WartortleB%s.gif'%i))
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)   
#                    
#    def animação_blastoise(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        
#        for i in range (1,32):
#            if v == "blastoise_A":
#                self.lista.append(tk.PhotoImage(file ='Squirtle/BlastoiseA%s.gif'%i))
#            elif v == "blastoise_F":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_F/BlastoiseF%s.gif'%i))
#            elif v == "blastoise_S":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_S/BlastoiseF%s.gif'%i))
#            elif v == "blastoise_B":
#                self.lista.append(tk.PhotoImage(file ='Squirtle_B/BlastoiseB%s.gif'%i))
#        for k in self.lista:
#            self.listagif.append(k)
#        for j in self.listagif:
#            self.canvas.create_image(192/2,192/2,image = j)
#            self.canvas.update()
#            time.sleep(0.02)   
#                    
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):                    
#                elif v == "bulbasaur_A":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "bulbasaur_F":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "bulbasaur_S":    
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "bulbasaur_B":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)   
                
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):
#                elif v == "ivysaur_A":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "ivysaur_F":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "ivysaur_S":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "ivysaur_B":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)   
                
                
#    def animação_squirtle(self):
#        self.lista = []
#        self.listagif = []
#        v = self.v
#        for i in range(100000000000000000000000):
#            for i in range (1,32):
#                elif v == "venusaur_A":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "venusaur_F":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "venusaur_S":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#                elif v == "venusaur_B":
#                    self.lista.append(tk.PhotoImage(file = .gif'%i))
#
#            for k in self.lista:
#                self.listagif.append(k)
#            for j in self.listagif:
#                self.canvas.create_image(192/2,192/2,image = j)
#                self.canvas.update()
#                time.sleep(0.02)
#    def app(self):
#        self.window.after(0, self.animação_squirtle)           
     
tamag = Tamagotchi()
tamag.iniciar()
>>>>>>> d19536b3c0901d718248e0c65adef9ada77ebaef
