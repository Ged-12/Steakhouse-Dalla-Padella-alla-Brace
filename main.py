from tkinter import Tk, Canvas, Button, Menu, simpledialog, messagebox      #Importazione moduli da tkinter
from PIL import Image, ImageTk                                              #Importazione moduli da pillow per gestione immagini
from Globali import Ristorante                                              #Importazione da Globali della classe Ristorante
from Prenotazione import Prenotazione                                       #Importazione da Prenotazione della classe Prenotazione
import tkinter.font                                                         #Importazione modulo font tkinter
import json                                                                 #Importazione modulo json 
import os                                                                   #Importazione modulo os


class Inizio():
    def __init__(self):
        self.gui()                                                          #Avvia GUI

    #Metodo impostazione GUI
    def gui(self):

        self.w1 = Tk()                                                      #Creazione finestra
        self.w1.geometry('560x350')                                         #Impostazione grandezza
        self.w1.configure(bg='#ffffff')                                     #Impostazione colore
        self.w1.title("Dalla Padella alla Brace")                           #Impostazione titolo
        self.w1.iconbitmap("./Icona.ico")                                   #Impostazione icona

        self.menubar = Menu(self.w1)                                        #Creazione menubar
        self.w1.config(menu=self.menubar)                                   #Aggiunta a finestra
        self.ConfigMenu = Menu(self.menubar)                                #Creazione menu
        self.menubar.add_cascade(label="Configurazione",menu=self.ConfigMenu)#Aggiunta a menubar e label
        self.ConfigMenu.add_command(label="N°Tavoli",command=self.ModificaTavoli)#Aggiunta opzione per modifica numero tavoli
        self.ConfigMenu.add_command(label="N°Persone*Tavolo",command=self.ModificaPersoneTavoli)#Aggiunta opzione per modifica numero persone per tavolo

        self.subJSON = Menu(self.ConfigMenu)                                #Creazione sottomenu
        self.ConfigMenu.add_cascade(label="JSON", menu=self.subJSON)        #Aggiunta a Menu esistente
        self.subJSON.add_command(label="Importa", command=self.Importa_JSON)#Aggiunta opzione per importazione menu tramite JSON a sottomenu

        self.image2 = Canvas(self.w1, bg='#ffffff')                         #Creazione Canvas 
        self.image2.place(x=-9, y=-9, width=573, height=359)                #Impostazione Canvas
        self.image2i = Image.open("./logo transp 80.png")                   #Apertura immagine
        self.image2img = ImageTk.PhotoImage(self.image2i.resize((573, 359)))#Impostazione immagine
        self.image2.create_image(0, 0, image=self.image2img, anchor='nw')   #Aggiunta immagine a canvas
        
        self.button1 = Button(self.w1, text="Inizia", font=tkinter.font.Font(family="Calibri", size=12), command=self.Inizio)#Creazione pulsante di Inizio
        self.button1.place(x=60, y=180, width=428, height=62)               #Posizionamento pulsante

    #Metodo modifica numero tavoli
    def ModificaTavoli(self):
        num_tavoli = simpledialog.askinteger("Imposta Tavoli", "Inserisci il numero di tavoli:", minvalue=1)#Acquisizione nuovo valore
        Ristorante.Numero_Tavoli = num_tavoli                               #Modifica

    #Metodo modifica numero persone per tavolo
    def ModificaPersoneTavoli(self):
        num_persone = simpledialog.askinteger("Imposta Persone", "Inserisci il numero di persone per tavolo:", minvalue=1)#Acquisizione nuovo valore
        Ristorante.Persone_per_tavolo = num_persone                         #Modifica

    #Metodo importazione menu tramite JSON
    def Importa_JSON(self):
        nomefile = ""                                                       #Inizializza nomefile
        nomefile = simpledialog.askstring("Inserire file", "Inserisci nome file con estensione JSON",)#Acquisizione nomefile
        if not nomefile.lower().endswith('.json'):                          #Controllo se nomefile finisce con estensione convertendo il nomefile in piccolo 
            messagebox.showerror("Errore", "Il file deve avere l'estensione .json")#Avvisa
            return
        if os.path.exists(nomefile):#Controlla se il file esiste
            with open(nomefile, 'r', encoding='utf-8') as file:# Apri file
                content = file.read()#Leggi il contenuto del file
                        
                #Controlli se il contenuto è valido
            if content.strip() == "":  # Controlla se il file è vuoto
                messagebox.showerror("Errore", "Il file è vuoto.")#Avvisa
                return
            else:
                if content.startswith('{'):#Verifica se il contenuto inizia con '{'
                    is_valid_json = False#Indicatore validità
                    try:
                        json.loads(content)#Prova a caricare il JSON
                        is_valid_json = True
                    except:
                        is_valid_json = False

                    if is_valid_json:#Se il caricamento è avvenuto con successo
                        menu = json.loads(content)#Carica il JSON
                        Ristorante.Menu = menu#Modifica menu ristorante
                        messagebox.showinfo("Successo", "File JSON importato con successo.")#Avvisa
                    else:
                        messagebox.showerror("Errore", "Errore caricamento JSON: formato non valido.")#Avvisa
                else:
                    messagebox.showerror("Errore", "Errore caricamento JSON: il contenuto non inizia con '{' o '['.")#Avvisa
        else:
            messagebox.showerror("Errore", "File non trovato.")  # Avvisa

    #Metodo Se pulsante viene premuto
    def Inizio(self):
        self.w1.destroy()                                                   #Chiudi finestra
        Prenotazione()                                                      #Passa alla prossima finestra

if __name__ == '__main__':                                                  #Condizione che verifica che il programma sia principale e non importato
    a = Inizio()                                                            #Crea un'istanza della classe Inizio
    a.w1.mainloop()                                                         #Avvia il ciclo principale dell'interfaccia grafica