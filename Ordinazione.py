from tkinter import Tk, Frame, Button, Label, Spinbox, messagebox               #Importazione moduli da tkinter
from tkinter.ttk import Notebook                                                #Importazione modulo per creazione tab da tkinter
from PIL import Image, ImageTk                                                  #Importazione moduli da pillow per gestione immagini
from Globali import Ristorante, Ordine                                          #Importazione da Globali della classe Ristorante e Ordine
from Pagamento import Pagamento                                                 #Importazione da Pagamento della classe Pagamento
import tkinter.font                                                             #Importazione modulo font tkinter

class Ordinazione():
    def __init__(self):
        self.Spinboxes = []                                                     #Creazione lista per archiviazione spinbox
        self.gui()                                                              #Avvio GUI

    #Metodo impostazione GUI
    def gui(self):
        
        self.w1 = Tk()                                                          #Creazione Finestra
        self.w1.geometry('350x450')                                             #Impostazione finestra
        self.w1.configure(bg = '#ffffff')                                       #Impostazione colore
        self.w1.title("Dalla Padella alla Brace: Ordinazione")                  #Impostazione titolo
        self.w1.iconbitmap("./Icona.ico")                                       #Impostazione icona

        self.LabelTotale = Label(self.w1, anchor='w', font = tkinter.font.Font(family = "Calibri", size = 9))#Creazione label per il costo totale
        self.LabelTotale.place(x = 18, y = 410, width = 90, height = 22)#Posizionamento label
    
        self.button1 = Button(self.w1, text = "Avanti", font = tkinter.font.Font(family = "Calibri", size = 9), command=self.Pagamento)#Creazione pulsante per acquisizione ordine e passaggio alla fase di Pagamento
        self.button1.place(x = 240, y = 410, width = 90, height = 22)#Posizionamento pulsante

        self.notebook = Notebook(self.w1)#Creazione base per le tab

        self.image1 = Image.open("./i.png")#Apertura immagine
        self.image1 = ImageTk.PhotoImage(self.image1.resize((30, 22)))#Impostazione immagine del pulsante

        self.tab1 = Frame(self.notebook, width=350, height=375, bg = '#ffffff')#Creazione Frame della tab
        self.notebook.add(self.tab1, text = "Carne")#Aggiunta della tab alla base e titolo
        self.Grafica_Piatti(self.tab1,0)#Richiamo metodo creazione elementi nella tab con inserimento della tab e inizio elementi menu associati

        self.tab2 = Frame(self.notebook, width=350, height=375, bg = '#ffffff')
        self.notebook.add(self.tab2, text = "Contorni")
        self.Grafica_Piatti(self.tab2,9)

        self.tab3 = Frame(self.notebook, width=350, height=375, bg = '#ffffff')
        self.notebook.add(self.tab3, text = "Dolci")
        self.Grafica_Piatti(self.tab3,18)

        self.tab4 = Frame(self.notebook, width=350, height=375, bg = '#ffffff')
        self.notebook.add(self.tab4, text = "Bibite")
        self.Grafica_Piatti(self.tab4,27)

        self.notebook.pack()#Affiancamento elementi tab

    #Metodo aggiunta grafica elementi menu    
    def Grafica_Piatti(self,tab,inizio):
        Y = 26#Costante asse y iniziale
        menu = list(Ristorante.Menu.items())#Creazione lista a partire dagli elementi del menu
        for i in range(inizio, inizio + 9):#For per aggiunta elementi, ogni sezione ha massimo 9 piatti
            piatto, dettagli = menu[i]#Scomposizione elementi lista in piatto e dettagli
            prezzo = f"{dettagli['prezzo']:.2f}"#Accesso al prezzo del piatto ed impostazione come float a due cifre

            label = Label(tab, text=f"{piatto}: €{prezzo}", anchor='w', font=tkinter.font.Font(family="Calibri", size=9))#Creazione label piatto menu con prezzo
            label.place(x=18, y = Y, width=200, height=22)

            button = Button(tab, image=self.image1, command=lambda p=piatto: self.Info_Piatti(p))#Creazione pulsante associato a piatto che esegue metodo per la visulizzazione degli ingredienti
            button.place(x = 200, y = Y, width = 30, height = 22)#Posizionamento pulsante

            spinbox = Spinbox(tab, from_=0, to=Ordine.Numero_Persone, width=10, font=tkinter.font.Font(family="Calibri", size=9), command=self.Totale)#Creazione spinbox per inserimento quantità prodotto con massimo al numero di persone selezionato e che esegue ad ogni modifica metodo per la visualizzazione del prezzo totale
            spinbox.place(x=290, y = Y, width=40, height=22)#Posizionamento spinbox
            self.Spinboxes.append((piatto, spinbox))#Aggiunta spinbox a lista di doppi

            Y += 40#Incremento asse y

    #Metodo per la visualizzazione degli ingredienti
    def Info_Piatti(self,piatto):

        ingredienti = ", ".join(Ristorante.Menu[piatto]['ingredienti'])#Creazione stringa a partire dalla lista di ingredienti del piatto 
        messagebox.showinfo(piatto, f"Ingredienti: {ingredienti}")#visualizzazione ingredienti attraverso messagebox

    #Metodo visualizzazione prezzo totale
    def Totale(self):
        Ordine.Totale=0#Inizializzazione totale
        for piatto, spinbox in self.Spinboxes:#For per ottenimento quantità da spinbox e prezzi piatti
            quantita = int(spinbox.get())#Acquisizione quantita da Spinbox
            if (quantita>0):#Verifica se la quantità è maggiore di 0
                prezzo = Ristorante.Menu[piatto]["prezzo"]#Acquisizione prezzo piatto
                Ordine.Totale += prezzo * quantita#Calcolo prezzo totale
        self.LabelTotale.config(text=f"Totale: €{Ordine.Totale:.2f}")#Visualizza prezzo totale su label

    #Metodo acquisizione e visualizzazione ordine e passaggio a pagamento
    def Pagamento(self):
        messaggio = "Hai ordinato:\n"#Inizializzazione messaggio
        Ordine.Totale = 0#Inizializzazione prezzo totale

        for piatto, spinbox in self.Spinboxes:#For per ottenimento valori spinbox e prezzi piatti
            quantita = int(spinbox.get())#Acquisizione quantita da spinbox
            if (quantita > Ordine.Numero_Persone):#Verifica se valore superiore a numero di persone della prenotazione
                messagebox.showerror("Piatti", f"La quantità non deve superare il numero di persone a tavola\n(MAX: {Ordine.Numero_Persone})")#Avvisa
                return
            elif (quantita > 0):#Verifica se quantità maggiore di zero
                prezzo = Ristorante.Menu[piatto]["prezzo"]#Acquisizione prezzo piatto
                Ordine.Ordinazione[piatto] = quantita#Aggiunta piatto e quantità a ordinazione
                Ordine.Totale += prezzo * quantita#Calcolo prezzo totale
                messaggio += f"{piatto}: {quantita} x €{prezzo:.2f} = €{(prezzo * quantita):.2f}\n"#Creazione messaggio conferma ordinazione

        if Ordine.Ordinazione:#Verifica se Ordinazione non è vuota
            messaggio += f"\nTotale: €{Ordine.Totale:.2f}\n\nVuoi procedere al pagamento?"#Conclusione costruzione messaggio

            conferma = messagebox.askyesno("Conferma Ordinazione", messaggio)#Visualizzazione ordine attraverso messagebox

            if conferma:#Se conferma
                self.w1.destroy()#Chiudi Finestra
                Pagamento()#Passa alla prossima finestra
            else:
                Ordine.Ordinazione = {}#Se non accetta, azzera ordinazione
                return