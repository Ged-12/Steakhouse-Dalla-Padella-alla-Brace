from tkinter import Tk, Button, Radiobutton, messagebox                                         #Importazione moduli da tkinter
from Globali import Ordine                                                                      #Importazione da Globali della classe Ordine
import tkinter.font                                                                             #Importazione modulo font tkinter

class Pagamento:
    def __init__(self):
        self.gui()                                                                              #Avvio GUI

    def gui(self):
        self.w1 = Tk()                                                                          #Creazione Finestra
        self.w1.geometry('320x190')                                                             #Impostazione grandezza
        self.w1.configure(bg='#ffffff')                                                         #Impostazione colore
        self.w1.title("Dalla Padella alla Brace: Pagamento")                                    #Impostazione titolo
        self.w1.iconbitmap("./Icona.ico")                                                       #Impostazione icona

        #Creazione pulsanti di opzioni per metodo di pagamento con commando che esegue metodo per acquisizione scelta metodo e archiviazione
        self.radio1 = Radiobutton(self.w1, text="Visa", variable=Ordine.Metodo_Pagamento, value="Visa", anchor='w', font=tkinter.font.Font(family="Calibri", size=9), command=lambda: self.seleziona_metodo("Visa"))
        self.radio1.place(x=30, y=30, width=90, height=22)
        self.radio2 = Radiobutton(self.w1, text="Mastercard", variable=Ordine.Metodo_Pagamento, value="Mastercard", anchor='w', font=tkinter.font.Font(family="Calibri", size=9), command=lambda: self.seleziona_metodo("Mastercard"))
        self.radio2.place(x=190, y=30, width=90, height=22)
        self.radio3 = Radiobutton(self.w1, text="Bancomat", variable=Ordine.Metodo_Pagamento, value="Bancomat", anchor='w', font=tkinter.font.Font(family="Calibri", size=9), command=lambda: self.seleziona_metodo("Bancomat"))
        self.radio3.place(x=30, y=80, width=90, height=22)
        self.radio4 = Radiobutton(self.w1, text="Contanti", variable=Ordine.Metodo_Pagamento, value="Contanti", anchor='w', font=tkinter.font.Font(family="Calibri", size=9), command=lambda: self.seleziona_metodo("Contanti"))
        self.radio4.place(x=190, y=80, width=90, height=22)

        self.button1 = Button(self.w1, text="Procedi", font=tkinter.font.Font(family="Calibri", size=9), command=self.procedi_pagamento)#Creazione pulsante per esecuzione pagamento
        self.button1.place(x=110, y=130, width=90, height=22)#Posizionamento pulsante

    #Metodo acquisizione metodo di pagamento
    def seleziona_metodo(self, metodo):
        Ordine.Metodo_Pagamento = metodo#Archiviazione metodo di pagamento

    def procedi_pagamento(self):
        if Ordine.Metodo_Pagamento == "": #Controlla se è stato selezionato un metodo di pagamento
            messagebox.showerror("Errore", "Seleziona un metodo di pagamento.")#Avvisa
            return

        #Calcola commissioni
        commissioni = 0
        if Ordine.Metodo_Pagamento == ("Visa" or "Mastercard"):#Se Visa o Mastercard
            commissioni = 1.5
        elif Ordine.Metodo_Pagamento == "Bancomat":#Se Bancomat
            commissioni = 0.5
        elif Ordine.Metodo_Pagamento == "Contanti":#Se Contanti
            commissioni = 0.0

        Ordine.Totale += commissioni#Aggiunta commisioni a prezzo finale

        # Mostra il messaggio di conferma
        messagebox.showinfo("Ordine Completato", f"Ordine completato con successo a nome di {Ordine.Intestatario} con tavolo n°{Ordine.Numero_Tavolo} con {Ordine.Numero_Persone} persone, pagamento con {Ordine.Metodo_Pagamento}.\nPrezzo finale = €{Ordine.Totale:.2f}")
        self.w1.destroy()#Chiudi ultima finestra