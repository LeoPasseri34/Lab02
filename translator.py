from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.d= Dictionary()

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("------------------------------------")
        print("Traduttore Alieno-Italiano")
        print("------------------------------------")
        print("1- Stampa il dizionario")
        print("2- Inserire una nuova parola")
        print("3- Cercare una traduzione")
        print("4- Cercare con wildcard")
        print("5- Exit")


    def loadDictionary(self, dict):
        infile = open(dict, "r")
        dizionario = {}
        for line in infile:
            #print(line)
            linea = line[:len(line)-1]
            linea = linea.split(" ")
            dizionario[linea[0]] = linea[1:]
        self.d.aggiorna(dizionario)
        infile.close()


    def stampaDizio(self):
        print(self.d.stampa())


    def handleAdd(self, entry):
        flag = True
        if entry[0].isalpha():
            for i in entry[1]:
                if i.isalpha():
                    pass
                else: flag = False
        else: flag = False

        if flag:
            if entry[0] in self.d.dizionario:
                self.d.aggiungiParola(entry[0], entry[1])
            else:
                self.d.addWord(entry[0], entry[1])
        else: print("Errore")


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        print(self.d.translate(query))


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        print(self.d.translateWordWildCard(query))
        pass

    def copiaDizionario(self, nomefile):
        self.d.scrivi()
