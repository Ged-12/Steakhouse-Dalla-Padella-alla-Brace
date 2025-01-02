from tkinter import Tk, Button, Label, Entry, Spinbox, messagebox               #Importazione moduli da tkinter                   
from PIL import Image, ImageTk                                                  #Importazione moduli da pillow per gestione immagini
from Ordinazione import Ordinazione                                             #Importazione da Ordinazione della classe Ordinazione
from Globali import Ristorante, Ordine                                          #Importazione da Globali della classe Ristorante e Ordine
import tkinter.font                                                             #Importazione modulo font tkinter

class Prenotazione():  
    def __init__(self):
        Ristorante()                                                            #Crea oggetto ristorante per generazione occupazione tavoli
        self.gui()                                                              #Avvia GUI

    #Metodo impostazione GUI
    def gui(self):
        self.w1 = Tk()                                                          #Creazione finestra
        self.w1.geometry('300x180')                                             #Impostazione grandezza
        self.w1.resizable(False, False)                                         #Impedisce allargamento finestra
        self.w1.configure(bg='#ffffff')                                         #Impostazione colore
        self.w1.title("Dalla Padella alla Brace: Prenotazione")                 #Impostazione titolo
        self.w1.iconbitmap("./Icona.ico")                                       #Impostazione icona
        
        self.label1 = Label(self.w1, text="N° Persone", anchor='w', font=tkinter.font.Font(family="Calibri", size=9))#Creazione label
        self.label1.place(x=20, y=20, width=90, height=22)#Posizionamento label
        
        self.label2 = Label(self.w1, text="Intestatario Tavolo", anchor='w', font=tkinter.font.Font(family="Calibri", size=9))#Creazione label
        self.label2.place(x=20, y=60, width=120, height=22)#Posizionamento label
        
        self.label3 = Label(self.w1, text="Tavolo scelto", anchor='w', font=tkinter.font.Font(family="Calibri", size=9))#Creazione label
        self.label3.place(x=20, y=100, width=90, height=22)#Posizionamento label
        
        self.ltext1 = Entry(self.w1, font=tkinter.font.Font(family="Calibri", size=9))#Creazione casella di testo inserimento intestatario
        self.ltext1.place(x=180, y=60, width=110, height=22)#Posionamento casella di testo
        
        self.spin1 = Spinbox(self.w1, from_=1, to=Ristorante.Persone_per_tavolo, width=10, font=tkinter.font.Font(family="Calibri", size=9))#Creazione spinbox per inserimento numero persone fino a massimo numero persone per tavolo
        self.spin1.place(x=180, y=20, width=40, height=22)#Posizionamento spinbox
        
        self.spin2 = Spinbox(self.w1, from_=1, to=Ristorante.Numero_Tavoli, increment=1, font=tkinter.font.Font(family="Calibri", size=9))#Creazione spinbox per inserimento numero di tavolo scelto fino a il numero massimo di tavoli
        self.spin2.place(x=180, y=100, width=40, height=22)#Posionamento spinbox

        self.button1 = Button(self.w1, text="Avanti", font=tkinter.font.Font(family="Calibri", size=9), command=self.Verifica_Prenotazione)#Creazione pulsante per acquisizione dati prenotazione e passaggio a prossima finestra
        self.button1.place(x=100, y=150, width=90, height=22)#Posizionamento pulsante

        self.image3 = Image.open("./i.png")
        self.image3 = ImageTk.PhotoImage(self.image3.resize((30, 22)))#Impostazione grandezza immagine pulsante
        self.button2 = Button(self.w1, font=tkinter.font.Font(family="Calibri", size=9), image=self.image3, command=self.Verifica_Occupazione_Tavoli)#Creazione pulsante per ricevere informazioni sul occupazione dei tavoli con immagine i
        self.button2.place(x=110, y=100, width=30, height=22)#Posizionamento pulsante

    #Metodo creazione messaggio informazione occupazione tavoli
    def Verifica_Occupazione_Tavoli(self):
        messaggio = ""#Inizializzazione messaggio
        for i in range(Ristorante.Numero_Tavoli):#For per creazione informazione per ciascun tavolo
            if(Ristorante.Occupazione_Tavoli[i] == True):
                stato = "Occupato"#Se tavolo Occupato segna stato
            else:
                stato = "Libero"#Se libero segna stato
            messaggio += f"Tavolo {i + 1}: {stato}\n"#Formazione messaggio
        messagebox.showinfo("Disponibilità", messaggio)#Visualizzazione messaggio

    #Metodo acquisizione informazioni prenotazione e verifica
    def Verifica_Prenotazione(self):
        Ordine.Numero_Persone= int(self.spin1.get())#Acquisizione numero di persone da spinbox
        if(Ordine.Numero_Persone <= 0):#Verifica se valore inferiore o uguale a 0
            messagebox.showerror("Persone", "Numero persone non consentito")#Avvisa
            return
        elif(Ordine.Numero_Persone > Ristorante.Persone_per_tavolo):#Verifica se valore superiore a limite ristorante
            messagebox.showerror("Persone", f"Numero persone superiore a numero persone massimo per tavolo\n(MAX: {Ristorante.Persone_per_tavolo})")#Avvisa
            return

        Ordine.Intestatario = self.ltext1.get()#Acquisizione intestatario del tavolo da spinbox
        if(len(Ordine.Intestatario)==0):#Verifica se Intestatario è vuoto
            messagebox.showerror("Intestatario", "Intestatario non può essere vuoto o nullo")#Avvisa
            return
        
        Ordine.Numero_Tavolo = int(self.spin2.get())#Acquisizione numero tavolo scelto da spinbox
        if(Ordine.Numero_Tavolo <= 0):#Verifica se il numero inserito è inferiore o uguale a zero
            messagebox.showerror("Tavoli", "Numero tavolo non consentito")#Avvisa
            return
        elif(Ordine.Numero_Tavolo > Ristorante.Numero_Tavoli):#Verifica se superiore a numero tavoli
            messagebox.showerror("Tavoli", f"Numero tavolo scelto superiore al numero di tavoli presenti\n(MAX: {Ristorante.Numero_Tavoli})")#Avvisa
            return
        if(Ristorante.Occupazione_Tavoli[Ordine.Numero_Tavolo-1] == True):#Verifica disponibilità tavolo
            messagebox.showerror("Disponibilità", "Tavolo occupato")#Avvisa
            return

        # Mostra messaggio di conferma
        risposta = messagebox.askyesno("Conferma", f"Hai inserito:\nN° Persone: {Ordine.Numero_Persone}\nIntestatario: {Ordine.Intestatario}\nTavolo: {Ordine.Numero_Tavolo}\nConferma?")
        if(risposta == True):#Se accetta
            self.w1.destroy()#Chiudi finestra
            Ordinazione()#Passa a prossima finestra