
###http://stackoverflow.com/questions/13215215/python-tkinter-animation###

import tkinter as tk
import time
import tkinter.messagebox as tkm

class Tamagotchi:
    
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.geometry("400x470+100+100")
        self.window.title("Tamagotchi")
        

        
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
        self.label_dia.configure(text = "Dias de vida:\n {0}" .format(self.update_day()))
        self.label_dia.grid(row = 0, column = 0, columnspan = 4)
        
        self.label_fome = tk.Label()
        self.label_fome.configure(text = "Fome:\n100")
        self.label_fome.grid(row = 1, column = 0)
        
        self.label_saude = tk.Label()
        self.label_saude.configure(text = "Limpeza:\n100")
        self.label_saude.grid(row = 1, column = 1)
        
        self.label_diversao = tk.Label()
        self.label_diversao.configure(text = "Diversão:\n100")
        self.label_diversao.grid(row = 1, column = 2)
        
        self.label_sono = tk.Label()
        self.label_sono.configure(text = "Sono:\n100")
        self.label_sono.grid(row = 1, column = 3)
        
        # Imagem
        self.imagem = tk.PhotoImage(file = "normal.gif")
        self.label_imagem = tk.Label()
        self.label_imagem.configure(image = self.imagem)
        self.label_imagem.grid(row = 2, column = 0, columnspan = 4)
        
        # Botões
        self.button_feed = tk.Button(self.window, text = "Alimentar", height = 1, width = 5)
        self.button_feed.grid(row = 3, column = 0, sticky = "nsew")
        self.button_feed.configure(command = self.update_hunger)
        
        self.button_clean = tk.Button(self.window, text = "Limpar", height = 1, width = 5)
        self.button_clean.grid(row = 3, column = 1, sticky = "nsew")
        self.button_clean.configure(command = self.update_clean)
        
        self.button_fun = tk.Button(self.window, text = "Brincar", height = 1, width = 5)
        self.button_fun.grid(row = 3, column = 2, sticky = "nsew")
        self.button_fun.configure(command = self.update_fun)
        
        self.button_sleep = tk.Button(self.window, text = "Dormir", height = 1, width = 5)
        self.button_sleep.grid(row = 3, column = 3, sticky = "nsew")
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

     
tamag = Tamagotchi()
tamag.iniciar()
