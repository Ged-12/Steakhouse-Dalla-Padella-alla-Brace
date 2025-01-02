import random               #Importa modulo random

class Ristorante:           
    Numero_Tavoli:int = 6
    Persone_per_tavolo:int = 4
    Occupazione_Tavoli = []

    def __init__(self):
        self.Random_Tavoli()

    #Modulo per generazione randomica occupazione tavoli
    def Random_Tavoli(self):
        while True:
            for i in range(self.Numero_Tavoli):
                self.Occupazione_Tavoli.append(random.choice([True, False]))
            
            cont = 0
            for i in range(self.Numero_Tavoli):
                if(self.Occupazione_Tavoli[i] == True):
                    cont += 1
            if(cont != self.Numero_Tavoli):
                break

    #Creazione Menu con struttura string:[float:list(string)]
    Menu= {
        "Bistecca Fiorentina": {
        "prezzo": 34.99,
        "ingredienti": ["bistecca di manzo", "sale", "pepe", "olio d'oliva"]
        },
        "Filetto di Manzo": {
            "prezzo": 27.99,
            "ingredienti": ["filetto di manzo", "sale", "pepe", "burro"]
        },
        "Costine di Maiale": {
            "prezzo": 21.99,
            "ingredienti": ["costine di maiale", "salsa barbecue", "sale", "pepe"]
        },
        "Pollo alla Griglia": {
            "prezzo": 17.99,
            "ingredienti": ["petto di pollo", "olio d'oliva", "sale", "pepe", "rosmarino"]
        },
        "Arrosto di Vitello": {
            "prezzo": 30.00,
            "ingredienti": ["spalla di vitello", "sale", "pepe", "vino bianco", "aglio"]
        },
        "Salsiccia alla Brace": {
            "prezzo": 14.99,
            "ingredienti": ["salsiccia di maiale", "sale", "pepe", "finocchio"]
        },
        "Spezzatino di Manzo": {
            "prezzo": 24.99,
            "ingredienti": ["manzo", "carote", "cipolla", "vino rosso", "brodo"]
        },
        "Pollo alla Cacciatora ": {
            "prezzo": 20.00,
            "ingredienti": ["pollo", "pomodori", "olive", "cipolla", "vino bianco"]
        },
        "Hamburger di Manzo": {
            "prezzo": 16.99,
            "ingredienti": ["carne macinata di manzo", "pane per hamburger", "lattuga", "pomodoro", "formaggio"]
        },
        "Patate al Forno": {
            "prezzo": 4.99,
            "ingredienti": ["patate", "olio d'oliva", "rosmarino", "sale"]
        },
        "Insalata Mista": {
            "prezzo": 5.99,
            "ingredienti": ["lattuga", "pomodori", "cetrioli", "olio d'oliva", "aceto"]
        },
        "Verdure Grigliate": {
            "prezzo": 6.99,
            "ingredienti": ["zucchine", "melanzane", "peperoni", "olio d'oliva", "sale"]
        },
        "Carote Marinate": {
            "prezzo": 4.50,
            "ingredienti": ["carote", "aceto balsamico", "olio d'oliva", "aglio", "prezzemolo"]
        },
        "Chips di Cavolo Riccio": {
            "prezzo": 3.99,
            "ingredienti": ["cavolo riccio", "olio d'oliva", "sale"]
        },
        "Fagiolini Saltati": {
            "prezzo": 6.50,
            "ingredienti": ["fagiolini", "aglio", "olio d'oliva", "sale"]
        },
        "Zucchine Grigliate": {
            "prezzo": 5.50,
            "ingredienti": ["zucchine", "olio d'oliva", "sale", "pepe"]
        },
        "Olive Miste Condite": {
            "prezzo": 4.99,
            "ingredienti": ["olive verdi", "olive nere", "olio d'oliva", "peperoncino", "aglio", "prezzemolo"]
        },
        "Carciofi alla Romana": {
            "prezzo": 7.99,
            "ingredienti": ["carciofi", "aglio", "prezzemolo", "olio d'oliva"]
        },
        "Fetta di Tiramisù": {
            "prezzo": 5.99,
            "ingredienti": ["mascarpone", "caffè", "savoiardi", "cacao", "zucchero"]
        },
        "Panna Cotta": {
            "prezzo": 5.50,
            "ingredienti": ["panna", "zucchero", "gelatina", "vaniglia"]
        },
        "Cheesecake": {
            "prezzo": 6.99,
            "ingredienti" : ["formaggio cremoso", "biscotti", "burro", "zucchero", "uova"]
        },
        "Fetta di Torta di Mele": {
            "prezzo": 4.50,
            "ingredienti": ["mele", "farina", "zucchero", "uova", "burro"]
        },
        "Fetta di Pastiera": {
            "prezzo": 6.50,
            "ingredienti": ["grano cotto","ricotta", "zucchero", "uova", "burro", "farina", "aromi", "scorza di limone"]
        },
        "Profiteroles": {
            "prezzo": 6.50,
            "ingredienti": ["pasta choux", "crema", "cioccolato"]
        },
        "Fetta di Torta al Cioccolato": {
            "prezzo": 4.99,
            "ingredienti": ["cioccolato", "farina", "zucchero", "uova", "burro"]
        },
        "Millefoglie": {
            "prezzo": 6.50,
            "ingredienti": ["pasta sfoglia", "crema pasticcera", "zucchero a velo"]
        },
        "Mousse al Cioccolato": {
            "prezzo": 6.50,
            "ingredienti": ["cioccolato fondente", "panna", "zucchero", "uova"]
        },
        "Acqua Naturale": {
            "prezzo": 0.99,
            "ingredienti": ["acqua"]
        },
        "Acqua Frizzante": {
            "prezzo": 1.49,
            "ingredienti": ["acqua", "anidride carbonica"]
        },
        "Coca-Cola": {
            "prezzo": 2.50,
            "ingredienti": ["coca-cola"]
        },
        "Fanta": {
            "prezzo": 2.50,
            "ingredienti": ["fanta"]
        },
        "Sprite": {
            "prezzo": 2.50,
            "ingredienti": ["sprite"]
        },
        "Birra Peroni": {
            "prezzo": 3.50,
            "ingredienti": ["birra peroni"]
        },
        "Birra Guinness": {
            "prezzo": 3.50,
            "ingredienti": ["birra guinness"]
        },
        "Birra Artigianale": {
            "prezzo": 4.99,
            "ingredienti": ["acqua", "malto", "luppolo", "lievito"]
        },
        "Vino Rosso": {
            "prezzo": 19.99,
            "ingredienti": ["uva rossa", "acqua", "zucchero"]
        }
    }
class Ordine:
    Numero_Persone:int = 0      #Numero persone selezionate
    Numero_Tavolo:int = 0       #Tavolo selezionato
    Intestatario:str = ""       #Intestatario scelto
    Ordinazione = {}            #Ordine prodotti scelti con struttura string:int
    Totale:float = 0.0          #Totale costo ordine
    Metodo_Pagamento:str = ""   #Metodo di pagamento scelto